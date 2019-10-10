def expanded_form(num):
    numstring = str(num)
    result_string = ""

    first = True
    for i, v in enumerate(numstring):
        if(v != '0'):
            if(not first):
                result_string += " + "
            if(first):
                first = False

            result_string += v
            result_string += '0' * (len(numstring) - (i + 1))
    return result_string
