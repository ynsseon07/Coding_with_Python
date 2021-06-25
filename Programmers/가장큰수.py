def compare(a, b):
    if a+b > b+a:
        return a > b
    elif a+b < b+a:
        return b > a

print(compare(6, 10))