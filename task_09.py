def connect_dicts(dict1, dict2):
    sum_dict1 = sum(dict1.values())
    sum_dict2 = sum(dict2.values())
    primary_dict = dict2 if sum_dict1 <= sum_dict2 else dict1
    secondary_dict = dict1 if sum_dict1 <= sum_dict2 else dict2
    primary_dict = {key: value for key, value in primary_dict.items() if value >= 10}
    secondary_dict = {key: value for key, value in secondary_dict.items() if value >= 10}
    combined_dict = {**secondary_dict, **primary_dict}
    return dict(sorted(combined_dict.items(), key=lambda item: item[1]))


print(connect_dicts({"a": 2, "b": 12}, {"c": 11, "e": 5}))  # => { "c": 11, "b": 12 }
print(connect_dicts({"a": 13, "b": 9, "d": 11}, {"c": 12, "a": 15}))  # => { "d": 11, "c": 12, "a": 15 }
print(connect_dicts({"a": 14, "b": 12}, {"c": 11, "a": 15}))  # => { "c": 11, "b": 12, "a": 15 }
