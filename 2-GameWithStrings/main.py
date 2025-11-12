def lvl_1():
    print("\n\nLVL 1")
    text_1 = "приВет МИР"
    print("Оригинальная строка: ", text_1)
    print("upper()  -> ", text_1.upper())
    print("lower()  -> ", text_1.lower())
    print("capitalize()  -> ", text_1.capitalize())

def lvl_2():
    print("\n\nLVL 2")
    text_2 = ("Ботать круто! Очень круто!")
    print("Оригинальная строка  -> ", text_2)
    print("Вхождение первого 'круто'  -> ", text_2.find("круто"))
    print("Замена 'круто' на что-то  -> ", text_2.replace("круто!", "грустно :(").replace("очень", "ваще"))
    print("Количество букв 'О'  -> ", text_2.count('о'))

def lvl_3():
    print("\n\nLVL 3")
    text_3="1,2,3,4,5"
    print("Оригинальная строка  -> ", text_3)
    print("Разделение по запятым  -> ", text_3.split(","))
    print("Соединение без запятых  -> ", "".join(text_3.split(",")))

def lvl_4():
    print("\n\nLVL 4")
    text_4 = ["   1234#*   ", "  ABC#12   "]
    i = 1
    for txt in text_4:
        print("Оригинальная строка  ->  '", txt, "'", sep='')
        print("Вывод только чисел  -> ", [c for c in txt if c.isdigit()])
        print("Вывод только букОв  -> ", [c for c in txt if c.isalpha()])
        print("strip()  ->  '", txt.strip(), "'", sep='')
        print("f-строки  -> ", f"{i}-я строка!")
        print("format  -> ", "{first} круче чем {second}!!!".format(first=text_4[0].strip(), second=text_4[1].strip()))
        print("---------------")
        i += 1

print("Приветствуем на самой тупой игре")
lvl_1()
lvl_2()
lvl_3()
lvl_4()
