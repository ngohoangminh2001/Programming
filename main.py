from simple_calc import sum, sub, mul, div

if __name__ == '__main__':
    op = int(input('Which operation do you need? (0 = sum, 1 = sub, 2 = mul, 3 = division) '))
    a = int(input('a = '))
    b = int(input('b = '))
    if (op == 0):
        print('a + b = ', sum(a, b))
    elif (op == 1):
        print('a - b = ', sub(a, b))
    elif (op == 2):
        print('a * b = ', mul(a, b))
    elif (op == 3):
        print('a / b = ', div(a, b))