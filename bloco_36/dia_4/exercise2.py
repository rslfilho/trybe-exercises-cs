str = "serdevemuitolegalmasehprecisoestudarbastante"


def biggest_non_duplicated_substring(string):
    result = 0

    for index, char in enumerate(string):
        char_useds = set()
        char_useds.add(char)
        for char2 in string[index + 1:]:
            if char2 not in char_useds:
                char_useds.add(char2)
            else:
                if len(char_useds) > result:
                    result = len(char_useds)
                break

    return result


print(biggest_non_duplicated_substring(str))
