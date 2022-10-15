'''
共享数据：

如果多个线程共同对某个数据修改，则可能出现不可预料的结果，为了保证数据的正确性，需要对多个线程进行同步。
同步： 一个一个的完成，一个做完另一个才能进来。
效率就会降低。

使用Thread对象的Lock和Rlock可以实现简单的线程同步，这两个对象都有acquire方法和release方法，
对于那些需要每次只允许一个线程操作的数据，可以将其操作放到acquire和release方法之间。

多线程的优势在于可以同时运行多个任务（至少感觉起来是这样）。
但是当线程需要共享数据时，可能存在数据不同步的问题。
为了避免这种情况，引入了锁的概念。

lock =threading.Lock()

lock.acquire()  请求得到锁
  ......
lock.release()  释放锁

只要不释放其他的线程都无法进入运行状态
'''

import threading
import random
import time

lock = threading.Lock()

list1 = [0] * 10


def task1():
    # 获取线程锁，如果已经上锁，则等待锁的释放
    # lock.acquire()  # 阻塞
    for i in range(len(list1)):
        list1[i] = 1
        time.sleep(0.5)
    # lock.release()  释放锁


def task2():
    # lock.acquire()  # 阻塞
    for i in range(len(list1)):
        print('---->', list1[i])
        time.sleep(0.5)
    # lock.release()


if __name__ == '__main__':
    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)

    t2.start()
    t1.start()

    t2.join()
    t1.join()

    print(list1)


# 死锁
'''
开发过程中使用线程，在线程间共享多个资源的时候，
如果两个线程分别占有一部分资源并且同时等待对方的资源，就会造成死锁。
尽管死锁很少发生，但一旦发生就会造成应用的停止响应，程序不做任何事情。

避免死锁：
解决：
1. 重构代码
2. 使用timeout参数

'''

from threading import Thread, Lock
import time

lockA = Lock()
lockB = Lock()


class MyThread(Thread):
    # def __init__(self,name):
    #     pass
    def run(self):  # start()
        if lockA.acquire():  # 如果可以获取到锁则返回True
            print(self.name + '获取了A锁')  #
            time.sleep(0.1)
            if lockB.acquire(timeout=5):  # 阻塞
                print(self.name + '又获取了B锁，原来还有A锁')
                lockB.release()
            lockA.release()


class MyThread1(Thread):
    def run(self):  # start()
        if lockB.acquire():  # 如果可以获取到锁则返回True
            print(self.name + '获取了B锁')
            time.sleep(0.1)
            if lockA.acquire(timeout=5):
                print(self.name + '又获取了A锁，原来还有B锁')
                lockA.release()
            lockB.release()


if __name__ == '__main__':
    t1 = MyThread()
    t2 = MyThread1()

    t1.start()
    t2.start()

'''
生产者与消费者：两个线程之间的通信

Python的queue模块中提供了同步的、线程安全的队列类，包括FIFO（先入先出)队列Queue，
LIFO（后入先出）队列LifoQueue，和优先级队列PriorityQueue。这些队列都实现了锁原理
（可以理解为原子操作，即要么不做，要么就做完），能够在多线程中直接使用。
可以使用队列来实现线程间的同步。

'''

import threading
import queue
import random
import time


def produce(q):
    i = 0
    while i < 10:
        num = random.randint(1, 100)
        q.put("生产者产生数据：%d" % num)
        print("生产者产生数据：%d" % num)
        time.sleep(1)
        i += 1
    q.put(None)
    # 完成任务
    q.task_done()


def consume(q):
    while True:
        item = q.get()
        if item is None:
            break
        print("消费者获取到：%s" % item)
        time.sleep(4)
    # 完成任务
    q.task_done()


if __name__ == "__main__":
    q = queue.Queue(10)
    arr = []

    # 创建生产者
    th = threading.Thread(target=produce, args=(q,))
    th.start()

    # 创建消费者
    tc = threading.Thread(target=consume, args=(q,))
    tc.start()

    th.join()
    tc.join()
    print("END")

'''
线程：Thread

1. 创建线程
   A.t =  Thread(target=func,name='',args=(),kwargs={})  新建状态
     t.start()  ---->就绪状态

     run()
     join()   
   B. 自定义线程
        class MyThread(Thread):
           def __init__(self,name):
              super().__init__()
              self.name=name

            def run(self):
                任务

        t = MyThread('name')
        t.start()


2. 数据共享
        进程共享数据与线程共享数据区别：
          进程是每个进程中都有一份
          线程是共同一个数据  ----》 数据安全性问题

        GIL  ----》 伪线程 

        lock = Lock()
        lock.acquire()
        ......
        lock.release()

        -----> 只要用锁：死锁
        避免死锁
3. 线程间通信： 生产者与消费者
   生产者：线程
   消费者：线程
   import queue

   q = queue.Queue()
     # 创建生产者
    th = threading.Thread(target=produce, args=(q,))
    th.start()

    # 创建消费者
    tc = threading.Thread(target=consume, args=(q,))
    tc.start()

   q.put()
   q.get()

扩展： GIL

'''
