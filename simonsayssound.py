from msvcrt import getch
from random import shuffle

import winsound
Freq = 2500 # Set Frequency To 2500 Hertz
Dur = 1000 # Set Duration To 1000 ms == 1 second
#winsound.Beep(Freq,Dur)


sounds = {'a': 2500,'b': 3000,'c': 3500,'d': 4500}

def generate_sequence(ins):
    h = sounds.keys()
    shuffle(h)
    ins.append(h[0])
    return ins

def play_sequence(ins):
    for element in ins:
        #Down Arrow
        winsound.beep(sounds[element],Dur)

ans = ['a', 'b']
usr = []

while True:
    ans = generate_sequence(ans)    
    usr = []
    while True:
        key = ord(getch())
        if key == 27: #ESC
            break
        elif key == 13: #Enter
            select()
        elif key == 224: #Special keys (arrows, f keys, ins, del, etc.)
            key = ord(getch())
            if key == 80: #Down arrow
                winsound.Beep(Freq,Dur)
                usr.append("a")
            elif key == 72: #Up arrow
                winsound.Beep(3000,Dur)
                usr.append("b")
            elif key == 75: #left arrow
                winsound.Beep(3500,Dur)
                usr.append("c")
            elif key == 77: #right arrow
                winsound.Beep(4000,Dur)
                usr.append("d")
        #space bar
        elif key == 32:
            break
    if ans == usr:
        print 'Congratulations, let\'s begin the next round'
    else:
        print 'YOU LOST!!!'
        exit(11)
    
