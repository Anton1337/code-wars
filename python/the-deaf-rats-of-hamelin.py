def count_deaf_rats(town_square):
    # Print town square.
    for stri in town_square:
        print(stri)

    p_pos = (0, 0)
    dead_rat_count = 0

    # Find P position.
    for y, stri in enumerate(town_square):
        for x, char in enumerate(stri):
            if char is 'P':
                p_pos = (x, y)
    print(p_pos)

    # Count dead rats loop
    for y, stri in enumerate(town_square):
        for x, char in enumerate(stri):

            # Up arrow case.
            if(char == '↑' and (above(y, p_pos[1]) or equal(y, p_pos[1]))):
                dead_rat_count += 1

            # Down arrow case.
            if(char == '↓' and (below(y, p_pos[1]) or equal(y, p_pos[1]))):
                dead_rat_count += 1

            # Right arrow case.
            if(char == '→' and (right_of(x, p_pos[0]) or equal(x, p_pos[0]))):
                dead_rat_count += 1

            # Left arrow case.
            if(char == '←' and (left_of(x, p_pos[0]) or equal(x, p_pos[0]))):
                dead_rat_count += 1

            x_diff = x - p_pos[0]
            y_diff = y - p_pos[1]

            y_new = y - x_diff
            y_new2 = y + x_diff

            # Up-Right arrow case.
            if(char == '↗' and (above(y_new, p_pos[1]) or equal(y_new, p_pos[1]))):
                dead_rat_count += 1

            # Up-Left arrow case.
            if(char == '↖' and (above(y_new2, p_pos[1]) or equal(y_new2, p_pos[1]))):
                dead_rat_count += 1

            # Down-Right arrow case.
            if(char == '↘' and (below(y_new2, p_pos[1]) or equal(y_new2, p_pos[1]))):
                dead_rat_count += 1

            # Down-Left arrow case.
            if(char == '↙' and (below(y_new, p_pos[1]) or equal(y_new, p_pos[1]))):
                dead_rat_count += 1

    return dead_rat_count

    # Helpers


def left_of(a, b):
    return a < b


def right_of(a, b):
    return a > b


def above(a, b):
    return a < b


def below(a, b):
    return a > b


def equal(a, b):
    return a is b
