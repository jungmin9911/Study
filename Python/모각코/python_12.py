from unittest import result

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

a = Calculator(6,3)
print(a.add())
print(a.sub())
print(a.mult())
print(a.div())