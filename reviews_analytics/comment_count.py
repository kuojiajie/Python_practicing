import time
import progressbar

data = []
count = 0
start_time = time.time()
bar = progressbar.ProgressBar(maxval = 1000000)
bar.start()
with open('reviews.txt', 'r') as file:
    for line in file:
        data.append(line)
        count += 1
        bar.update(count)
bar.finish() 
end_time = time.time()
print('讀取時間:', end_time - start_time,'秒')
print('讀取完畢，一共有', len(data), '則留言')

print('第1則留言: ', data[0])

word_count = {}
start_time = time.time()
for line in data:
    words = line.split(' ')
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1 #新增key，value為1
    
for word in word_count:
    if word_count[word] > 1000000:
        print(word, word_count[word])
end_time = time.time()
print('計算時間:', end_time - start_time,'秒')
print(len(word_count))
print(word_count['jack'])

while True:
    word = input('請問你想查什麼字: ')
    if word == 'q':
        break
    if word in word_count:
        print(word, '出現過的次數為', word_count[word])
    else:
        print('查無此字')

print('感謝使用本功能')



