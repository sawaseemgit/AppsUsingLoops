import math
print('Welcome the Factorial Calculator App')
number = int(input('What number you would like to compute Factorial of: '))
number1=number
print(f'{number}! = ', end='')
for i in range(1,number1):
    print(i, end='*')
print(number1)

fact = 1
while number > 1:
    if number > 1:
        fact *= number
        number -= 1

print(f'\nFactorial of number {number1}, from my own algorithm is: ', fact)
print(f'Factorial of number {number1}, from math library is: ',math.factorial(number1))

