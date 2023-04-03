import threading

import threading
def mythread():
    print("start thread")
    print("hello")
    print(threading.currentThread().getName())
    print("end")
def mythread1():
    print("start thread")
    print("hello")
    print(threading.currentThread().getName())
    print("end")
t1=threading.Thread(target=mythread)
t2=threading.Thread(target=mythread1)
print(threading.currentThread().getName())
t1.start()
t2.start()