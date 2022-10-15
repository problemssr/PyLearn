# 线程
'''
  考虑？创建线程？ 如何使用线程？
   t = threading02.Thread(target=download, name='aa', args=(1,))
    t.start()

  线程：
    新建  就绪  运行  阻塞  结束

'''

import threading02

# 进程： Process
# 线程:  Thread
from time import sleep


def download(n):
    images = ['girl.jpg', 'boy.jpg', 'man.jpg']
    for image in images:
        print('正在下载:', image)
        sleep(n)
        print('下载{}成功！'.format(image))


def listenMusic():
    musics = ['大碗宽面', '土耳其冰淇淋', '烤面筋', '烤馒头片']
    for music in musics:
        sleep(0.5)
        print('正在听{}歌！'.format(music))


if __name__ == '__main__':
    # 线程对象
    t = threading02.Thread(target=download, name='aa', args=(1,))
    t.start()

    t1 = threading02.Thread(target=listenMusic, name='aa')
    t1.start()

    # n = 1
    # while True:
    #     print(n)
    #     sleep(1.5)
    #     n += 1


import threading
from time import sleep

'''
线程是可以共享全局变量的
GIL  全局解释器锁

'''
ticket = 1000


def run1():
    global ticket
    for i in range(100):
        sleep(0.1)
        ticket -= 1


# def run2():
#     global ticket
#     for i in range(100):
#         ticket -= 1


if __name__ == "__main__":
    # 创建线程
    th1 = threading.Thread(target=run1, name="th1")
    th2 = threading.Thread(target=run1, name="th2")
    th3 = threading.Thread(target=run1, name="th3")
    th4 = threading.Thread(target=run1, name="th4")
    # 启动
    th1.start()
    th2.start()
    th3.start()
    th4.start()

    th1.join()
    th2.join()
    th3.join()
    th4.join()

    print('money:', ticket)


import threading

n = 0


def task1():
    global n
    for i in range(1000000):
        n += 1
    print('----》task1中的n值是：', n)


def task2():
    global n
    for i in range(1000000):
        n += 1
    print('----》task2中的n值是：', n)


if __name__ == '__main__':
    th1 = threading.Thread(target=task1)
    th2 = threading.Thread(target=task2)

    th1.start()
    th2.start()

    th1.join()
    th2.join()

    print("最后打印n:", n)
