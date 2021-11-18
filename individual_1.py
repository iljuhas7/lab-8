#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Задание 1
# 3. Известны оценки по геометрии каждого из 24 учеников класса. В начале списка перечислены все пятерки,
# затем все остальные оценки. Сколько учеников имеют по геометрии 5 ? Условный оператор не использовать.

import random


if __name__ == '__main__':
    i = 24
    grade = []

    for i in range(0, i):
        grade.append(random.randint(2, 5))

    print(f"Массив оценок: {grade}")

    count = 0
    for i in grade:
        count += grade[i] / 5;

    print(f"Из них пятёрок: {count:0.1f}")
