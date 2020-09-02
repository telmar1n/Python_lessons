list_somethitg = ["hello", 10, 10.5, [1,2,3,4,5,], {"1":5, "2":10}]
dict_result = {}

print(len(list_somethitg))

for i in range(len(list_somethitg)):
    data = list_somethitg.pop()
    name_of_type = type(data)
    print(name_of_type)
    print(data)

    d = {name_of_type:data}
    print(d)
    dict_result.update(d)

print(dict_result)

# 4. Есть список элементов (могут быть строки, словари, числа и другие типы данных).
# Создать словарь в котором будут ключи имена типов данных и в значениях лежать сами значения в списке.
# Пример: [1,"2", {"123":123}, [1,2,3,4]]
# На выходе должно быть: {'list': [[1,2,3,4]], 'dict':[{"123":123}], 'int': [1], 'str': ["2"]}