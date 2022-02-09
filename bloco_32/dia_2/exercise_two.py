import random


word = random.choice(["telhado", "parede", "madeira", "cimento"])
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
