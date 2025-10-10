class Calculator:
    operators = ['+', '-', '*', '/']     # Поддерживаемые операторы

    # Превращает expression в два списка по методу "Обратной польской записи"
    # Принимает: expression - математическое выражение записанное в одну строку
    # Возвращает: Два списка типа List[str]
    # 1 - Список операторов
    # 2 - Список чисел
    def makeRPN(self, expression:str) -> [list[str],list[str]]:
        pass

    def calc(self, expression:str) -> float:
        numbers = []
        operators = []




print("Добро пожаловать в калькулятор!")
print("Введите математическое выражение в одну строку")
print("Поддерживаемые операторы: ", [c for c in Calculator.operators])
print()

inp = input()                               # Ввод значения
inp = inp.replace(" ", "")     # Убираем лишние пробелы
