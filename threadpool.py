from queue import Queue


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class ThreadPool(metaclass=Singleton):
    def __init__(self):
        self.pool = Queue()


def worker():
    while True:
        task = ThreadPool().pool.get()
        task.start()
        task.join()
        ThreadPool().pool.task_done()


if __name__ == "__main__":

    pass
