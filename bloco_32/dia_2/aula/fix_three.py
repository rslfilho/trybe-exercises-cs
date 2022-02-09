ratings = ["Marcos 10", "Felipe 4", "José 6", "Ana 10", "Maria 9", "Miguel 5"]


with open("file_1.txt", mode="w") as file:
    for rate in ratings:
        print(rate, file=file)


try:
    file = open("file_1.txt", mode="r")
    new_file = open("file_2.txt", mode="w")
except OSError:
    print("arquivo inexistente")
else:
    for line in file:
        splitted_line = line.split(' ')
        if int(splitted_line[1]) < 6:
            new_file.write(f"{splitted_line[0]}\n")
    file.close()
    new_file.close()
finally:
    print("Tentativa concluída")
