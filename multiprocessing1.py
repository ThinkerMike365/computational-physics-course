import multiprocessing as mp
import threading as td
import time
def job(q):
    res=0    
    for i in range(5000000):
        res+=i**3+i**2+i**4
    q.put(res)
def job_for_multicorepool(a):
    res=0    
    for i in range(5000000):
        res+=i**3+i**2+i**4
    return res
def multicore():
    q=mp.Queue()
    p1=mp.Process(target=job,args=(q,))
    p2=mp.Process(target=job,args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1=q.get()
    res2=q.get()
    print('multicore:',res1+res2)
def normal():
    res=0
    for _ in range(2):
        for i in range(5000000):
            res+=i**3+i**2+i**4
    print('normal:',res)
def multithread():
    q=mp.Queue()
    t1=td.Thread(target=job,args=(q,))
    t2=td.Thread(target=job,args=(q,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    res1=q.get()
    res2=q.get()
    print('thread:',res1+res2)
def multicorepool():
    a=0
    pool=mp.Pool()
    res=pool.map(job_for_multicorepool,range(2))
    print('multicorepool:',res[0]+res[1])
def multicorepool2():
    a=0
    pool=mp.Pool()
    res1=pool.apply_async(job_for_multicorepool,(a,))
    res2=pool.apply_async(job_for_multicorepool,(a,))
    print('multiprocessingpool2:',res1.get()+res2.get())
    
    
if __name__=='__main__':
    time.sleep(5)
    st=time.time()
    normal()
    st1=time.time()
    print('normal time:',st1-st)
    time.sleep(5)
    multithread()
    st2=time.time()
    print('multithread time',st2-st1-5)
    time.sleep(5)
    multicore()
    st3=time.time()
    print('multicore time',st3-st2-5)
    time.sleep(5)
    multicorepool()
    st4=time.time()
    print('multicorepool time:',st4-st3-5)
    time.sleep(5)
    multicorepool2()
    st5=time.time()
    print('multiprocessingpool2 time:',st5-st4-5)