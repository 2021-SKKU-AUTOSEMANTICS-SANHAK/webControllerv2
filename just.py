import time
from multiprocessing import Process

def foo(i):
    time.sleep(i)
    print("foo" + str(i))





