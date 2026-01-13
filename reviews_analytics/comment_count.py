data = []
count = 0
with open('reviews.txt', 'r') as file:
    for line in file:
        data.append(line)
        if count % 1000 == 0:
            print(len(data))
print('讀取完畢，一共有', len(data), '則留言')

print('第1則留言: ', data[0])

word_count = {}
for line in data:
    words = line.split(' ')
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1 #新增key，value為1
    
for word in word_count:
    if word_count[word] > 100:
        print(word, word_count)

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



