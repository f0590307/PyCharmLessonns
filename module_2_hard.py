import random
# # Вариант решения с созданием словаря паролей
# passwords = {}
# for i in range(3, 21):
#     list_ = []
#     for j in range(1, i):
#         for k in range(j+1, i):
#             if i % (j + k) == 0:
#                 list_.extend([j, k])
#     list_ = ''.join([str(item) for item in list_])
#     passwords[i] = list_
# w = random.choice(range(3, 21))
# print('Появилось число на первой вставке - ', str(w))
# input('Надмите Enter для подбора кода ')
# print('Шифр на второй вставке - ', passwords.get(w))
#
# # Вариант решения с текущим подбором пароля
# w = random.choice(range(3, 21))
# list_ = []
# for j in range(1, w):
#     for k in range(j + 1, w):
#         if w % (j + k) == 0:
#             list_.extend([j, k])
# list_ = ''.join([str(item) for item in list_])
# print('Появилось число на первой вставке - ', str(w))
# input('Надмите Enter для подбора кода ')
# print('Шифр на второй вставке - ', list_)
#
# # Вариант с созданием функции


def password(m):
    list_1 = []
    for l_ in range(1, m):
        for z in range(l_ + 1, m):
            if m % (l_ + z) == 0:
                list_1.extend([l_, z])
    list_1 = ''.join([str(item) for item in list_1])
    return list_1


m = random.choice(range(3, 21))
print('Появилось число на первой вставке - ', str(m))
input('Надмите Enter для подбора кода ')
print('Шифр на второй вставке - ', password(m))
