class Tape:
    def __init__(self, name, tape, head):
        self.name = name
        self.tape = tape
        self.head = head

    def move(self, moveTo):
        if(hasattr(self.__class__, moveTo) and callable(getattr(self.__class__, moveTo))):
            self.moveTo()

    def stay(self):
        print('stay')

    def left(self):
        print('links')  ## this is more like right
        if self.head == len(self.tape):
            self.tape.append('_')
        self.head+=1

    def right(self):
        print('rechts')
        if self.head == 0:
            self.tape.insert(0, '_')
        self.head-=1

    def write(self, val):
        self.tape[self.head] = val

    def print(self):
        return [self.tape[:self.head], self.tape[self.head], self.tape[self.head:]]

    def hasName(self, name):
        return self.name == name


