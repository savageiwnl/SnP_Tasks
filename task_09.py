def connect_dicts(dict1, dict2):
    # Определение приоритетного словаря на основе суммы значений
    sum_dict1 = sum(value for value in dict1.values() if value >= 10)
    sum_dict2 = sum(value for value in dict2.values() if value >= 10)
    priority_dict = dict2 if sum_dict1 <= sum_dict2 else dict1

    # Объединение словарей, исключая ключи со значениями меньше 10
    combined_dict = {**{k: v for k, v in dict1.items() if v >= 10}, **{k: v for k, v in dict2.items() if v >= 10}}

    # Перезапись значения ключа из приоритетного словаря
    combined_dict.update({k: v for k, v in priority_dict.items() if v >= 10})

    # Сортировка словаря по значениям ключей
    sorted_dict = dict(sorted(combined_dict.items(), key=lambda item: item[1]))

    return sorted_dict


print(connect_dicts({"a": 2, "b": 12}, {"c": 11, "e": 5}))
print(connect_dicts({"a": 13, "b": 9, "d": 11}, {"c": 12, "a": 15}))
print(connect_dicts({"a": 14, "b": 12}, {"c": 11, "a": 15}))