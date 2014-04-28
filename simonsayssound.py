from msvcrt import getch

import winsound
Freq = 2500 # Set Frequency To 2500 Hertz
Dur = 1000 # Set Duration To 1000 ms == 1 second
winsound.Beep(Freq,Dur)

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
        elif key == 72: #Up arrow
            winsound.Beep(3000,Dur)
        elif key == 75: #left arrow
            winsound.Beep(3500,Dur)
        elif key == 77: #left arrow
            winsound.Beep(4000,Dur)