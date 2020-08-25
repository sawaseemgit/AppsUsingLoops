print('Welcome to Fibonacci Sequence App')
number = int(input('How many digits of fibo seq would you like to compute: '))
print(f'The first {number} of the Fibo Seq are: ')
fsum = 0;
fibNum = [1, 1]
for i in range(number - 2):
    # if i>1:
    fsum = fibNum[i] + fibNum[i + 1]
    (fibNum.append(fsum))

print(f'The first {number} numbers in Fibonacci Seq are: ')
for num in fibNum:
    print(num)

ratios = []
for i in range(len(fibNum) - 1):
    ratio = fibNum[i + 1] / fibNum[i]
    ratios.append(ratio)

print('The corresponding Golden Ratio values are: ')
for ratio in ratios:
    print(ratio)