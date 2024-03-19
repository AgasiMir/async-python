# вариант №1
def proper_budget_1(n):
    n = str(n)[::-1]
    res = ""
    for i, j in enumerate(n):
        if not i % 3:
            res += "_" + j
        else:
            res += j

    return res[::-1].strip("_")


# вариант №2
def proper_budget_2(n):
    n = str(n)[::-1]
    res = "".join(
        ["_" + j if not i % 3 else j for i, j in enumerate(n, 1)][::-1]
    ).strip("_")

    return res


# вариант №3
def proper_budget_3(n):
    return f"{n:_}"


budget = 100000000
print(proper_budget_3(budget))
