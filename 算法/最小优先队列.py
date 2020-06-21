import heapq

class PriQueue():

    def __init__(self, queue):
        self.queue = queue

    def push(self, val):
        heapq.heappush(self.queue, val)


    def pop(self):
        return heapq.heappop(self.queue)


pq = PriQueue([])
pq.push(5)
pq.push(1)
pq.push(3)

print(pq.pop())
print(pq.pop())

class prioQueue:

    def __init__(self, elist=[]):
        self._elems = list(elist)
        self.buildheap()

    # 构造堆
    def buildheap():
        # 从最后一个有孩子结点的结点开始调整最大堆
        first = len(array) // 2 - 1
        for start in range(first, -1, -1):
            heap_adjust(array, start, len(array) - 1)

    def heap_adjust(array, start, end):
        temp = array[start]
        child = 2 * start
        while child <= end:
            if child < end and array[child] < array[child + 1]:
                child += 1
            if temp >= array[child]:
                break
            array[start] = array[child]
            start = child
            child *= 2
        array[start] = temp

    # 插入元素
    def enqueue(self, e):
        self._elems.append(None)
        self.siftup(e, len(self._elems)-1)
        return self._elems

    def siftup(self, e, last):
        elems , i , j = self._elems, last, (last-1)//2
        while i > 0 and e < elems[j]:
            elems[i] = elems[j]
            i, j = j ,(j-1)//2
        elems[i] = e

    # 删除堆顶
    def dequeue(self):
        elems = self._elems
        e0 = elems[0]
        e = elems.pop()
        if len(elems) > 0:
            self.siftdown(e, 0 , len(elems))
        return e0

    # 获取最小元素
    def peek(self):                       
        return self._elems[0]