print('Welcome to Binary/Hexadecimal Converter App')
max_number = int(input('Compute binary & hexadecimal values upto what number: '))
decimal = range(1, max_number + 1)
binary = []
hexa = []

for num in decimal:
    binary.append(bin(num))
    hexa.append(hex(num))
print('Generating lists is complete.')

print('Using slice, a portion of the list will be shown.')
startNumber = int(input('What decimal number would you like to start at: '))
endNumber = int(input('What decimal number would you like to stop at: '))
print(f'\tTable of values between {startNumber} and {endNumber}')
print('Decimal Value, Binary Value, Hexadecimal value')
for i in decimal[startNumber - 1:endNumber]:
    print(f'\t{i}\t{bin(i)}\t\t{hex(i)}')

input(f'Press Enter to see complete from 1 to {max_number}.')
print(f'\tSummary table of values between 1 and {max_number}:')
print('Decimal Value, Binary Value, Hexadecimal value')
for d,b,h in zip(decimal, binary, hexa):
    print(f'\t{d}\t{b}\t\t{h}')