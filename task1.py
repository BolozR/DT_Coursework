from Bellman_alg import *


def task(disp=False):
    print("Задание 1:")
    estimate = 90
    #gi - остаток средств i цеха
    g1 = 0.83
    g2 = 0.64
    g_max = round((g1 ** 3 * estimate), 2)
    g_min = round((g2 ** 3 * estimate), 2)
    g_step4 = round((g_max - g_min) / 5, 3)
    #xi - средства распределяемые на i шаге
    x4 = g_min / 10
    print("Шаг 4:")
    step4_cl = Bellman_Alg(g_step4, x4, 4, disp=disp)
    step4_res = step4_cl.step()
    print()
    g_max = round((g1 ** 2 * estimate), 2)
    g_min = round((g2 ** 2 * estimate), 2)
    g_step3 = round((g_max - g_min) / 5, 3)
    x3 = g_min / 10
    print("Шаг 3:")
    step3_cl = Bellman_Alg(g_step3, x3, 3, step4_cl.max, disp)
    step3_res = step3_cl.step()
    print()
    g_max = round((g1 * estimate), 2)
    g_min = round((g2 * estimate), 2)
    g_step2 = round((g_max - g_min) / 5, 3)
    x2 = g_min / 10
    print("Шаг 2:")
    step2_cl = Bellman_Alg(g_step2, x2, 2, step3_cl.max, disp)
    step2_res = step2_cl.step()
    print("Шаг 1:")
    step1_cl = Bellman_Alg(estimate, 9, 1, step2_cl.max, disp)
    step1_res = step1_cl.last_step(estimate)
    remainder = lambda workshop1, workshop2: 0.83 * workshop1 + 0.64 * workshop2
    #расчёт оптимального распределения средств для каждого шага:
    rem1 = round(remainder(step1_cl.max_x, estimate - step1_cl.max_x), 2)
    rem2 = round(remainder(step2_cl.max_x, rem1 - step2_cl.max_x), 2)
    rem3 = round(remainder(step3_cl.max_x, rem2 - step3_cl.max_x), 2)
    result_table = PrettyTable()
    result_table.field_names = ["Цех", "1 квартал", "2 квартал", "3 квартал", "4 квартал"]
    result_table.add_row(["1", str(step1_cl.max_x), str(step2_cl.max_x),
                          str(step3_cl.max_x), str(step4_cl.max_x)])
    result_table.add_row(["2", str(estimate - step1_cl.max_x), str(rem1 - step2_cl.max_x),
                          str(rem2 - step3_cl.max_x), str(rem3 - step4_cl.max_x)])
    print("Ответ:")
    print(result_table)
