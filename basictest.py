import time


def num(m):
    
    t1 = time.time()
    print(callable(t1))
    for i in range(0,m):
        
        time.sleep(1.5)
        print(i)

    t2 = time.time()

    print(str(t2-t1))

num(3)