import random


def get_arifmetical_sum(seq: list) -> int:
    numbers_dict = get_numbers_dict(seq)
    numbers_sum = 0
    count = 0
    for key, value in numbers_dict.items():
        if value > 1:
            numbers_sum += key * value
            count += value
    if count == 0:
        return 0
    return numbers_sum / count


def get_random_seq(flag: bool = False) -> list:
    # return [1, 1, 1, 1, 1]
    if flag:
        return [int(num) for num in input().split()]
    return [random.randint(1, 6) for _ in range(5)]


def get_numbers_dict(seq: list) -> dict:
    numbers_dict = {}

    for num in seq:
        if numbers_dict.get(num) == None:
            numbers_dict[num] = 1
        else:
            numbers_dict[num] += 1

    return numbers_dict


def get_points(seq: list) -> int:
    numbers_dict = get_numbers_dict(seq)
    values = list(numbers_dict.values())
    values.sort(reverse=True)
    if len(values) == 1:
        return 7

    max1, max2 = values[0], values[1]

    if max1 == 4:
        return 6

    if max1 == 3 and max2 == 2:
        return 5

    if max1 == 3:
        return 4

    if max1 == 2 and max2 == 2:
        return 3

    if max1 == 2:
        return 2

    return 1
