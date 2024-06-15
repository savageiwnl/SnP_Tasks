def coincidence(List, Range):
    if not List or not Range:
        return []
    start, end = Range
    result = [x for x in List if isinstance(x, (int, float)) and start <= x < end]
    result.sort()
    return result

lst = [None, 1, 'foo', 4, 2, 2.5]
rng = (1, 3)
res = coincidence(lst, rng)
print(res)