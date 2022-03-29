entrada = {
    'Clara': [0, 1, 5, 9, 10],
    'Marco': [0, 2, 8, 9, 10]
}

# saída: 'Marco'


def blefe(input):
    player1, player2 = input.keys()
    values1, values2 = input.values()

    values1_set = set(values1)
    values2_set = set(values2)

    player1_diff = values1_set.difference(values2_set)
    player1_pts = max(player1_diff) - min(player1_diff)

    player2_diff = values2_set.difference(values1_set)
    player2_pts = max(player2_diff) - min(player2_diff)

    if player1_pts > player2_pts:
        return player1
    elif player2_pts > player1_pts:
        return player2

    return 'Empate'


print(blefe(entrada))
