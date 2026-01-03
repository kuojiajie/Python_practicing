password = 'a123456'
i = 3
while i > 0:
    i = i - 1
    pwd = input('請輸入密碼: ')
    if pwd == password:
        print('登入成功')
        break
    else:
        if i == 0:
            print('密碼輸入錯誤 3 次，請等候15分鐘再重試')
            break
        print('密碼錯誤!還有', i, '次機會')