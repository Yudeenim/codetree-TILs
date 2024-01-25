class Product:
    def __init__(self, prod_id, code):
        self.prod_id = prod_id
        self.code = code

product1 = Product("codetree", 50)

prod2_id, code2 = tuple(input().split())

product2 = Product(prod2_id, int(code2))

print(f"product {product1.code} is {product1.prod_id}")
print(f"product {product2.code} is {product2.prod_id}")