import time
from multiprocessing import Process
import os

def foo(i):
    time.sleep(i)
    print("foo" + str(i))


the_path = os.path.dirname(os.path.abspath(__file__))
total_path = os.path.join(the_path, "people_counting/")
print(total_path)





