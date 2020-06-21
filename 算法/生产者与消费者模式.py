import threading
import time


'''

from threading import Lock
 
lock = Lock()
lock.acquire()
lock.release()

'''
'''
    多线程实现生成者和消费者模式
'''
# 生成者类 继承方式

class Producer(threading.Thread):

    finish = True
    global queue
    def run(self):
        for i in range(10):
            queue.append(i)
            print(f'producer : {i}')
            time.sleep(3)

        queue.append(self.finish)


class Comsumer(threading.Thread):

    global queue
    def run(self):
        while True:
            if queue:
                c = queue.pop(0)
                if c is True:
                    break
                print(f'comsumer : {c}')



queue = []
p = Producer()
c = Comsumer()

p.start()
c.start()

p.join()
c.join()

'''
t= threading.Thread(target=f1,args=(111,112))#创建线程
t.start()
'''







