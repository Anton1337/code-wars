def solution(number):
    return sum([v for v in range(1, number) if v % 3 == 0 or v % 5 == 0])
