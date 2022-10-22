balance = 580


def total_cost(price, quantity):
    cost = price*quantity
    remaining = balance-cost
    print(remaining)
    return cost


pay = total_cost(10, 3)
print(f'please pay:{pay}')
