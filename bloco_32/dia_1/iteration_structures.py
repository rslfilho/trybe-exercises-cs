# Exercício 13
factorial = 1
n = 5
counter = 1

while counter <= n:
    factorial *= counter
    counter += 1

print(factorial)

# Exercício 14

ratings = [6, 8, 5, 9, 10]

updated_ratings = [10 * rate for rate in ratings]

print(updated_ratings)

# Exercício 15

for rate in updated_ratings:
    if rate % 3 == 0:
        print(f"{rate} é múltiplo de 3")
