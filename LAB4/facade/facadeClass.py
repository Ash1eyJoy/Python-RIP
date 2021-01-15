from __future__ import annotations


class Facade:

    def __init__(self, numbers: list) -> None:
        self._sum = Sum(numbers)
        self._div = Division()

    def operation(self) -> str:
        results = []

        num = self._sum.operation_plus()
        den = self._sum.return_amount()
        self._div.set_variables(num,den)
        result = self._div.division()

        results.append("Среднее арифметическое чисел: ")
        results.append(self._sum.list_items())
        results.append("Результат: ")
        results.append(str(result))
        return "\n".join(results)


class Sum:
    _list = []

    def __init__(self, numbers: list):
        self._list = numbers

    def operation_plus(self):
        sum = 0
        for i in self._list:
            sum += i
        return sum

    def return_amount(self):
        return len(self._list)

    def list_items(self) -> str:
        return str(self._list)


class Division:

    def __init__(self, num=1.0, den=1.0):
        self._numerator = num
        self._denominator = den

    def division(self):
        return self._numerator / self._denominator

    def set_variables(self,n,d):
        self._numerator = n
        self._denominator = d