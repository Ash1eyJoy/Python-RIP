from facade.facadeClass import Facade, Sum, Division
import unittest
import random

class TestsFacade(unittest.TestCase):
    def test_facade_operation(self):
        for i in range(3, 10):
            items = []
            for j in range(20):
                items.append(random.randint(3,20))
            with self.subTest(items=items):
                f = Facade(items)
                result = f.operation()

                sum = Sum(items)
                num = sum.operation_plus()
                den = sum.return_amount()
                div = Division(num, den)
                res = div.division()

                sresult = []
                sresult.append("Среднее арифметическое чисел: ")
                sresult.append(str(items))
                sresult.append("Результат: ")
                sresult.append(str(res))
                expected = "\n".join(sresult)
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()