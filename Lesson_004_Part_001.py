list_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

list_2 = []
list_3 = []
list_else = []

while list_numbers:
    number = list_numbers.pop()

    if number % 2 == 0 and number != 0:
        list_2.append(number)
    elif number % 3 == 0 and number != 0:
        list_3.append(number)
    else:
        list_else.append(number)

print(list_2)
print(list_3)
print(list_else)

# 1. Дан список чисел. Необходимо вывести в отдельные списки (три списка пустых) такие числа:
# в первый добавляем все числа которые делятся на 2
# во второй - те которые делятся на три
# в третий - те которые не подходят под первые два условия