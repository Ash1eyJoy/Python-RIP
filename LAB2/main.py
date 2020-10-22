from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import matplotlib.pyplot as plt


def main():
    r = Rectangle("синего", 4, 4)
    c = Circle("зеленого", 4)
    s = Square("красного", 4)
    print("Ахвердиев Валерий, ИУ5-51Б Вариант 4")
    print(r)
    print(c)
    print(s)
    plt.plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
    plt.show()

if __name__ == "__main__":
    main()