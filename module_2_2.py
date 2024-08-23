first = int(input('Input integer (1/3): '))
second = int(input('Input integer (2/3): '))
third = int(input('Input integer (3/3): '))
if first == second and second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)
