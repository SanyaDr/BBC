a = float(input("Введите первое число:\n"))
op = input("Введите операцию (+, -, *, /):\n")
b = float(input("Введите второе число:\n"))
res = float(0.0)

match(op):
    case '+':
        res = a + b
    case '-':
        res = a - b
    case '*':
        res = a * b
    case '/':
        if b == 0:
            print("ERROR: Деление на ноль!")
        else:
            res = a / b

print(res)