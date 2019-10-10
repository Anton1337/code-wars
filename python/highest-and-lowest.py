def high_and_low(numbers):
    int_numbers = []
    numbers_list = numbers.split()

    for n in numbers_list:
        int_numbers.append(int(n))

    int_numbers.sort()

    highest = int_numbers[len(int_numbers) - 1]
    lowest = int_numbers[0]

    result_string = str(highest) + " " + str(lowest)
    return result_string
