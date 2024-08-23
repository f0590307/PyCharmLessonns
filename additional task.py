# Задание 1
s = "   казнить     нельзя,    помиловать    "
s1 = s.split()
print(" ".join(s1[::-1]))

# Задание 2
t = [25, 46, 78, 46, 25] # Палиндром
t1 = list(reversed(t))
print(t == t1)

a = [25, 46, 78, 46, 30] # Не палиндром
a1 = list(reversed(t))
print(a == a1)