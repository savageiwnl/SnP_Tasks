def coincidence(List=None, Range=None):
    if not List or not Range:
        return []
    start, stop = Range.start, Range.stop
    result = [x for x in List if isinstance(x, (int, float)) and start <= x < stop]
    result.sort()
    return result


print(coincidence())