
class FreqStack(object):

    def __init__(self):
        self.freq = {}
        self.group = {}
        self.maxfreq = 0

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        freq_val = self.freq.get(val, 0) + 1
        self.freq[val] = freq_val
        if freq_val > self.maxfreq:
            self.maxfreq = freq_val
        if freq_val not in self.group:
            self.group[freq_val] = []
        self.group[freq_val].append(val)
        

    def pop(self):
        """
        :rtype: int
        """
        val = self.group[self.maxfreq].pop()
        self.freq[val] -= 1
        if not self.group[self.maxfreq]:
            del self.group[self.maxfreq]
            self.maxfreq -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()