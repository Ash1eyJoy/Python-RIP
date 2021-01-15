from comand.command import Invoker, Order, Receiver, Cooking

if __name__ == "__main__":
    invoker = Invoker()
    order = ["Макароны по-флотски", "Стейк средней прожарки", "Клубничный молочный коктейль",
             "Латте на миндальном с маршмеллоу"]
    invoker.set_on_start(Order(order))
    receiver = Receiver()
    invoker.set_on_finish(Cooking(receiver, order))

    invoker.do_something_important()
