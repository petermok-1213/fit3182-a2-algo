from threading import Thread
from queue import Queue

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class ThreadPool(metaclass=Singleton):
    def __init__(self, max_thread: int):
        self.pool = Queue(maxsize=max_thread)


if __name__ == "__main__":

    threadpool = ThreadPool(8)
    print(threadpool.pool.maxsize)

    threadpool2 = ThreadPool()
    print(threadpool2.pool.maxsize)

    print(id(threadpool) == id(threadpool2))
