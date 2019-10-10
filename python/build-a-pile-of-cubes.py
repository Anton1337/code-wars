def find_nb(m):
    mass = 0
    ix = 1
    while (mass < m):
        mass += ix ** 3
        if(m == mass):
            return ix
        ix += 1
    return -1
