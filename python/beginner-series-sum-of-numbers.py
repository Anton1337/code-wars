def get_sum(a, b):
    start = min(a, b)
    end = max(a, b)

    sum = 0
    for v in range(start, end + 1):
        sum += v
    return sum
