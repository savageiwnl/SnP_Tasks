def coincidence(List=None, Range=None):
    if not List or not Range:
        return []
    result = [x for x in List if isinstance(x, (int, float)) and Range[0] <= x < Range[1]]
    result.sort()
    return result


print(coincidence([1, 2, 3, 4, 5], (3, 6)))