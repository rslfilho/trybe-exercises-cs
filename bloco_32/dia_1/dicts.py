info = {
  "personagem": "Margarida",
  "origem": "Pato Donald",
  "nota": "Namorada do personagem principal nos quadrinhos do Pato Donald",
}

# Exercício 08
# print(info.personagem) Gera erro de Atributo, "personagem" is not defined

# Exercício 09

info["recorrente"] = "Sim"

print(info)

# Exercício 10

info.pop("origem")
# ou del info["origem"]

print(info)