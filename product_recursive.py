def product_recursive(a, b):
    if a < b:
        return product_recursive(b, a)
    if b == 0:
        return 0
    return a + product_recursive(a, b-1)


print(product_recursive(10, 100))