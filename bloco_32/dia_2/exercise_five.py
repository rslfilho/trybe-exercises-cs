import json
import random


with open("pokemons.json", mode="r") as file:
    pokemons = json.load(file)["results"]

pokemon_name = random.choice(pokemons)["name"]

print("Um pokemon aleatório foi escolhido! \n")

response = ""
errors = 0

while response != pokemon_name and errors != len(pokemon_name):
    print(pokemon_name[0:errors])
    errors += 1
    response = input("Quem é esse pokemon? ")

if response == pokemon_name:
    print("Você acertou, muito bem!!\n")
    print(f"O pokemon escolhido era {pokemon_name}")
else:
    print("Você não acertou, tente novamente!!\n")
    print(f"O pokemon escolhido era {pokemon_name}")
