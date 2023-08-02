from threading import *


class ThreadedSim:
    def __init__(self, env):
        self.env = env

        t1 = Thread(target=self.work)
        t1.start()

    def work(self):
        print("Hello")
