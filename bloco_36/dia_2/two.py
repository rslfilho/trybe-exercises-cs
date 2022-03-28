def shuffle_cards(cards):
    half_cards = int(len(cards) / 2)
    result = []

    for index in range(0, half_cards):
        result.append(cards[index])
        result.append(cards[index + half_cards])

    return result


print(shuffle_cards([1, 4, 4, 7, 6, 6]))
