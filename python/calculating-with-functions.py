def zero(op=-1):
    if(op is -1):
        return 0
    else:
        return num_op(0, op)


def one(op=-1):
    if(op is -1):
        return 1
    else:
        return num_op(1, op)


def two(op=-1):
    if(op is -1):
        return 2
    else:
        return num_op(2, op)


def three(op=-1):
    if(op is -1):
        return 3
    else:
        return num_op(3, op)


def four(op=-1):
    if(op is -1):
        return 4
    else:
        return num_op(4, op)


def five(op=-1):
    if(op is -1):
        return 5
    else:
        return num_op(5, op)


def six(op=-1):
    if(op is -1):
        return 6
    else:
        return num_op(6, op)


def seven(op=-1):
    if(op is -1):
        return 7
    else:
        return num_op(7, op)


def eight(op=-1):
    if(op is -1):
        return 8
    else:
        return num_op(8, op)


def nine(op=-1):
    if(op is -1):
        return 9
    else:
        return num_op(9, op)


def num_op(first_num, op_tuple):
    second_num = op_tuple[0]
    op = op_tuple[1]

    if(op is '+'):
        # plus
        return first_num + second_num
    elif(op is '-'):
        # minus
        return first_num - second_num
    elif(op is '/'):
        # divide
        return int(first_num / second_num)
    else:
        # multiply
        return first_num * second_num


def plus(num):
    return (num, '+')


def minus(num):
    return (num, '-')


def times(num):
    return (num, '*')


def divided_by(num):
    return (num, '/')
