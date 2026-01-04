product_scan_code = []
with open('product.csv', 'r', encoding='utf-8') as file:
    for line in file:
        name, price = line.strip().split(',')
        product_scan_code.append([name, price])
print(product_scan_code)

while True:
    product_name = input('請輸入商品名稱: ')
    if product_name == 'q':
        break
    price = input('請輸入商品價格: ')
    product_scan_code.append([product_name, price])
print('商品清單: ', product_scan_code)
for product in product_scan_code:
    print(product[0], '的價格為', product[1])

with open('product.txt', 'w') as file:
    for product in product_scan_code:
        file.write(product[0] + ',' + str(product[1]) + '\n')

with open('product.csv', 'w', encoding = 'utf-8') as file:
    file.write('商品, 價格\n')
    for product in product_scan_code:
        file.write(product[0] + ',' + str(product[1]) + '\n')