# МОДУЛИ И ПАКЕТЫ. Задача: "А как делить?"
from math import inf


def divide(first, second):
    if first and second == 0:
        print(inf)
        return inf
    else:
        print(first / second)
