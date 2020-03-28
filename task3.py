import pulp
from prettytable import PrettyTable


def alg(limit, max_or_min, last_val = 0, disp = True):
    if disp: print("###################################################################")
    x1 = pulp.LpVariable("x1", 0, None, 'Integer')
    x2 = pulp.LpVariable("x2", 0, None, 'Integer')
    x3 = pulp.LpVariable("x3", 0, None, 'Integer')
    x4 = pulp.LpVariable("x4", 0, None, 'Integer')
    x5 = pulp.LpVariable("x5", 0, None, 'Integer')
    x6 = pulp.LpVariable("x6", 0, None, 'Integer')
    prob = pulp.LpProblem("task3", pulp.LpMaximize)
    # выбор целевой функции в зависимости от цели задачи максимизации комплектов/минимизации затрат:
    if max_or_min == "max":
        prob += x6, "obj"
    elif max_or_min == "min":
        prob += 20 * x2 + 40 * x3 + 50 * x5, "obj"
    # ограничения задачи:
    prob += x1 + x5 - 2 * x6 == 0, "d1"
    prob += x2 + 2 * x3 - 3 * x6 == 0, "d2"
    prob += 2 * x1 + 3 * x2 + 6 * x4 + x5 - 3 * x6 == 0, "d3"
    prob += x1 + x2 + x3 + x4 + x5 <= limit, "k"
    prob += x6 >= last_val, "min_val"
    prob.solve()
    sum = 0
    arr = []
    result_table = PrettyTable()
    result_table.field_names = ["x1", "x2", "x3", "x4", "x5", "x6"]
    if max_or_min == "max" and disp: print("Максимизация числа комплектов:")
    elif max_or_min == "min" and disp: print("Минимизация остатков:")
    for v in prob.variables():
        arr.append(int(v.varValue))
        sum += v.varValue
    result_table.add_row(arr)
    if disp:
        print(result_table)
        print("Остаток:", int(limit - (sum - v.varValue)))
        print("При ограничении в ", limit, " заготовок можно изготовить ", int(v.varValue), " комплектов.")
    return arr


def task():
    print("Задание 3:")
    limit = 300
    first = alg(limit, "max")
    second = alg(limit, "min", first[-1])
    last = first
    while last[-1] != (first[-1] + 1):
        limit += 1
        last = alg(limit, "max", disp=False)
    print("###################################################################")
    print("Исследование необходимого приращения количества поступивших полуфабрикатов для\n" 
          "увеличения числа комплектов заготовок на 1, 10, 20 и 30:")
    print("Для увеличения на 1:", limit)
    while last[-1] != (first[-1] + 10):
        limit += 1
        last = alg(limit, "max", disp=False)
    print("Для увеличения на 10:", limit)
    while last[-1] != (first[-1] + 20):
        limit += 1
        last = alg(limit, "max", disp=False)
    print("Для увеличения на 20:", limit)
    while last[-1] != (first[-1] + 30):
        limit += 1
        last = alg(limit, "max", disp=False)
    print("Для увеличения на 30:", limit)
