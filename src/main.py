from src.services import get_random_seq, get_points


def init_users_dict(users: int) -> dict:
    users_dict: dict = {}

    for i in range(1, users + 1):
        users_dict[i] = {
            "points": 0,
            "prem": False,
        }

    return users_dict


def main():
    users_number = int(input("Введите кол-во игроков: "))
    users = init_users_dict(users_number)
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
            # if users[user_now]["prem"] == False and points == 7:
            #     users[user_now]["prem"] = True
            #     users[user_now]["points"] += 100
            print("Кол-во очков: ", points)
            users[user_now]["points"] += points
            user_now += 1
        round_now += 1

    print("Итоги игры:")
    for user, data in users.items():
        print(f"Игрок №{user} - Сумма очков: {data["points"]}")


if __name__ == "__main__":
    main()
