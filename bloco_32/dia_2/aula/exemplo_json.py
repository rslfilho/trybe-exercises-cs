import json  # json é um modulo que vem embutido, porém precisamos importá-lo


with open("pokemons.json", "r") as file:
    pokemons = json.load(file)["results"]
    # acessamos a chave results que é onde contém nossa lista de pokemons

print(pokemons[0])  # imprime o primeiro pokemon da lista
