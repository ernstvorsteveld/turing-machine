import tape as t

class TapeCommander:

    def __init__(self):
        self.TapeLabels={'ST','RA', 'RB', 'S'}
        self.Tape=""

        self.tapes = [
            t.Tape('ST', ['1','1','1','1'], 0),
            t.Tape('RA', ['1','1','1','1'], 0),
            t.Tape('RB', ['1','1','1','1'], 0),
            t.Tape('S', ['1','1','1','1'], 0)]

    def getLabels(self):
        return self.TapeLabels

    def move(self, moves):
        index = 0
        for tape in self.tapes:
           tape.move(moves[index]) 
           index += 1

    def write(self, values):
        index = 0
        for tape in self.tapes:
            tape.write(values[index])
            index += 1

    def get(self, name):
        for tape in self.tapes:
            if tape.hasName(name):
                return tape
        print('tape not found')

    def print(self, name):
        tape = self.get(name)
        return tape.print()
