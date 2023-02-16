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

            # 4,25 roll  2.4 cook
            # /3 pin /2 workstation 

            with keyboard.Listener(on_press=on_press) as listener:
                while ( break_program):
                    if (first):
                        per(.1)
                        right(.3)
                        per(.1)
                        oh(2.3)
                        per(.1) #grab
                        first = False
                    else :
                        right(.3)
                        oh(1) #roll
                        per(.1) #grab
                    
                    left(.3) #cooler
                    per(.1) #meat
                    #right(.3)spowpdposoposo
                    #per(.1)
                    #time.sleep(.1)
                    #per(.1) #pie
                    down(.4)
                    per(.1)
                    oh(.1)
                    #pyautogui.sleep(3)  cook
                    up(.4)
                    per(.1)
                    right(.3)
                    per(.1)
                    oh(1.2)   #roll
                    down(.4)

                    
                    oh(.1)
                    per(.1)
                    left(.3)
                    per(.1)
                    up(.5)

        
    

def on_press(key):
    global break_program
    global end
    print (key)
    if key == keyboard.Key.end:
        print ('end pressed')
        break_program = False

        return False
    elif key == keyboard.Key.home:
        print('home pressed')
        break_program = True
        return False
    elif key == keyboard.Key.delete:
        print('end pressed')
        end = True
        return False
    
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

def ul (x): #A&W    
    PressKey(0x11)
    up(.1)
    per(.1)
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
             