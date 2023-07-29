from unittest import result
from sklearn import set_config

class Calculator:
    def __init__(self,first,second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def mult(self):
        result = self.first * self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

class PerfectCal(Calculator):
    def remainder(self):
        result = self.first%self.second
        return result

a = PerfectCal(6,3)
print(a.add())
print(a.sub())
print(a.mult())
print(a.div())
print(a.remainder())