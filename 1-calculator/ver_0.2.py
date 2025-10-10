class Calculator:
    def calc(self,a,b,c):
        res = 0
        match(c):
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
        return res

a = float(input("Введите первое число:\n"))
op = input("Введите операцию (+, -, *, /):\n")
b = float(input("Введите второе число:\n"))


print(Calculator.calc(None, a,b,op))
