def max_odd(array: list):
    result = [x for x in array if isinstance(x, (int, float)) and x % 2 != 0]
    print(result)
    if len(result) > 0:
        return int(max(result))
    else:
        return None


arr = ['ololo', 2, 3, 5, 21, [1, 2], None]
res = max_odd(arr)
print(res)
