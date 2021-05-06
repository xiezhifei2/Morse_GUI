from Tkinter import *
import Tkinter as tk
import tkFont
from gpiozero import LED
import RPi.GPIO
import time
RPi.GPIO.setmode(RPi.GPIO.BCM)
##hardware
led = LED(15)

def dot():
    led.on()
    time.sleep(0.25)
    led.off()
    time.sleep(0.25)
    
def dash():
    led.on()
    time.sleep(0.75)
    led.off()
    time.sleep(0.25)
    
def translater(i):
    if i == 'A':
        dot()
        dash()
        time.sleep(0.75)#sleep 0.75 between letter
    if i == 'B':
        dash()
        dot()
        dot()
        dot()
        time.sleep(0.75)#sleep 0.75 between letter
    if i == 'C':
        dash()
        dot()
        dash()
        dot()
        time.sleep(0.75)#sleep 0.75 between letter
    if i == 'D':
        dash()
        dot()
        dot()
        time.sleep(0.75)#sleep 0.75 between letter
    if i == 'E':
        dot()
        time.sleep(0.75)#sleep 0.75 between letter
    if i == 'F':
        dot()
        dot()
        dash()
        dot()
        time.sleep(0.75)#sleep 0.75 between letter
    if i == 'G':
        dash()
        dash()
        dot()
        time.sleep(0.75)#sleep 0.75 between letter
    if i == 'H':
        dot()
        dot()
        dot()
        dot()
        time.sleep(0.75)#sleep 0.75 between letter
    if i == 'I':
        dot()
        dot()
        time.sleep(0.75)#sleep 0.75 between letter
    if i == 'J':
        dot()
        dash()
        dash()
        dash()
        time.sleep(0.75)#sleep 0.75 between letter
    if i == 'K':
        dash()
        dot()
        dash()
        time.sleep(0.75)#sleep 0.75 between letter
    if i == 'L':
        dot()
        dash()
        dot()
        dot()
        time.sleep(0.75)#sleep 0.75 between letter
    if i == 'M':
        dash()
        dash()
        time.sleep(0.75)#sleep 0.75 between letter
    if i == 'N':
        dash()
        dot()
        time.sleep(0.75)#sleep 0.75 between letter
    if i == 'O':
        dash()
        dash()
        dash()
        time.sleep(0.75)#sleep 0.75 between letter
    if i == 'P':
        dot()
        dash()
        dash()
        dot()
        time.sleep(0.75)#sleep 0.75 between letter
    if i == 'Q':
        dash()
        dash()
        dot()
        dash()
        time.sleep(0.75)#sleep 0.75 between letter
    if i == 'R':
        dot()
        dash()
        dot()
        time.sleep(0.75)#sleep 0.75 between letter
    if i == 'S':
        dot()
        dot()
        dot()
        time.sleep(0.75)#sleep 0.75 between letter
    if i == 'T':
        dash()
        time.sleep(0.75)#sleep 0.75 between letter
    if i == 'U':
        dot()
        dot()
        dash()
        time.sleep(0.75)#sleep 0.75 between letter
    if i == 'V':
        dot()
        dot()
        dot()
        dash()
        time.sleep(0.75)#sleep 0.75 between letter
    if i == 'W':
        dot()
        dash()
        dash()
        time.sleep(0.75)#sleep 0.75 between letter
    if i == 'X':
        dash()
        dot()
        dot()
        dash()
        time.sleep(0.75)#sleep 0.75 between letter
    if i == 'Y':
        dash()
        dot()
        dash()
        dash()
        time.sleep(0.75)#sleep 0.75 between letter
    if i == 'Z':
        dash()
        dash()
        dot()
        dot()
        time.sleep(0.75)#sleep 0.75 between letter
        
def enter():
    words = e.get().upper()
    for i in words:
        translater(i)
        
    
def close():
    RPi.GPIO.cleanup()
    win.destroy()
    
def validation(input):
    if len(input)<13:##maximum 12 character
        return True
    else:
        return False
    
win = tk.Tk()
win.title("Morse Code Tanslator LED ")
myFont = tkFont.Font(family = 'Helvetica',size = 12, weight = "bold")

#enter box
v = StringVar()
test = win.register(validation)#wrap the validation function
e = Entry(win, textvariable = v, validate = 'key',
          validatecommand = (test,'%P'), width = 50)
e.grid(row = 0, column=1)

#translate button
translateButton = Button(win, text = "Translate", font = myFont, command = enter, bg = 'White',height = 1, width = 6)
translateButton.grid(row = 1, column=1)

#exit button
exitButton = Button(win, text = "Exit", font = myFont, command = close, bg = 'red',height = 1, width = 3)
exitButton.grid(row = 2, column=1)

win.protocol("WM_DELETE_WINDOW",close)#exit cleanly
win.mainloop()#keep loopping





