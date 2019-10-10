def order(sentence):
    string_list = sentence.split()

    stored_words = {}

    for str in string_list:
        for c in str:
            if (is_int(c)):
                stored_words[int(c)] = str

    ordered = ""
    for i in range(1, len(string_list) + 1):
        ordered += stored_words[i]
        if (i != (len(string_list))):
            ordered += " "

    return ordered


def is_int(value):
    try:
        int(value)
        return True
    except:
        return False
