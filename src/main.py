from src.services import get_random_seq, get_points


def main():
    users: dict[int, int] = {}
    users_number = int(input("Введите кол-во игроков: "))
    round_now = 1
    round_count = 2
    while round_now <= round_count:
        user_now = 1
        print("")
        print("Текущий раунд: ", round_now)
        while user_now <= users_number:
            print("Сейчас ход игрока №", user_now)
            input("Нажмите Enter для продолжения...")
            seq = get_random_seq()
            print("Рандомная последовательность: ", seq)
            points = get_points(seq)
            users[user_now] += points
            user_now += 1
        round_now += 1

    print("Итоги игры:")
    for user, points in users.items():
        print(f"Игрок №{user} - Сумма очков: {points}")


if __name__ == "__main__":
    main()
