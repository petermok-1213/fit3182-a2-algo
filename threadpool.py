import time
from queue import Queue, Empty
from threading import Thread, current_thread


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class ThreadPool(metaclass=Singleton):
    def __init__(self, n: int):
        self.pool = Queue()
        self.max_worker = n
        self.workers = []

    def worker(self):
        while not self.pool.empty():
            print(current_thread().name + " Running")
            try:
                task = self.pool.get(block=False)
            except Empty:
                print("Empty Queue")
            else:
                print(current_thread().name + " started " + task.name)
                task.start()
                task.join()
                self.pool.task_done()
                print(current_thread().name + " finished " + task.name)

    def start_worker(self):
        print("Starting Workers")
        for _ in range(self.max_worker):
            worker = Thread(target=self.worker(), daemon=True)
            self.workers.append(worker)
        for worker in self.workers:
            worker.start()



    def stop_worker(self):
        print("Stopping Workers")
        for worker in self.workers:
            worker.join()


if __name__ == "__main__":

    pass
