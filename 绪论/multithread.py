import threading
import time
from queue import Queue
def job(l,q):
    for i in range(len(l)):
        l[i]=l[i]**10+l[i]**7
    q.put(l)
def multithreading():
    q=Queue()
    threads=[]
    data=[[1,2,3],[3,4,5],[4,4,4],[5,5,5],[102,309,404]]
    for i in range(5):
        t=threading.Thread(target=job,args=(data[i],q))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
    results=[]
    for _ in range(4):
        results.append(q.get())
    print(results)
def normal():
    data=[[1,2,3],[3,4,5],[4,4,4],[5,5,5],[102,309,404]]
    for _ in range(5):
        for i in range(3):
            data[_][i]=data[_][i]**10+data[_][i]**7
    print(data)
st=time.time()    
multithreading()
st1=time.time()
print('multithreading time:',st1-st)
normal()
st2=time.time()
print('normal time:',st2-st1)
