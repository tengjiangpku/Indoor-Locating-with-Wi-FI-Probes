class lru():
    def __init__(self, max_length = 5):
        self.max_length = max_length
        self.l = [0 for _ in range(self.max_length)]
        self.length = 0
        self.idx = 0
        self.sum = 0

    def insert(self, value):
        if self.length < self.max_length:
            self.sum += value
            self.l[self.idx] = value
            self.idx += 1
            self.length += 1
            if self.idx == self.max_length:
                self.idx = 0
        else:
            self.sum -= self.l[self.idx]
            self.l[self.idx] = value
            self.sum += self.l[self.idx]
            self.idx += 1
            if self.idx == self.max_length:
                self.idx = 0
    
    def ave(self):
        if self.length == 0:
            return 0
        return self.sum/self.length

if __name__ == '__main__':
    l = lru()
    for i in range(10):
        l.insert(i)
        print(l.ave())