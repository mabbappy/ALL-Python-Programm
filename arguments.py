from unittest import result


def add(num1, num2):
    total = num1+num2
    print(f"num1:{num1} and num2:{num2}")
    return total


result = add(12, 14)
print(result)


def multiply(num1, num2):
    result = num1*num2
    return result


output = multiply(45, 2)
print(output)


def multiply2(*numbers):
    print(numbers)
    result = 1
    for num in numbers:
        result *= num
    return result


final_result = multiply2(12, 3, 2)
print(final_result)
