words = ['cat', 'bt', 'hat', 'tree']
chars = 'atach'
# saída: 6
"""Explicação: As palavras que podem ser formadas com os caracteres da string
               são "cat" (tamanho 3) e "hat" (tamanho 3)."""


words2 = ['hello', 'world', 'students']
chars2 = 'welldonehoneyr'
# saída: 10
"""Explicação: As palavras que podem ser formadas com os caracteres da string
               são "hello" (tamanho 5) e "world" (tamanho 5)."""


def good_words_length(word_list, characters):
    chars_dict = {}

    for char in characters:
        if char not in chars_dict:
            chars_dict[char] = 1
        else:
            chars_dict[char] += 1

    good_words = []
    for word in word_list:
        char_count = {}
        for char in word:
            if char not in chars_dict:
                break

            if char not in char_count:
                char_count[char] = 1
            else:
                char_count[char] += 1

                if char_count[char] > chars_dict[char]:
                    break
        else:
            good_words.append(word)

    result = 0
    for word in good_words:
        result += len(word)

    return result


print(good_words_length(words, chars))
print(good_words_length(words2, chars2))
