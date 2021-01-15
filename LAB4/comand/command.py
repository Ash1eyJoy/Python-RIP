from __future__ import annotations
from abc import ABC, abstractmethod


class Command(ABC):
    """
    Интерфейс Команды объявляет метод для выполнения команд.
    """

    @abstractmethod
    def execute(self) -> None:
        pass


class Order(Command):
    def __init__(self, payload: list) -> None:
        self.orders = payload

    def execute(self) -> None:
        print(f"Ваш заказ: "
              f"({self.orders})")

    def return_guest_order(self):
        return self.orders


class Cooking(Command):
    def __init__(self, receiver: Receiver, l: list) -> None:
        self._receiver = receiver
        self._list_of_orders = l

    def execute(self) -> None:
        for o in self._list_of_orders:
            self._receiver.start_cook(o)
        for o in self._list_of_orders:
            self._receiver.ready(o)


class Receiver:
    def start_cook(self, a: str) -> None:
        print(f"Ваш {a} начали готовить.\n", end="")

    def ready(self, b: str) -> None:
        print(f"Ваш {b} готово.\n", end="")


class Invoker:
    _on_start = None
    _on_finish = None

    def set_on_start(self, command: Command):
        self._on_start = command

    def set_on_finish(self, command: Command):
        self._on_finish = command

    def do_something_important(self) -> None:
        print("Здрваствуйте, желаете сделать заказ?\n")
        if isinstance(self._on_start, Command):
            self._on_start.execute()

            print("Передаю ваш заказ на кухню\n")
            if isinstance(self._on_finish, Command):
                self._on_finish.execute()
        else:
            print("Хорошо, я подойду позже\n")


