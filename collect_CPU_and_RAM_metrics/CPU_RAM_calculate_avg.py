import psutil
import time
import pandas as pd
import threading

stop_flag = False

def wait_enter():
    global stop_flag
    input("按 Enter 停止...\n")
    stop_flag = True

# 開啟子執行緒等待 Enter
threading.Thread(target=wait_enter, daemon=True).start()

# 建立空的 DataFrame
df = pd.DataFrame(columns=['second','cpu_total_percent','ram_total','ram_available','ram_percent','ram_used','ram_free'])

# 一開始先印備註與欄位
print("\n# idx: index, sec: elapsed seconds, CPU%: CPU usage, RAM_T(GB): total RAM, RAM_A(GB): available RAM, RAM_U(GB): used RAM, RAM_F(GB): free RAM")
print(f"{'idx':<4} {'sec':<6} {'CPU%':<10} {'RAM_T(GB)':<12} {'RAM_A(GB)':<10} {'RAM_U(GB)':<10} {'RAM_F(GB)':<10}")

second = 0
display_index = 1  # 顯示索引從1開始

while not stop_flag:
    # 每秒收集一次
    cpu_total_percent = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()

    # 新增一列資料
    df.loc[len(df)] = [second, cpu_total_percent, ram.total, ram.available, ram.percent, ram.used, ram.free]

    # 每 5 秒印一次最新一筆
    if second % 5 == 0:
        row = df.iloc[-1]
        ram_total_gb = row['ram_total'] / 1e9
        ram_available_gb = row['ram_available'] / 1e9
        ram_used_gb = row['ram_used'] / 1e9
        ram_free_gb = row['ram_free'] / 1e9
        print(f"{display_index:<4} {row['second']:<6.1f} {row['cpu_total_percent']:<10.1f} "
              f"{ram_total_gb:<12.2f} {ram_available_gb:<10.2f} {ram_used_gb:<10.2f} {ram_free_gb:<10.2f}")
        display_index += 1

    second += 1

# 停止後計算平均值
cpu_avg = df['cpu_total_percent'].mean()
ram_total_avg = (df['ram_total'] / 1e9).mean()
ram_available_avg = (df['ram_available'] / 1e9).mean()
ram_used_avg = (df['ram_used'] / 1e9).mean()
ram_free_avg = (df['ram_free'] / 1e9).mean()

print("\n已收集完整資料，平均值:")
print(f"{'CPU%':<10} {'RAM_T(GB)':<12} {'RAM_A(GB)':<10} {'RAM_U(GB)':<10} {'RAM_F(GB)':<10}")
print(f"{cpu_avg:<10.2f} {ram_total_avg:<12.2f} {ram_available_avg:<10.2f} {ram_used_avg:<10.2f} {ram_free_avg:<10.2f}")
