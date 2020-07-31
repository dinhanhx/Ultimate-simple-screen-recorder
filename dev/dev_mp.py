import multiprocess as mp
import time

def foo_one(eve1, eve2):
    print("Foo one is boosting")
    time.sleep(5)
    eve1.set() # Alarm foo_two()
    eve2.wait() # Need to wait foo_two() finishing boosting
    print("Foo one is running")
    return None

def foo_two(eve1, eve2):
    print("Foo two is boosting")
    time.sleep(10)
    eve2.set() # Alarm foo_one()
    eve1.wait() # Need to wait foo_one() finishing boosting
    print("Foo two is running")
    return None

if __name__ == '__main__':
    eve1 = mp.Event()
    eve2 = mp.Event()
    p1 = mp.Process(target = foo_one, args = [eve1, eve2])
    p2 = mp.Process(target = foo_two, args = [eve1, eve2])
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("foo_one and foo_two finish")
