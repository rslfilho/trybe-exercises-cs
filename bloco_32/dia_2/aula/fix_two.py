import sys


values_str = input("Digite vários números naturais (separe por espaço): ")
values_list = values_str.split(' ')


sum = 0


for value in values_list:
    if not value.isdigit():
        print(
          f"Erro ao somar valores,{value} é um valor inválido",
          file=sys.stderr
        )
    sum += int(value)


print(f"A soma dos valores digitados é: {sum}")
