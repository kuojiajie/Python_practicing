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

filter_comment_lower_100_word = []
for comment_lower_100_word in data:
    if len(comment_lower_100_word) < 100:
        filter_comment_lower_100_word.append(comment_lower_100_word)
print('超過100字的留言有', len(filter_comment_lower_100_word), '則')
print(filter_comment_lower_100_word[0])

filter_comment_include_good = []
for comment_include_good in data:
    if 'good' in comment_include_good:
        filter_comment_include_good.append(comment_include_good)
print('提到good的留言有', len(filter_comment_include_good), '則')
print(filter_comment_include_good[0])
