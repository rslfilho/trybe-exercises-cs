scores = {}


def employee_score(subordinateds, employee):
    if employee in scores:
        return scores[employee]

    if len(subordinateds[employee]) == 0:
        scores[employee] = 1
        return 1
    else:
        subordinateds_score = 0
        for sub in subordinateds[employee]:
            subordinateds_score += employee_score(subordinateds, sub)

        scores[employee] = 1 + subordinateds_score
        return 1 + subordinateds_score


subordinates = {
    1: [2, 3],
    2: [4],
    3: [],
    4: [5, 6],
    5: [7],
    6: [],
    7: [],
}

print(employee_score(subordinates, 1))
print(employee_score(subordinates, 2))
print(employee_score(subordinates, 3))
print(employee_score(subordinates, 4))
print(employee_score(subordinates, 5))
print(employee_score(subordinates, 6))
print(employee_score(subordinates, 7))

print(scores)


def add_subordinated(employee, k):
    if len(subordinates[employee]) >= k:
        add_subordinated(employee + 1, k)
    else:
        subordinates[employee].append(len(subordinates) + 1)
        scores[employee] += 1


add_subordinated(4, 2)
print(subordinates)
print(scores)
