immutable_var = (1, 3, False, "apple", [123, 234])
print(immutable_var)
# immutable_var[0] = 500 - Выдаст ошибку (Неизменяемый элемент кортежа)
# immutable_var[1] = 500 - Выдаст ошибку (Неизменяемый элемент кортежа)
# immutable_var[2] = True - Выдаст ошибку (Неизменяемый элемент кортежа)
# immutable_var[3] = "pineapple" - Выдаст ошибку (Неизменяемый элемент кортежа)
# immutable_var[4] = 500 - Выдаст ошибку (Список внутри кортежа является его элементом и его полностью заменить нельзя)
immutable_var[4][0] = 500 # Замена элемента в списке внутри кортежа)
immutable_var[4][1] = 1000 # Замена элемента в списке внутри кортежа
print(immutable_var)
print()

mutable_list = [1, 3, False, "apple", [123, 234]]
print(mutable_list)
mutable_list[0] = 100
mutable_list[1] = "pineapple"
mutable_list[2] = 300
mutable_list[3] = True
mutable_list[4][0] = 'apple'
mutable_list[4][1] = 5000
print(mutable_list)