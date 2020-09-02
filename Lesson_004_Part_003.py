list_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

number = 1

while list_number:
    number_i = list_number.pop()
    number = number * number_i

print(number)

# 3. Дан список. Найти произведение (перемножить) всех элементов списка.