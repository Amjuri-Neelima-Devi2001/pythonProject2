import threading
import time
def demo1(n):
    for i in range(n):
        time.sleep(2)
        print(i,end='\t')
def demo2(n):
    for i in range(n):
        time.sleep(2)
        print(i, end='\t')
t1=threading.Thread(target=demo1,args=([10]))
t2=threading.Thread(target=demo2,args=([10]))
t1.start()
t1.join()
t2.start()


