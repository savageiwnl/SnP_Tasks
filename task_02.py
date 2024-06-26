def coincidence(List, Range):
    if not List or not Range:
        return []
    start, stop = Range.start, Range.stop
    result = [x for x in List if isinstance(x, (int, float)) and start <= x < stop]
    result.sort()
    return result


print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)))