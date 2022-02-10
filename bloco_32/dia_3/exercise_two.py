def word_to_phone_number(word):
    result = ''
    if not 1 < len(word) <= 30:
        raise ValueError("Invalid parameter")

    for letter in word:
        if letter in "ABC":
            result += '2'
        elif letter in "DEF":
            result += '3'
        elif letter in "GHI":
            result += '4'
        elif letter in "JKL":
            result += '5'
        elif letter in "MNO":
            result += '6'
        elif letter in "PQRS":
            result += '7'
        elif letter in "TUV":
            result += '8'
        elif letter in "WXYZ":
            result += '9'
        elif letter in "-01":
            result += letter
        else:
            raise ValueError("Invalid letter")

    return result
