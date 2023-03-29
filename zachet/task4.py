# Task: Дано: массив из 10**6 целых чисел, каждое из которых лежит на отрезке [13, 25].
# Задача: отсортировать массив наиболее эффективным способом

# 1.7084000000000543e-05 sec
def sort(massive):
    """
    :param massive:
    :return:massive
    """
    if len(massive) <= 1:
        return massive
    # Если длина массива меньше или равна 1, то мы выводим сам массив, так как там либо один элемент или пусто.
    # (Что нам как раз и подходит)
    else:
        element_ = massive[0]  # Выбираем элемент, который будем сравнивать со всеми остальными элементами.
        less_el = [x for x in massive[1:] if
                   x < element_]  # Создаем список с элементами которые меньше element_, двигаемся от 2-го элемента
        greater_el = [x for x in massive[1:] if
                      x >= element_]  # Создаем список с элементами которые больше element_, двигаемся от 2-го элемента
        return sort(less_el) + [element_] + sort(
            greater_el)
    # Используем рекурсию для созданя финального списка с осортированными элементами; Складываем три
    # списка с меньшеми значениями,большими значениями и со сравнивемым значением.


print(sort([13, 15, 17, 12]))
