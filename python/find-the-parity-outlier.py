def find_outlier(integers):
    odd_counter = 0
    even_counter = 0
    for v in integers[:3]:
        if (v % 2 == 0):
            even_counter += 1
        else:
            odd_counter += 1

    if(even_counter > odd_counter):
        # Loop to find and return odd number.
        for i in integers:
            if (i % 2 == 1):
                return i

    else:
        # Loop to find and return even number
        for i in integers:
            if (i % 2 == 0):
                return i
