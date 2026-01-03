height = input('請輸入身高(cm): ')
height = float(height)
weight = input('請輸入體重(kg): ')
weight = float(weight)
BMI = weight / ((height / 100) *(height / 100))
print('BMI= ', BMI)
if BMI < 18.5:
    print('體重過輕')
elif BMI >= 18.5 and BMI < 24:
    print('體重正常')
elif BMI >= 24 and BMI < 27:
    print('體重過重')
elif BMI >= 27 and BMI < 30:
    print('輕度肥胖')
elif BMI >= 30 and BMI < 35:
    print('中度肥胖')
else:
    print('重度肥胖')