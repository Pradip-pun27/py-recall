from multiprocessing import  cpu_count,Process
import time

def counter(num):
    count = 0
    while count<=num:
        count+=1

def main():
    print(cpu_count()) # To check how many cores does my laptop's processor have
    p1= Process(target = counter, args=(250000000,))
    p2= Process(target = counter, args=(250000000,))
    p3= Process(target = counter, args=(250000000,))
    p4= Process(target = counter, args=(250000000,))

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p1.join()
    p2.join()
    p3.join()
    p3.join()



if __name__ =='__main__':
    main()
    print(time.perf_counter())