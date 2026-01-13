import threading, time

def eating_breakfast():
    time.sleep(4)
    print("I'm done eating breakfast")

def drinking_tea():
    time.sleep(3)
    print("I'm done drinking coffee.")

def Watching_ytbe_video():
    time.sleep(7)
    print("I'm done watching ytbe Videos.")


start = time.time()
th1 = threading.Thread(target=eating_breakfast, args=())
th1.start()
th2= threading.Thread(target=drinking_tea,args=())
th2.start()
th3= threading.Thread(target=drinking_tea,args=())
th3.start()

th1.join()
th2.join()
th3.join()
print(time.time()-start)


# Watching_ytbe_video()
# eating_breakfast()
# drinking_tea()

# We can count the number of threads that are currently running in the background
print(threading.active_count())
print(threading.active_count.__doc__)
print(threading.enumerate())
print(time.perf_counter())