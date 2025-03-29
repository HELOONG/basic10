import threading

from demo3 import t, t1
from helo.ll import func


def th():
    func()
    from helo.ll import a
    print(a)
    th1 = threading.Thread(target=t)
    th2 = threading.Thread(target=t1)
    th1.start()
    th2.start()


if __name__ == '__main__':
    th()