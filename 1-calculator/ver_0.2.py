class Calculator:
    def calc(self, a, b, c):
        match(c):
            case '+':
                return a + b
            case '-':
                return a - b
            case '*':
                return a * b
            case '/':
                if b == 0:
                    raise ValueError("ERROR: Деление на ноль!")
                return a / b
            case _:
                raise ValueError(f"Неизвестная операция: {c}")

try:
    a = float(input("Введите первое число:\n"))
    op = input("Введите операцию (+, -, *, /):\n")
    b = float(input("Введите второе число:\n"))

    calculator = Calculator()
    result = calculator.calc(a, b, op)
    print(f"Результат: {result}")

except ValueError as e:
    print(f"Ошибка: {e}")
except Exception as e:
    print(f"Неожиданная ошибка: {e}")
