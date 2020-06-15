#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

######################################################################

#第*部分  并发操作

######################################################################


import threading
from time import sleep, ctime

##======1.传入函数，启动线程=========fib
##
def fib(n):
    # sleep(0.005)
    if n < 2:
        return 1
    return (fib(n-2)+fib(n-1))

def loop(nsec):
    print('开始线程,name={}，id={},daemon={},time={}'.format(
                threading.current_thread().name, 
                threading.current_thread().ident, 
                threading.current_thread().daemon, ctime()))
    sleep(nsec)
    print('结束线程：id={}'.format(threading.current_thread().ident))

print('开始==========')
thrdloop = threading.Thread(target = loop, args = (4,))
thrdfib = threading.Thread(target = fib, args = (20,))


thrdloop.start()

print('开始线程,name={}，id={},daemon={}, time={}'.format(
                thrdfib.name, thrdfib.ident, thrdfib.daemon, ctime()))
thrdfib.start()
thrdfib.join()
print('结束线程：id={}'.format(thrdfib.ident))

thrdloop.join()


print('结束==========')

##======2.派生线程类，启动线程=========
##

class MyThread(threading.Thread):
    def __init__(self, nsec):
        threading.Thread.__init__(self) #记得调用基类的初始化
        self.nsec = nsec

    def run(self):
        print('开始线程,name={}，id={},daemon={}, time={}'.format(
                    self.name, self.ident, self.daemon, ctime()))
        sleep(self.nsec)
        print('结束线程：{},time={}'.format(self.ident, ctime()))

print('\n开始==========')
thrdOne = MyThread(4)
thrdTwo = MyThread(2)

thrdOne.start()
thrdTwo.start()

thrdOne.join()
thrdTwo.join()

print('结束==========')


##======3.锁同步=========
##
print('[]'*20)
from random import randrange
from threading import Thread, currentThread, Lock
from time import sleep, ctime

loops = []
for i in range(5):
    loops.append(randrange(2,10))

remaining = set()
lock = Lock()

def loopFun(nsec):
    myName = currentThread().name

    lock.acquire()                  #1)使用锁同步
    remaining.add(myName)
    print('{}开始线程{}'.format(ctime(), myName))
    lock.release()

    sleep(nsec)

    # lock.acquire()
    with lock:                      #2)使用上下文管理锁，即使中间出异常，也能够正常释放锁
        remaining.remove(myName)
        print('{}结束线程{},{}秒'.format(ctime(),myName, nsec))
        print('剩下：{}'.format(remaining or 'None'))
    # lock.release()

for pause in loops:
    thrd = Thread(target=loopFun, args=(pause,))
    thrd.start()
sleep(5)
print('OK')


##======4.信号量同步=========
##
print('=='*20)
from random import randrange
from threading import Thread, currentThread, BoundedSemaphore
from time import sleep, ctime

lock = Lock()
MAX = 5
candyTray = BoundedSemaphore(MAX)

def refill():
    lock.acquire()
    print('放糖')
    try:
        candyTray.release()
    except ValueError:
        print('槽满了')
    else:
        print('OK')
    lock.release()

def buy():
    lock.acquire()
    print('购买')
    if candyTray.acquire(False):
        print('OK')
    else:
        print('空了')
    lock.release()

def producer(loops):
    for i in range(loops):
        refill()
        sleep(randrange(3))

def consumer(loops):
    for i in range(loops):
        buy()
        sleep(randrange(3))

nloops = randrange(2,6)
Thread(target=consumer, args=(randrange(nloops, nloops+MAX+2),)).start()

Thread(target=producer, args=(nloops,)).start()

sleep(10)
print("OK")

##======5.队列同步=========
##

from random import randint
from time import sleep
from queue import Queue
from threading import Thread

def writeQ(queue):
    print('生产元素')
    queue.put('xxx', True)
    print('队列大小={}'.format(queue.qsize()))

def readQ(queue):
    val = queue.get(True)
    print('取出元素“{}”，队列大小={}'.format(val, queue.qsize()))

def writer(q, nloops):
    for i in range(nloops):
        writeQ(q)
        sleep(randint(1,3))

def reader(q, nloops):
    for i in range(nloops):
        readQ(q)
        sleep(randint(2,5))

nloops = randint(2,5)
q = Queue(32)

thrdWt = Thread(target=writer, args=(q, nloops))
thrdRd = Thread(target=reader, args=(q, nloops))

thrdWt.start()
thrdRd.start()

thrdWt.join()
thrdRd.join()
