#1. Напишите функцию (F): на вход список имен и целое число N; на выходе список длины N случайных имен из первого списка
# (могут повторяться, можно взять значения: количество имен 20, N = 100, рекомендуется использовать функцию random);

import random

def random_list_of_the_names(a,N):
    '''
    :param a: первоначальный список имен
    :param N: количество имен
    :return: новый список из случайных имен
    '''
    new_list = []
    for i in range(N):
        new_list.append(random.choice(a))
    return new_list


a = ['Вася','Петя','Аня', 'Катя', 'Саша', 'Оля', 'Дима', 'Костя', 'Алла', 'Лена', 'Ксюша', 'Паша', 'Артем', 'Андрей',
'Сергей', 'Инна', 'Ашот', 'Миша', 'Стас', 'Лев']

print(random_list_of_the_names(a,20))



#2. Напишите функцию вывода самого частого имени из списка на выходе функции F;
from collections import Counter
def the_most_common_name(a,N):
    '''

    :param a: начальный список имен
    :param N: количество имен в списке
    :return: самое частое имя в списке
    '''
    new_list = []
    for i in range(N):
        new_list.append(random.choice(a))

    return new_list, Counter(new_list).most_common(1)


print(the_most_common_name(a,20))



# 3 Напишите функцию вывода самой редкой буквы, с которого начинаются имена в списке на выходе функции F


def the_rarest_letter(a, N):
    '''

    :param a: начальный список имен
    :param N: количество имен в списке
    :return: самая редкая буква
    '''
    new_list = []
    for i in range(N):
        new_list.append(random.choice(a))

    the_first_letter = list(map(lambda names:names[0],new_list))
    return new_list, Counter(the_first_letter).most_common()[-1]

print(the_rarest_letter(a, 15))



