data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(*data_structure):
    result = 0
    for i in data_structure:
        if isinstance(i, (float, int)):
            result = result + i
        elif isinstance(i, str):
            result = result + len(i)
        elif isinstance(i, (list, tuple, set)):
            result = result + calculate_structure_sum(*i)
        elif isinstance(i, dict):
            result = result + calculate_structure_sum(*i.items())
    return result


print(calculate_structure_sum(data_structure))
