from operator import itemgetter


class Comp:
    """Компьютер"""

    def __init__(self, id, name, cost, disp_id):
        self.id = id
        self.name = name
        self.cost = cost
        self.disp_id = disp_id


class Disp:
    """Дисплейный класс"""

    def __init__(self, id, name):
        self.id = id
        self.name = name


class CompDisp:
    """
    'Компьютеры дисплейного класса' для реализации
    связи многие-ко-многим
    """

    def __init__(self, dep_id, emp_id):
        self.dep_id = dep_id
        self.emp_id = emp_id


# Компьютер
displays = [
    Disp(1, 'FULL HD 60Gz'),
    Disp(2, '4K 60Gz'),
    Disp(3, 'FullHD 120Gz'),

    Disp(11, ' (другой) FULL HD 60Gz'),
    Disp(22, '4K 60Gz (другой)'),
    Disp(33, '(другая) FullHD 120Gz'),
]

# Дисплейный класс
dispmodel = [
    Comp(1, 'LG', 25000, 1),
    Comp(2, 'Sony', 35000, 2),
    Comp(3, 'Apple PRO Display XDR', 45000, 3),
    Comp(4, 'AOC', 35000, 3),
    Comp(5, 'MSI', 25000, 3),
]

comp_disp = [
    CompDisp(1, 1),
    CompDisp(2, 2),
    CompDisp(3, 3),
    CompDisp(3, 4),
    CompDisp(3, 5),

    CompDisp(11, 1),
    CompDisp(22, 2),
    CompDisp(33, 3),
    CompDisp(33, 4),
    CompDisp(33, 5),
]


def main():
    """Основная функция"""

    # Соединение данных один-ко-многим
    one_to_many = [(e.name, e.cost, d.name)
                   for d in displays
                   for e in dispmodel
                   if e.disp_id == d.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(d.name, ed.dep_id, ed.emp_id)
                         for d in displays
                         for ed in comp_disp
                         if d.id == ed.dep_id]

    many_to_many = [(e.name, e.cost, dep_name)
                    for dep_name, dep_id, emp_id in many_to_many_temp
                    for e in dispmodel if e.id == emp_id]

    print('Задание А1')
    res_11 = sorted(one_to_many, key=itemgetter(2))
    print(res_11)

    print('\nЗадание А2')
    res_12_unsorted = []
    for d in displays:

        d_emps = list(filter(lambda i: i[2] == d.name, one_to_many))

        if len(d_emps) > 0:

            d_sals = [cost for _, cost, _ in d_emps]

            d_sals_sum = sum(d_sals)
            res_12_unsorted.append((d.name, d_sals_sum))

    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)

    print('\nЗадание А3')
    res_13 = {}

    for d in displays:
        if '60Gz' in d.name:

            d_emps = list(filter(lambda i: i[2] == d.name, many_to_many))
            d_emps_names = [x for x, _, _ in d_emps]
            res_13[d.name] = d_emps_names

    print(res_13)


if __name__ == '__main__':
    main()

