name = input("Digite o seu nome: ")


for index in range(len(name)):
    print(name.upper())
    name = name[:-1]
