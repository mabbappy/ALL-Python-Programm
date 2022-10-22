def double_it(num):
    result = num*2
    return result


# double_it(50)
def add(num, num1):
    x = num+num1
    return x


sum = add(2, 4)
print(sum)


# add(2, 3)
def multiply(num, num1):
    result = num*num1
    return result


output = multiply(25, 2)
print(output)
# multiply(2, 3)
again_double = add(sum, output)
print(again_double)
