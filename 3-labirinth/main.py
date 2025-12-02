import random

class Player:
    def __init__(self):
        self.hp = 100  # Здоровье игрока
        self.mana = 50  # Мана для использования навыков
        self.attack = 15  # Сила атаки
        self.defense = 5  # Защита

def player_skills(mana: int, attack: int):
    damage = 0
    print("Доступные навыки:\n1) Базовая атака (Расход маны: 0, Урон: 100% от атаки)\n2) Сильная атака (Расход маны: 10, Урон: 150% от атаки)\n3) Особая атака (Расход маны: 20, Урон: 200% от атаки)")
    print("Выберите навык для использования:")

    while damage == 0:
        try:
            ch = int(input())
            if ch == 1:
                damage = attack  # Базовая атака без затрат маны
            elif ch == 2:
                if mana >= 10:
                    damage = int(attack * 1.5)  # Урон увеличен на 50%
                    mana -= 10  # Тратится мана
                else:
                    print("Недостаточно маны для этого навыка. Выберите другой:")
            elif ch == 3:
                if mana >= 20:
                    damage = int(attack * 2.0)  # Урон увеличен в 2 раза
                    mana -= 20  # Тратится мана
                else:
                    print("Недостаточно маны для этого навыка. Выберите другой:")
            else:
                print("Неверный выбор. Пожалуйста, выберите 1, 2 или 3:")
        except ValueError:
            print("Пожалуйста, введите число:")

    return [mana, damage]

class Monster:
    def __init__(self):
        self.hp = 60  # Здоровье монстра
        self.attack = 12  # Атака монстра
        self.defense = 3  # Защита монстра

def fight_monster(player_hp: int, player_mana: int, player_attack: int, backpack: list):
    monster = Monster()
    print("Вы встретили Монстра!")
    print(f'Здоровье врага: {monster.hp}')
    print(f'Атака врага: {monster.attack}')
    print(f'Защита врага: {monster.defense}')

    # Проверка на наличие яда в инвентаре
    if 'Poison' in backpack:
        print('Хотите использовать яд перед боем? (Y/N)')
        ans = str(input()).upper()
        if ans == 'Y':
            backpack.remove('Poison')
            monster.hp -= 20  # Яд наносит урон монстру
            print("Вы использовали яд! Монстр потерял 20 HP.")

    # Цикл боя
    while monster.hp > 0 and player_hp > 0:
        print(f'\nЗдоровье врага: {monster.hp}')
        print(f'Ваше здоровье: {player_hp}')
        print(f'Ваша мана: {player_mana}')

        # Ход игрока
        fight_res = player_skills(player_mana, player_attack)
        player_mana = fight_res[0]
        damage = max(0, fight_res[1] - monster.defense)  # Учитываем защиту монстра
        monster.hp -= damage
        print(f"Вы нанесли {damage} урона монстру!")

        # Проверка на победу
        if monster.hp <= 0:
            break

        # Ход монстра
        monster_damage = max(0, monster.attack - 2)  # Игрок имеет базовую защиту
        player_hp -= monster_damage
        print(f"Монстр атакует! Вы получаете {monster_damage} урона.")

    # Восстановление маны после боя
    player_mana = min(50, player_mana + 5)

    return [monster.hp, player_hp, player_mana, backpack]

def chest_loot(backpack: list):
    items = ['Healing potion', 'Power Up', 'Poison']
    item = random.choice(items)  # Случайный предмет из сундука
    backpack.append(item)
    print(f'Вы нашли {item}!')

    # Описание предметов
    if item == 'Healing potion':
        print('Зелье лечения: Восстанавливает 20 HP при использовании.')
    elif item == 'Power Up':
        print('Усиление: Постоянно увеличивает ваши характеристики.')
    elif item == 'Poison':
        print("Яд: Наносит 20 урона врагу в начале боя.")

    return backpack

def use_healing_potion(hp: int, backpack: list):
    if 'Healing potion' in backpack:
        backpack.remove('Healing potion')
        hp = min(100, hp + 20)  # Лечение, но не больше максимума
        print('Ваше здоровье восстановлено на 20!')
    else:
        print("У вас нет зелий лечения.")
    return [hp, backpack]

def use_power_up(player: Player, backpack: list):
    if 'Power Up' in backpack:
        backpack.remove('Power Up')
        # Увеличение всех характеристик
        player.hp += 10
        player.attack += 5
        player.defense += 2
        print('Ваши характеристики увеличены!')
    else:
        print("У вас нет усилений.")
    return backpack

def show_backpack(backpack: list):
    if not backpack:
        print("Ваш рюкзак пуст.")
    else:
        print("В вашем рюкзаке:")
        for item in set(backpack):
            print(f"- {item}: {backpack.count(item)}")  # Показываем количество каждого предмета

def show_stats(player: Player):
    print(f"HP: {player.hp}/100")
    print(f"Мана: {player.mana}/50")
    print(f"Атака: {player.attack}")
    print(f"Защита: {player.defense}")

# Основная игра
def main():
    print("Добро пожаловать в Подземелье!")
    print("Пройдите через подземелье, найдите портал и сбегите!")

    # Создание игрока
    player = Player()

    # Создание подземелья
    print('Какой размер лабиринта вы хотите? (Введите n m):')
    try:
        n, m = map(int, input().split())
    except:
        n, m = 5, 5  # Размер по умолчанию

    # Типы комнат: E-Пустая, C-Сундук, M-Монстр
    rooms = ['E', 'C', 'M']
    labyrinth = [[random.choice(rooms) for _ in range(n)] for _ in range(m)]
    labyrinth[m-1][n-1] = 'P'  # Портал в конце
    labyrinth[0][0] = 'E'  # Стартовая позиция

    # Отображение карты
    lab_interface = [['*' for _ in range(n)] for _ in range(m)]
    lab_interface[0][0] = 'X'  # Позиция игрока

    x, y = 0, 0  # Координаты игрока
    backpack = []  # Инвентарь
    has_key = False  # Найден ли ключ

    print("\nУправление:")
    print("w - вверх, s - вниз, a - влево, d - вправо")
    print("stats - показать характеристики, backpack - показать инвентарь")
    print("heal - использовать зелье лечения, powerup - использовать усиление")

    # Главный игровой цикл
    while player.hp > 0:
        # Отображение карты
        print("\nТекущее подземелье:")
        for row in lab_interface:
            print(' '.join(row))
        print("X - ваша позиция, * - неисследованные комнаты")

        print('\nВведите команду:')
        command = input().lower()

        moved = False
        old_x, old_y = x, y  # Старые координаты для обновления карты

        # Обработка движения
        if command == 'w' and y > 0:
            y -= 1  # Движение вверх
            moved = True
        elif command == 's' and y < m-1:
            y += 1  # Движение вниз
            moved = True
        elif command == 'a' and x > 0:
            x -= 1  # Движение влево
            moved = True
        elif command == 'd' and x < n-1:
            x += 1  # Движение вправо
            moved = True

        # Если игрок переместился
        if moved:
            lab_interface[old_y][old_x] = 'E'  # Помечаем старую позицию как исследованную
            lab_interface[y][x] = 'X'  # Помечаем новую позицию

            room_type = labyrinth[y][x]
            print(f"\nВы входите в новую комнату...")

            if room_type == 'E':
                print("Эта комната пуста.")
                player.mana = min(50, player.mana + 5)  # Восстановление маны

            elif room_type == 'C':
                print("Вы нашли сундук!")
                backpack = chest_loot(backpack)
                player.mana = min(50, player.mana + 5)

            elif room_type == 'M':
                result = fight_monster(player.hp, player.mana, player.attack, backpack)
                if result[1] <= 0:
                    print("Вы побеждены! Игра окончена.")
                    break
                player.hp = result[1]
                player.mana = result[2]
                backpack = result[3]
                if player.hp > 0:
                    print("Вы победили монстра!")
                    # Шанс найти ключ после победы над монстром
                    if not has_key and random.random() < 0.3:
                        has_key = True
                        print("Вы нашли ключ! Теперь вы можете использовать портал.")

            elif room_type == 'P':
                if has_key:
                    print("Поздравляем! Вы нашли портал и сбежали из подземелья!")
                    break
                else:
                    print("Вы нашли портал, но вам нужен ключ чтобы активировать его!")
                    player.mana = min(50, player.mana + 5)

        # Обработка других команд
        elif command == 'stats':
            show_stats(player)
        elif command == 'backpack':
            show_backpack(backpack)
        elif command == 'heal':
            result = use_healing_potion(player.hp, backpack)
            player.hp = result[0]
            backpack = result[1]
        elif command == 'powerup':
            backpack = use_power_up(player, backpack)

        # Проверка на смерть игрока
        if player.hp <= 0:
            print("Вы погибли! Игра окончена.")
            break

    print("Спасибо за игру!")

if __name__ == "__main__":
    main()