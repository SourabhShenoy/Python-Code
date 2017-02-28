import collections

class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.queue = collections.deque(maxlen=size)
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        queue = self.queue
        queue.append(val)
        return float(sum(queue))/len(queue)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)



class MovingAverage(object):

    def __init__(self, size):
        self.queue = deque(maxlen=size)
        self.wsize = size
        self.cursum = 0
        

    def next(self, val):
        self.cursum += val
        if len(self.queue) == self.wsize:
            self.cursum -= self.queue.popleft()
        self.queue.append(val)
        return float(self.cursum) / len(self.queue)