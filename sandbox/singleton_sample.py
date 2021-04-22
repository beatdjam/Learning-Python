import threading


class Singleton:
    __singleton = None
    __lock = threading.Lock()

    def __new__(cls):
        with cls.__lock:
            if cls.__singleton is None:
                cls.__singleton = object.__new__(cls)
        return cls.__singleton


if __name__ == '__main__':
    val1: Singleton = Singleton()
    print(val1)
    val2 = Singleton()
    print(val2)
    print(val1 is val2)
