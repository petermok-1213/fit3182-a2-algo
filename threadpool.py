from queue import Queue
from threading import Thread, current_thread
from copy import deepcopy

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class ThreadPool(metaclass=Singleton):
    def __init__(self):
        self.pool = Queue()
        workers = [Thread(target=init_worker(str(i)), daemon=True) for i in range(n)]

def init_worker(name: str):
    while True:
        task = ThreadPool().pool.get()
        if task is None:
            break
        task.start()
        print(current_thread().name + name + " finished " + str(task.native_id))
        task.join()
        ThreadPool().pool.task_done()

def create_worker_threads(n: int):

    for worker in ThreadPool().workers:
        worker.start()

