from singleton.singletonClass import Singleton
import unittest


class TestsSingleton(unittest.TestCase):
    def test_singleton_return_file(self):
        singleton = Singleton()
        sfile = singleton.return_file()

        file = open(singleton.file, 'r')
        expect = file.read()
        file.close()
        self.assertEqual(sfile, expect)

    def test_singleton(self):
        s1 = Singleton()
        s2 = Singleton()
        self.assertEqual(id(s1), id(s2))

    def test_singleton_write_file(self):
        singleton = Singleton()
        line = "Сосисоны"
        singleton.write_file(line)

        file = open(singleton.file, 'r')
        fileText = file.read()
        file.close()

        expect = ""
        for i in range(len(line)):
            expect += fileText[len(fileText) - len(line) + i]
        self.assertEqual(line, expect)

if __name__ == '__main__':
    unittest.main()

