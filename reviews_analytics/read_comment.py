data = []
count = 0
with open('reviews.txt', 'r') as file:
    for line in file:
        data.append(line)
        if count % 1000 == 0:
            print(len(data))
print('讀取完畢，一共有', len(data), '則留言')

print('第1則留言: ', data[0])
print('第2則留言: ', data[1])
print('第666666則留言: ', data[666665])

sum_len = 0
for comment in data:
    sum_len += len(comment)
print('每則留言平均有', sum_len / len(data), '字')