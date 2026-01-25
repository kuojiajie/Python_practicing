import psutil      # 用來取得 CPU / RAM 等系統資訊
import time        # 提供時間功能，例如 sleep (雖然這裡用 interval)
import pandas as pd  # 用來操作表格資料 (DataFrame)
import threading   # 用來建立子執行緒，不阻塞主程式

# 全域旗標，控制監控程式是否停止
stop_flag = False

# 建立一個等待 Enter 的函式，用來設定 stop_flag
def wait_enter():
    global stop_flag
    input("按 Enter 停止...\n")  # 這裡提示使用者按 Enter 停止收集
    stop_flag = True

# 開啟子執行緒，讓 wait_enter() 在背景執行，不阻塞主程式
threading.Thread(target=wait_enter, daemon=True).start()

# 建立空的 DataFrame，用來存放收集到的 CPU / RAM 資料
df = pd.DataFrame(columns=[
    'second',           # 經過的秒數
    'cpu_total_percent',# CPU 使用率
    'ram_total',        # RAM 總量
    'ram_available',    # RAM 可用量
    'ram_percent',      # RAM 使用百分比
    'ram_used',         # 已使用 RAM
    'ram_free'          # 空閒 RAM
])

# 一開始先印備註與欄位名稱，方便終端機查看
print("\n# idx: index, sec: elapsed seconds, CPU%: CPU usage, "
      "RAM_T(GB): total RAM, RAM_A(GB): available RAM, "
      "RAM_U(GB): used RAM, RAM_F(GB): free RAM")
print(f"{'idx':<4} {'sec':<6} {'CPU%':<10} {'RAM_T(GB)':<12} "
      f"{'RAM_A(GB)':<10} {'RAM_U(GB)':<10} {'RAM_F(GB)':<10}")

second = 0            # 用來記錄經過的秒數
display_index = 1     # 終端機顯示的索引，從 1 開始

# 主迴圈，每秒收集一次資料，直到使用者按 Enter
while not stop_flag:
    cpu_total_percent = psutil.cpu_percent(interval=1)  # 每秒取一次 CPU 使用率
    ram = psutil.virtual_memory()                        # 取得 RAM 狀態

    # 新增一列資料到 DataFrame，index 自動用 len(df)
    df.loc[len(df)] = [
        second, cpu_total_percent, ram.total, ram.available,
        ram.percent, ram.used, ram.free
    ]

    # 每 5 秒印一次最新一筆資料
    if second % 5 == 0:
        row = df.iloc[-1]  # 取最後一列
        # 將 RAM 轉換成 GB，保留兩位小數
        ram_total_gb = row['ram_total'] / 1e9
        ram_available_gb = row['ram_available'] / 1e9
        ram_used_gb = row['ram_used'] / 1e9
        ram_free_gb = row['ram_free'] / 1e9

        # 終端機列印格式化資料
        print(f"{display_index:<4} {row['second']:<6.1f} {row['cpu_total_percent']:<10.1f} "
              f"{ram_total_gb:<12.2f} {ram_available_gb:<10.2f} "
              f"{ram_used_gb:<10.2f} {ram_free_gb:<10.2f}")
        display_index += 1  # 顯示索引累加

    second += 1  # 經過秒數累加

# 停止後，計算各欄位平均值
cpu_avg = df['cpu_total_percent'].mean()
ram_total_avg = (df['ram_total'] / 1e9).mean()
ram_available_avg = (df['ram_available'] / 1e9).mean()
ram_used_avg = (df['ram_used'] / 1e9).mean()
ram_free_avg = (df['ram_free'] / 1e9).mean()

# 印出平均值
print("\n已收集完整資料，平均值:")
print(f"{'CPU%':<10} {'RAM_T(GB)':<12} {'RAM_A(GB)':<10} "
      f"{'RAM_U(GB)':<10} {'RAM_F(GB)':<10}")
print(f"{cpu_avg:<10.2f} {ram_total_avg:<12.2f} {ram_available_avg:<10.2f} "
      f"{ram_used_avg:<10.2f} {ram_free_avg:<10.2f}")

# 將完整資料存成 Excel，index 不寫入檔案
df.to_excel("CPU_RAM_tracing.xlsx", index=False)
