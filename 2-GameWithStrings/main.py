from turtledemo.paint import switchupdown


def lvl_1():
    print("\n\nУровень 1!")
    inp = input("Введите строку для работы: ")
    print(inp, "+", "upper() ->", inp.upper())
    print(inp, "+", "lower() ->", inp.lower())
    print(inp, "+", "capitalize ->", inp.capitalize())

def lvl_2():
    print("\n\nУровень 2!")
    inp = input("Введите строку со словом 'круто': ")
    print(inp, "+ find('круто') ->", inp.lower().find("круто"))
    print(inp, "+ replace('круто', 'ужас') ->", inp.replace("круто", "ужас"))
    print(inp, f"+ count('о') ->", inp.lower().count("о"))

def lvl_3():
    print("\n\nУровень 3")
    inp = input("Введите строку с символами ',': ")
    print(f"'{inp}' + split(',') ->", inp.split(','))
    print(f"'{inp}' + join(';') ->", ";".join(inp.split(',')))

def lvl_4():
    print("\n\nУровень 4")
    inp1 = input("Введите число: ")
    inp2 = input("Введите строку: ")
    inp3 = input("Введите строку с пробелами: ")

    print(f"'{inp1}' + isdigit() ->", inp1.isdigit())
    print(f"'{inp2}' + isalpha() ->", inp2.isalpha())
    print(f"'{inp3}' + strip() -> '{inp3.strip()}'")

def lvl_5():
    inp = input("Введите 'грязную' строку для нормализации: ")
    print(f"'{inp}' ->", " ".join(inp.strip().lower().split(";")).capitalize())

selectedLevel = -1
while selectedLevel != 0:
    selectedLevel = int(input("\nВведите уровень игры от 1 до 5. 0 - для выхода: "))
    match selectedLevel:
        case 1:
            lvl_1()
        case 2:
            lvl_2()
        case 3:
            lvl_3()
        case 4:
            lvl_4()
        case 5:
            lvl_5()
