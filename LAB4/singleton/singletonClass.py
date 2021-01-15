class SingletonMeta(type):
    """
    В Python класс Одиночка можно реализовать по-разному. Возможные способы
    включают себя базовый класс, декоратор, метакласс. Мы воспользуемся
    метаклассом, поскольку он лучше всего подходит для этой цели.
    """
    file = "base.txt"

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Данная реализация не учитывает возможное изменение передаваемых
        аргументов в `__init__`.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    file = "file.txt"
    def return_file(cls):
        f = open(cls.file, 'r')
        line = f.read()
        f.close()
        return line

    def write_file(cls, l):
        f = open(cls.file, 'a')
        f.write(l)
        f.close()
