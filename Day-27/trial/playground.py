def add(*args):
    result = 0
    for arg in args:
        result += arg
    return result

print(add(1))
print(add(1,2))
print(add(1,2,3,4,5))
