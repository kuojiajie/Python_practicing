import os

def read_file(filename):
    product_scan_code = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if '商品, 價格' in line:
                continue
            name, price = line.strip().split(',')
            product_scan_code.append([name, price])
    return product_scan_code

def user_input(product_scan_code):
    while True:
        product_name = input('請輸入商品名稱: ')
        if product_name == 'q':
            break
        price = input('請輸入商品價格: ')
        product_scan_code.append([product_name, price])
    print('商品清單: ', product_scan_code)
    return product_scan_code

def print_product(product_scan_code):
    for product in product_scan_code:
        print(product[0], '的價格為', product[1])

def write_file(filename, product_scan_code):
    with open(filename, 'w', encoding = 'utf-8') as file:
        file.write('商品, 價格\n')
        for product in product_scan_code:
            file.write(product[0] + ',' + str(product[1]) + '\n')

def main():
    filename = 'products.csv'
    if os.path.isfile(filename):
        print('file exist')
        products = read_file(filename)
    else:
        print('file not found')
        products = []
    products = user_input(products)
    print_product(products)
    write_file('products.csv', products)

main()