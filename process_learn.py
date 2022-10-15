'''
生活中，你可能一边听歌，一边写作业；一边上网，一边吃饭。。。这些都是生活中的多任务场景。电脑也可以执行多任务，比如你可以同时打开浏览器上网，听音乐，打开pycharm编写代码...。简单的说**多任务就是同一时间内运行多个程序**

- 单核CPU实现多任务原理：操作系统轮流让各个任务交替执行，QQ执行2us，切换到微信，在执行2us，再切换到陌陌，执行2us……。表面是看，每个任务反复执行下去，但是CPU调度执行速度太快了，导致我们感觉就行所有任务都在同时执行一样

- 多核CPU实现多任务原理：真正的秉性执行多任务只能在多核CPU上实现，但是由于任务数量远远多于CPU的核心数量，所以，操作西永也会自动把很多任务轮流调度到每个核心上执行

- 并发和并行
  - **并发**：当有多个线程在操作时,如果系统只有一个CPU,则它根本不可能真正同时进行一个以上的线程，它只能把CPU运行时间划分成若干个时间段,再将时间 段分配给各个线程执行，在一个时间段的线程代码运行时，其它线程处于挂起状。.这种方式我们称之为并发(Concurrent)。
  - **并行**：当系统有一个以上CPU时,则线程的操作有可能非并发。当一个CPU执行一个线程时，另一个CPU可以执行另一个线程，两个线程互不抢占CPU资源，可以同时进行，这种方式我们称之为并行(Parallel)。
- 实现多任务的方式：
  - 多进程模式；
  - 多线程模式；
  - 协程。
  进程  >  线程  >  协程

  from multiprocessing import Process

  process = Process(target= 函数，name=进程的名字，args=（给函数传递的参数）)
  process 对象

  对象调用方法:
  process.start()    启动进程并执行任务
  process.run()  只是执行了任务但是没有启动进程
  terminate()   终止
'''

# 进程创建
import os
from multiprocessing import Process
from time import sleep


def task1(s, name):
    while True:
        sleep(s)
        print('这是任务1.。。。。。。。。。。', os.getpid(), '------', os.getppid(), name)


def task2(s, name):
    while True:
        sleep(s)
        print('这是任务2.。。。。。。。。。。', os.getpid(), '------', os.getppid(), name)


number = 1
if __name__ == '__main__':
    print(os.getpid())
    # 子进程
    p = Process(target=task1, name='任务1', args=(1, 'aa'))
    p.start()
    print(p.name)
    p1 = Process(target=task2, name='任务2', args=(2, 'bb'))
    p1.start()
    print(p1.name)

    while True:
        number += 1
        sleep(0.2)
        if number == 100:
            p.terminate()
            p1.terminate()
            break
        else:
            print('---------------->number:',number)

    print('--------------')
    print('*****************')


# 进程创建

'''
 多进程对于全局变量访问，在每一个全局变量里面都放一个m变量，
 保证每个进程访问变量互不干扰。
 m = 1  # 不可变类型
 list1 = []  # 可变类型

 主进程启动子进程，启动之后无法控制是谁先谁后
'''
import os
from multiprocessing import Process
from time import sleep

m = 1  # 不可变类型
list1 = []  # 可变类型


def task1(s, name):
    global m
    while True:
        sleep(s)
        m += 1
        list1.append(str(m) + 'task1')
        print('这是任务1.。。。。。。。。。。', m, list1)


def task2(s, name):
    global m
    while True:
        sleep(s)
        m += 1
        list1.append(str(m) + 'task2')
        print('这是任务2.。。。。。。。。。。', m, list1)


if __name__ == '__main__':

    # 子进程
    p = Process(target=task1, name='任务1', args=(1, 'aa'))
    p.start()

    p1 = Process(target=task2, name='任务2', args=(2, 'bb'))
    p1.start()

    while True:
        sleep(1)
        m += 1
        print('--------->main:', m)


# 进程：自定义
from multiprocessing import Process


class MyProcess(Process):

    def __init__(self, name, num):
        super(MyProcess, self).__init__()
        self.name = name
        self.num = num

    # 重写run方法
    def run(self):
        n = 1
        while True:
            # print('进程名字：' + self.name)
            print('{}--------->自定义进程,n:{}'.format(n, self.name))
            n += 1


if __name__ == '__main__':
    p = MyProcess('小明', 10)
    p.start()

    p1 = MyProcess('小红')
    p1.start()



'''
当需要创建的子进程数量不多时，可以直接利用multiprocessing中的Process动态成生多个进程，
但如果是上百甚至上千个目标，手动的去创建进程的工作量巨大，此时就可以用到multiprocessing模块提供的Pool方法。
初始化Pool时，可以指定一个最大进程数，当有新的请求提交到Pool中时，如果池还没有满，
那么就会创建一个新的进程用来执行该请求；但如果池中的进程数已经达到指定的最大值，那么该请求就会等待，
直到池中有进程结束，才会创建新的进程来执行。

非阻塞式:全部添加到队列中，立刻返回，并没有等待其他的进程完毕，但是回调函数是等待任务完成之后才调用。

阻塞式:
'''
import os
from multiprocessing import Pool
import time

# 非阻塞式进程
from random import random


def task(task_name):
    print('开始做任务啦!', task_name)
    start = time.time()
    # 使用sleep
    time.sleep(random() * 2)
    end = time.time()
    # print()
    return '完成任务:{}!用时:{},进程id:{}'.format(task_name, (end - start), os.getpid())


container = []


def callback_func(n):
    container.append(n)


if __name__ == '__main__':
    pool = Pool(5)

    tasks = ['听音乐', '吃饭', '洗衣服', '打游戏', '散步', '看孩子', '做饭']
    for task1 in tasks:
        pool.apply_async(task, args=(task1,), callback=callback_func)

    pool.close()  # 添加任务结束
    pool.join()  #

    for c in container:
        print(c)
    print('over!!!!!')

# 阻塞式
import os
import time
from multiprocessing import Pool
from random import random

'''
 特点：
 添加一个执行一个任务，如果一个任务不结束另一个任务就进不来。

 进程池：
 pool = Pool(max)  创建进程池对象
 pool.apply()  阻塞的
 pool.apply_async()  非阻塞的

 pool.close()  
 pool.join()  让主进程让步

'''


def task(task_name):
    print('开始做任务啦!', task_name)
    start = time.time()
    # 使用sleep
    time.sleep(random() * 2)
    end = time.time()
    print('完成任务:{}!用时:{},进程id:{}'.format(task_name, (end - start), os.getpid()))


if __name__ == '__main__':
    pool = Pool(5)
    tasks = ['听音乐', '吃饭', '洗衣服', '打游戏', '散步', '看孩子', '做饭']
    for task1 in tasks:
        pool.apply(task, args=(task1,))
    pool.close()
    pool.join()
    print('over!!!!')


# 进程间通信
from multiprocessing import Queue

q = Queue(5)

q.put('A')
q.put('B')
q.put('C')
q.put('D')
q.put('E')
print(q.qsize())
if not q.full():  # 判断队列是否满    q.empty()  判断队列是否是空的
    q.put('F', timeout=3)  # put() 如果queue满了则只能等待，除非有‘空地’则添加成功
else:
    print('队列已满！')


# 获取队列的值
print(q.get(timeout=2))
print(q.get(timeout=2))
print(q.get(timeout=2))
print(q.get(timeout=2))
print(q.get(timeout=2))
print(q.get(timeout=2))

# q.put_nowait()
# q.get_nowait()


# 进程间通信
from multiprocessing import Process, Queue
from time import sleep


def download(q):
    images = ['girl.jpg', 'boy.jpg', 'man.jpg']
    for image in images:
        print('正在下载:', image)
        sleep(0.5)
        q.put(image)


def getfile(q):
    while True:
        try:
            file = q.get(timeout=5)
            print('{}保存成功！'.format(file))
        except:
            print('全部保存完毕！')
            break


if __name__ == '__main__':
    q = Queue(5)
    p1 = Process(target=download, args=(q,))
    p2 = Process(target=getfile, args=(q,))

    p1.start()
    p1.join()

    p2.start()
    p2.join()

    print('00000000000')
