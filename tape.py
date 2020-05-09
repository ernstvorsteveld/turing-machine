class Tape:
    def __init__(self, name, tape, head):
        self.name = name
        self.tape = tape
        self.head = head
        self.moves = { 'L' : self.left, 'R' : self.right }

    def move(self, moveTo):
        if moveTo in self.moves:
            self.moves.get(moveTo)()

    def stay(self):
        print('stay')

    def left(self):
        print('links')  ## this is more like right
        self.head += 1
        if self.head == len(self.tape):
            self.tape.append('_')

    def right(self):
        print('rechts')
        if self.head == 0:
            self.tape.insert(0, '_')
        else:
            self.head -= 1

    def write(self, val):
        self.tape[self.head] = val

    def print(self):
        print(self.head)
        print(self.tape)
        if self.head == len(self.tape) - 1:
            return [''.join(self.tape[:self.head]), self.tape[self.head], '']
        return [''.join(self.tape[:self.head]), self.tape[self.head], ''.join(self.tape[self.head+1:])]

    def hasName(self, name):
        return self.name == name

    def getHead(self):
        return self.head

