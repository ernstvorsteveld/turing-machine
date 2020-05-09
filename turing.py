import PySimpleGUI as sg

class Tape:
    def __init__(self, name, tape, head):
        self.name = name
        self.tape = tape
        self.head = head

    def move(self, moveTo):
        if(hasattr(self.__class__, moveTo) and callable(getattr(self.__class__, moveTo))) :
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

class TapeCommander:

    def __init__(self):
        self.TapeLabels={'ST','RA', 'RB', 'S'}
        self.Tape=""

        self.tapes = [
            Tape('ST', ['1','1','1','1'], 0),
            Tape('RA', ['1','1','1','1'], 0),
            Tape('RB', ['1','1','1','1'], 0),
            Tape('S', ['1','0','1','1'], 0)]

#        self.AllTapes=[Tape0, Tape1, Tape2, Tape3]
#        self.AllHeads=[TapeHead0, TapeHead1, TapeHead2, TapeHead3]
#        print(AllTapes)
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



##Kan weg code
#voorbeeld=SplitTape(AllTapes[0],AllHeads[0])
#Tape0Lengte=len(Tape0)
#TapeHead0=0
#print(voorbeeld, Tape0Lengte)

#exit()
##Kan weg code

def TapeLayout(label, left, head, right, name):
    return [sg.Text(size=(12,1), key=left,justification='right', text=label),
    sg.Text(size=(1,1), key=head,justification='center'),
    sg.Text(size=(12,1), key=right,justification='left'),
    sg.Text(name)]

       
sg.theme('Dark Blue 3')

frame_TapeCommando =[[sg.Button('INIT Tapes', key='INIT' ,font='Courier 10', size=[20,1])],
               [sg.Button('Write Tape', key='write',font='Courier 10', size=[20,1]),
                sg.Input(key='-WST-', size=(1,1)),
                sg.Input(key='-WRA-',size=(1,1)),
                sg.Input(key='-WRB-',size=(1,1)),
                sg.Input(key='-WS-', size=(1,1))],
               [sg.Button('Move Tape', key='move',font='Courier 10', size=[20,1]),
                sg.Input(key='-MST-', size=(1,1)),
                sg.Input(key='-MRA-',size=(1,1)),
                sg.Input(key='-MRB-',size=(1,1)),
                sg.Input(key='-MS-', size=(1,1))],
               [sg.Button('Read Tape', key='Show',font='Courier 10', size=[20,1], bind_return_key='true')]]

frame_TapeInformatie =[
             TapeLayout('Stack',      '-TapeLeftPos0-', '-TapeHeadPos0-','-TapeRightPos0-', 'STACK Tape'),
             TapeLayout('Register A', '-TapeLeftPos1-', '-TapeHeadPos1-','-TapeRightPos1-', 'Register A'),
             TapeLayout('Register B', '-TapeLeftPos2-', '-TapeHeadPos2-','-TapeRightPos2-', 'Register B'),
             TapeLayout('Status',     '-TapeLeftPos3-', '-TapeHeadPos3-','-TapeRightPos3-', 'STATUS')
            ]

layout = [  [sg.Frame('Tape Informatie', frame_TapeInformatie,font='Courier 12')],
            [sg.Frame('Tape Commando', frame_TapeCommando,font='Courier 12')],
            [sg.Button('Exit',font='Courier 10', size=[20,1])]]          

window = sg.Window('Window Title', layout, font='courier 18', keep_on_top = True, no_titlebar=False, grab_anywhere=False)


tapeCommander = TapeCommander()

while True:  # Event Loop
    event, values = window.read(timeout = None)       # can also be written as event, values = window()
    print(event, values)
    if event is None or event == 'Exit':
        break
    if event == 'INIT':
        tapeCommander = TapeCommander()
    if event == 'write':
        tapeCommander.write([values['-WST-'],values['-WRA-'],values['-WRB-'],values['-WS-']])
    if event == 'move':
        tapeCommander.move([values['-MST-'],values['-MRA-'],values['-MRB-'],values['-MS-']])
    if event == 'Show':
#         TapeCommand=values['-TapeCommand-']
#         CommandValues=[values['-STval-'],values['-RAval-'],values['-RBval-'],values['-Sval-']]
#         TapeCommander(TapeCommand, CommandValues)
       
       
## Read all tapes en schow
    #STACK TAPE
        PrintTape = tapeCommander.print('ST')
        window['-TapeLeftPos0-'].update(PrintTape[0])
        window['-TapeHeadPos0-'].update(PrintTape[1])
        window['-TapeRightPos0-'].update(PrintTape[2])
    #Register A 
        PrintTape = tapeCommander.print('RA')
        window['-TapeLeftPos1-'].update(PrintTape[0])
        window['-TapeHeadPos1-'].update(PrintTape[1])
        window['-TapeRightPos1-'].update(PrintTape[2])
    #Register B  
        PrintTape = tapeCommander.print('RB')
        window['-TapeLeftPos2-'].update(PrintTape[0])
        window['-TapeHeadPos2-'].update(PrintTape[1])
        window['-TapeRightPos2-'].update(PrintTape[2])
    #STATUS TAPE
        PrintTape = tapeCommander.print('S')
        window['-TapeLeftPos3-'].update(PrintTape[0])
        window['-TapeHeadPos3-'].update(PrintTape[1])
        window['-TapeRightPos3-'].update(PrintTape[2])

window.close()

