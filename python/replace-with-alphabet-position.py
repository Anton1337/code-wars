def alphabet_position(text):
    result_string = ""
    upper_a = 65
    lower_a = 97

    for i, char in enumerate(text):
        if(char.isalpha()):
            if(char.isupper()):
                result_string += str(ord(char) - upper_a + 1)
                if(i != len(text) - 1):
                    result_string += " "
            else:
                result_string += str(ord(char) - lower_a + 1)
                if(i != len(text) - 1):
                    result_string += " "
    return result_string
