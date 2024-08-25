def get_multiplied_digits(number):
    str_number = str(number).replace('0', '')  # Без удаления "0" код выполняется не корректно при окончании number на 0 (Например: 500)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first


result = get_multiplied_digits(40203)
print(result)
