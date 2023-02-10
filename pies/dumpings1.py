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
first = True
def main():
    while not end:
        with keyboard.Listener(on_press=on_press) as listener:
            print("starting") 
            time.sleep(1)
            global first
            first = True
            # 1.3 dough
            # 2.7 meat  1.5 carrot
            # /3 pin /2 workstation 

            
            while ( break_program):
                
                per(.1)
                right(.2)
                per(.1)
                oh(.7)
                 #grab
        
                
                left(.2) #cooler
                per(.1) #meat
                upp(.3)
                per(.1)
                oh(1.4) #cut meat
                per(.1)
                right(.15)
                per(.1) #place meat
                down(.25)
                right(.25)
                per(.1) #grab carrot
                up(.2)
                upp(.2)
                per(.1)
                oh(.85) #cut carrot
                per(.1)
                right(.15)
                per(.1) #place carrot
                oh(.3)#roll
                per(.1)
                down(.5)
                per(.1) #place on hob
                time.sleep(.6)
                
                per(.1)
                left(.2)
                per(.1)
                up(.5)

        
    

def on_press(key):
    global break_program
    global end
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

def upp (x): #A&W    
    PressKey(0x11)
    PressKey(0x20)
    time.sleep(x)
    ReleaseKey (0x11)
    ReleaseKey(0x20)

def ul (x): #A&W    
    PressKey(0x11)
    up(.1)
    per(.05)
    time.sleep(x)
    ReleaseKey(0x11)    
    

def down (x):   #S
    PressKey(0x1F)
    time.sleep(x)
    ReleaseKey(0x1F)

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

