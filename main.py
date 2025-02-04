from deque.deque import Deque

def rabbits(target_month: int, rabbit_lifetime: int) -> int:
    """Возвращает количество пар кроликов в популяции на заданный месяц.
    В начальный момент времени имеется одна пара кроликов. Начиная со второго
    месяца после рождения пара кроликов производит новую пару каждый месяц.
    После достижения предельного возраста кролики умирают.

    :param target_month: месяц, на который нужно рассчитать количество пар кроликов.
    :param rabbit_lifetime: продолжительность жизни каждого кролика, не менее 2 месяцев.
    :return: количество пар кроликов
    """
    if target_month <= 2:
        return 1

    rabbits_age = Deque(rabbit_lifetime)
    rabbits_age.head.value = 1
    rabbits_age.head.next.value = 1

    for _ in range(2, target_month):
        last_removed = rabbits_age.pop()
        new_rabbits = rabbits_age.get(0) + rabbits_age.get(1) - last_removed
        rabbits_age.appendleft(new_rabbits)

    return rabbits_age.get(0)


def main():
    n = 35
    lifetime = 5
    print(f"\nВычисление числа пар кроликов по состоянию на {n} месяц")
    print(f"при продолжительности жизни кролика {lifetime} месяцев")
    print("количество пар кроликов составит:", rabbits(n, lifetime))


if __name__ == "__main__":
    main()