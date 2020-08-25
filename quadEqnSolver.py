import cmath as cm

print('Welcome to Quadratic Solver App')
'''
A quadratic equation of form ax^2+bx+c=0. This will be converted to
form a+bj, where a is real number portion and b is complex
'''
noOfEqns = int(input('How many equations would you like to solve: '))

for eqn in range(noOfEqns):
    print('Solving Equation #{eqn}\n--------------------')
    a = float(input('Enter the value for a,coefficient of x^2: '))
    b = float(input('Enter the value for b,coefficient of x: '))
    c = float(input('Enter the value for c,constant: '))
    print('Solving the quadratic Eqns. now: ')
    x1 = (-b + (cm.sqrt(b ** 2 - (4 * a * c)))) / (2 * a)
    x2 = (-b - (cm.sqrt(b ** 2 - (4 * a * c)))) / (2 * a)
    print(f'The solution to {a}x^2+({b})x+{c}=0 are: \n\t{x1}\n\t{x2}')

print('Thank you for using Quadratic Eqn. Solver App..!')
