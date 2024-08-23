grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades1 = []
i = 0
while i < len(grades):
    grades1.append(sum(grades[i])/len(grades[i]))
    i += 1
list_ = sorted(list(students))
res = dict(zip(list_, grades1))
print(res)
