def read_products_from_file(filename):
    products = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.split()
            name = " ".join(parts[:-1])
            price = float(parts[-1])
            products.append((name, price))
    return products

def filter_products_by_price(products, min_price, max_price):
    return [product for product in products if min_price <= product[1] <= max_price]

def calculate_average_price(products):
    total_price = sum(product[1] for product in products)
    return total_price / len(products) if products else 0

filename = 'products.txt'
products = read_products_from_file(filename)

filtered_products = filter_products_by_price(products, 10, 50)
print("Товары стоимостью от 10 до 50 рублей:")
for product in filtered_products:
    print(f"{product[0]}: {product[1]} рублей")

average_price = calculate_average_price(products)
print(f"\nСредняя стоимость всех товаров: {average_price:.2f} рублей")
