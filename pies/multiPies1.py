import pyautogui
import time
from pynput import keyboard

    #to do list 
    # move comand from 8624 num pad arrow keys
    # move comand to 1234 so rotate in a circle 1 to 4 for rotate
    # different if for /3 /2 & /6 
    # + == upgrade listener
    #

break_program = False
end = False
pause = False
first = True
choice = 0
queue = []
def main():
    while not end:
        with keyboard.Listener(on_press=on_press) as listener:
            print("starting") 
            time.sleep(1)
            global first
            first = True
            global queue
            blank = []
            global break_program
            global pause
            global choice

            # 4,25 roll  2.4 cook
            # /3 pin /2 workstation 

            
            while ( break_program):
                
                
                
                if (first):
                    per(.1)

                    upp(.3)
                    #right(.3)
                    per(.1)
                    oh(4.3/6)
                    per(.1) #grabo
                    first = False
                else :

                    upp(.3)
                   # oh(3.3/3) #roll
                    per(.1) #grab
                
                if queue[0] == 1:
                    choice=1
                    left(.3) #cooler
                    per(.1) #meat
                    #right(.3)spowpdposoposo
                    #per(.1)
                    #time.sleep(.1)
                    #per(.1) #pie
                    down(.5)
                    per(.1)
                    oh(.1)
                elif queue[0] == 2:
                    choice=2
                    right(.3)
                    per(.1)
                    down(.5)
                    per(.1)
                    oh(.1)
                elif queue[0] == 3:
                    choice =3
                    down(.5)
                    right(.3)
                    per(.1)
                    down(.3)
                    per(.3)
                    left(.3)
                    down(.3)
                    per(.1)
                    oh(.1)

                queue.pop(0)
                if  len(queue) == 0:
                    
                    pause = True
                    print("is empty")
                    time.sleep(2.4)
                    oh(.1)
                    per(.1)
                    if choice == 1:
                        left(.3)
                        per(.1)
                        up(.5)
                    elif choice ==2 :
                        dll(.3)
                        per(.1)
                        up(.5)
                    elif choice == 3:
                        up(.3)
                        ull(.3)
                        per(.1)
                        up(.2)
                    
                    first = True
                else :
                    print("is not empty")
                    up(.5)
                    per(.1)
                    upp(.3)
                    per(.1)
                    oh(1.3)   #roll
                    down(.5)
                    oh(.1)
                    per(.1)
                    if choice == 1:
                        left(.3)
                        per(.1)
                        up(.5)
                    elif choice == 2:
                        dll(.3)
                        per(.1)
                        up(.5)
                    elif choice == 3:
                        up(.4)
                        ull(.4)
                        per(.1)
                        up(.2)
                    

                    first = False
                    
                for x in queue :
                    print (x)
                #pyautogui.sleep(3)  cook
                
                
                if  len(queue) != 0:
                    pause = False

               
                while  pause:
                    print("sleep")
                    time.sleep(1)

        
def keyMove(x):
    match x :
        case 8:
            move(1)
        case 6:
            move(2)
        case 2:
            move(3)
        case 4:
            move(4)
       
    
def move (x): 
    x=x%4
    match x :
        case 1:
            up(.2)
        case 2:
            right(.2)
        case 3: 
            down(.2)
        case 4:
            left(.2)
    


def on_press(key):
    global break_program
    global end
    global queue
    global pause
    #print (key)
    match key:
        case keyboard.Key.end:
            print ('end pressed')
            break_program = False
        case keyboard.Key.home:
            print('home pressed')
            break_program = True
        case keyboard.Key.delete:
            print('end pressed')
            end = True
        case keyboard.Key.page_up:
            print('end pressed')
            pause = False
        case keyboard.Key.page_down:
            print('end pressed')
            pause = True
        case keyboard.Key.print_screen:
            print("#1 pressed")
            queue.append(1)
            pause = False
        case keyboard.Key.scroll_lock:
            print("#2 pressed")
            queue.append(2)
            pause = False
        case keyboard.Key.pause:
            print("#3 pressed")
            queue.append(3)
            pause = False
        case keyboard.Key.backspace:
            print("backspace pressed")
            queue.pop
        case keyboard.Key.enter:
            print("enter pressed")
            queue.clear
        
        
        

    return True
        
    
def left (x): #A
    PressKey(0x1E) 
    time.sleep(x)
    ReleaseKey (0x1E)

def right (x):  #D
    PressKey(0x20)
    time.sleep(x)
    ReleaseKey (0x20)

def up (x):   #W
    PressKey(0x11)
    time.sleep(x)
    ReleaseKey (0x11)
    
def down (x):   #S
    PressKey(0x1F)
    time.sleep(x)
    ReleaseKey(0x1F)

def upp (x): #D&W    
    PressKey(0x11)
    PressKey(0x20)
    time.sleep(x)
    ReleaseKey (0x11)
    ReleaseKey(0x20)

def dll (x): #A&S  
    PressKey(0x1F)
    PressKey(0x1E)
    time.sleep(x)
    ReleaseKey (0x1F)
    ReleaseKey(0x1E)

def ull (x): #W&A  
    PressKey(0x11)
    PressKey(0x1E)
    time.sleep(x)
    ReleaseKey (0x11)
    ReleaseKey(0x1E)



       
    



def per (x):   #P
    PressKey(0x19)
    time.sleep(x)
    ReleaseKey (0x19)

def oh (x):     #O
    PressKey(0x18)
    time.sleep(x)
    ReleaseKey (0x18)


import ctypes, time
# Bunch of stuff so that the script can send keystrokes to game #

SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions 
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def KeyPress():
    time.sleep(3)
    PressKey(0x10) # press Q
    time.sleep(.05)
    ReleaseKey(0x10) #release Q

main()
             