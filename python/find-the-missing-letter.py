def find_missing_letter(chars):
    index = -1
    for c in chars:
        int_value = ord(c)  # a = 97
        if(index is -1):
            index = int_value
        elif(int_value is not index + 1):
            return chr(int_value - 1)
        else:
            index = int_value
