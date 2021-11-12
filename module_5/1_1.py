class StringVar:

    def __init__(self, st):
        self.st = st

    def set(self, st):
        self.st = st
        return self.st

    def get(self):
        return self.st


s = StringVar(input())
print(s.get())
print(s.set('Hello World'))
