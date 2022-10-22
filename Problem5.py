# tt=int(input())
for i in range(0, 50, 1):
    if i % 5 == 0 and i % 3 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('FizZ')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
