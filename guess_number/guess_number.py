import random

start = input ('請輸入數字範圍(起始值): ')
start = int(start)
end = input('請輸入數字範圍(結束值): ')
end = int(end)

ans = random.randint(start, end)
count = 0

print('遊戲開始')
while True:
    num = input('請猜一個數字:')
    num = int(num)
    count += 1
    if num == ans:
        print('恭喜!，數字', num,'猜中了!')
        print('總共猜了', count,'次')
        break
    elif num > ans:
        print('您猜的數字: ', num, ' 比答案大，再猜小一點!')
    elif num < ans:
        print('您猜的數字: ', num, ' 比答案小，再猜大一點!')
    print('您猜', count, '次了')
print('遊戲結束')