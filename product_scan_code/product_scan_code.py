product_scan_code = []
while True:
    product_name = input('請輸入商品名稱: ')
    if product_name == 'q':
        break
    price = input('請輸入商品價格: ')
    product_scan_code.append([product_name, price])
print('商品清單: ', product_scan_code)
for product in product_scan_code:
    print(product[0], '的價格為', product[1])