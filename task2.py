import pulp


def run(S, Cost, disp = True):
    prob = pulp.LpProblem("task2", pulp.LpMaximize)
    x1 = pulp.LpVariable("x1", 0, None, 'Integer')
    x2 = pulp.LpVariable("x2", 0, None, 'Integer')
    x3 = pulp.LpVariable("x3", 0, None, 'Integer')
    x4 = pulp.LpVariable("x4", 0, None, 'Integer')
    x5 = pulp.LpVariable("x5", 0, None, 'Integer')
    # целевая функция:
    prob += 1300 * x1 + 500 * x2 + 2100 * x3 + 2000 * x4 + 900 * x5, "obj"
    # ограничение по площади:
    prob += 27 * x1 + 25 * x2 + 22 * x3 + 17 * x4 + 22 * x5 <= S, "S"
    # ограничение по средствам:
    prob += 32 * x1 + 35 * x2 + 59 * x3 + 58 * x4 + 40 * x5 <= Cost, "P"
    prob.solve()
    notNullCount = 0
    # вывод результатов:
    if disp: print("Оптимальный план: ", end="")
    for v in prob.variables():
        if v.varValue != 0:
            if disp: print(v.name, "=", int(v.varValue), end=" ")
            notNullCount += 1
    if disp: print("\nМаксимальная производительность = ", int(pulp.value(prob.objective)))
    return notNullCount


def task():
    print("Задание 2:")
    print("---------------------------------")
    print("Ответ: ")
    run(180, 374)
    print("---------------------------------")
    print("Исследование 1 (увеличение количества средств до 1000): ")
    run(180, 1000)
    print("---------------------------------")
    print("Исследование 2 (уменьшение количества средств до 100): ")
    run(180, 100)
    print("---------------------------------")
    print("Исследование 3 (увеличение доступной площади до 1000): ")
    run(1000, 374)
    print("---------------------------------")
    print("Исследование 4 (уменьшение доступной площади до 100): ")
    run(100, 374)
    print("---------------------------------")
    print("Выяснить границы изменения количества средств, в пределах которых оптимальным\n"
          "является выбор 2-х и более типов оборудования: ")
    i = 100
    res = run(180, i, disp=False)
    while res < 2:
        i += 1
        res = run(180, i, disp=False)
    print("Нижняя граница:", i)
    i = 250
    res = run(180, i, disp=False)
    while res >= 2:
        i += 1
        res = run(180, i, disp=False)
    print("Верхняя граница:", i)
    print("---------------------------------")