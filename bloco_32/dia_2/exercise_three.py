import random
import sys

try:
    with open("words.txt", "r") as file:
        words = file.read().split("\n")

    word = random.choice(words)
    scrambled_word = "".join(random.sample(word, len(word)))

    print(f"Palavra embaralhada: {scrambled_word}")

    responses = []

    responses.append(input("Chute 01: "))
    responses.append(input("Chute 02: "))
    responses.append(input("Chute 03: "))

    winner = False

    for response in responses:
        if response == word:
            winner = True

    print(f"Palavra sorteada: {word}")

    if winner:
        print("Você acertou!")
    else:
        print("Você não acertou!")
except OSError:
    err = "Arquivo não encontrado"
    print(f"Erro aconteceu: {err}", file=sys.stderr)
