from src.services import get_random_seq, get_points, get_arifmetical_sum


def init_users_dict(users: int) -> dict:
    users_dict: dict = {}

    for i in range(1, users + 1):
        users_dict[i] = {
            "points": 0,
            "prem": False,
        }

    return users_dict


def main():
    users_number = 0

    while users_number < 2:
        try:
            users_number = int(input("Введите кол-во игроков: "))
        except KeyboardInterrupt:
            raise KeyError("close")
        except:
            pass

    users = init_users_dict(users_number)

    round_now = 1
    round_count = 10
    while round_now <= round_count:
        user_now = 1
        print("\n\n----==== Текущий раунд: ", round_now, "====----")
        while user_now <= users_number:
            total_points = 0
            print("\nСейчас ход игрока №", user_now)
            input("Нажмите Enter для продолжения...")
            # seq = get_random_seq(True)
            seq = get_random_seq()
            print("Рандомная последовательность: ", seq)
            points = get_points(seq)

            total_points = points * 50 + get_arifmetical_sum(seq) * 10

            if users[user_now]["prem"] == False and points == 7:
                users[user_now]["prem"] = True
                total_points += 100
                print("Начислена премия игроку: ", user_now)

            print("Кол-во баллов: ", round(total_points))
            users[user_now]["points"] += total_points
            user_now += 1
        round_now += 1

    print("\n\n------====== Итоги игры: ======------")
    victory_users = []
    max = 0
    for user, data in users.items():
        a = round(data["points"])
        print(f" ---=== Игрок №{user} - Сумма баллов: {a}")
        if data["points"] > max:
            max = data["points"]

    for user, data in users.items():
        if data["points"] == max:
            victory_users.append(user)

    if len(victory_users) == 1:
        print(f"Победил игрок: {victory_users[0]}")
    else:
        print("Ничья")

    print()


if __name__ == "__main__":
    main()
