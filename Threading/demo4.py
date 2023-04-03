import threading
class Cal_square(threading.Thread):
    def __init__(self,number):
        threading.Thread.__init__(self)
        self.num=number
    def cal(self):
        for i in range(self.num):
            print(i*i)
    def run(self):
        self.cal()
thread1=Cal_square(1000)
thread1.start()