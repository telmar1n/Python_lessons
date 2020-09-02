string_input = input("input your string")

char_input = input("input your char what you what find")

print(string_input.find(char_input))

if string_input.find(char_input) != -1:
    print("i find your char")
else:
    print(" i can't find this")

# 2. Пользователь вводит строку и символ (одну букву). Проверить есть ли в этой строке введенный символ.