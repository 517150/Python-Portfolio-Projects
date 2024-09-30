a = int(input('Number: '))
b = input('Sign: ')
c = int(input('Number: '))

print(f'{a} {b} {c}')

if b == '+':
    x = a + c
    print(x)
elif b == '-':
    x = a - c
    print(x)
elif b == '*':
    x = a * c
    print(x)
elif b == '/':
    x = a / c
    print(x)
else:
    print('Invalid operation!')
