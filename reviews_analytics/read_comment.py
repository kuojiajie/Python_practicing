data = []
count = 0
with open('reviews.txt', 'r') as file:
    for line in file:
        data.append(line)
        if count % 1000 == 0:
            print(len(data))
print('讀取完畢，一共有', count, '則留言')

print('第1則留言: ', data[0])
print('第2則留言: ', data[1])
print('第666666則留言: ', data[666665])