def binary_array_to_number(arr):
    answer = 0

    for i, v in enumerate(arr[::-1]):
        if(v):
            answer += 2 ** i
    return answer
