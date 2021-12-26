from threading import Thread
from utils import decript_using_caesar
    
class DecriptThread (Thread):
    def __init__(self, que, id, file_name):
        Thread.__init__(self)
        self.que = que
        self.id = id
        self.file_name = file_name

    def run(self):
        with open(self.file_name) as f:
            x = f.read()
            self.que.put([self.id, decript_using_caesar(x)])