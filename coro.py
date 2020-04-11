import serial
from pynput.keyboard import Key, Controller
ser = serial.Serial("COM30", 9600)

keyboard = Controller()
while True:
    # bytesToRead = ser.inWaiting()
    cc=str(ser.readline())
    print(cc)
    ss=(cc[2:3])
 
    while not ser.inWaiting():
        print(ss)

        if ss=='U':
             keyboard.press(Key.up)
            #  keyboard.release(Key.down)
            #  keyboard.release(Key.left)
            #  keyboard.release(Key.right)
            #  keyboard.release(Key.up)
        elif ss== 'D':
            keyboard.press(Key.down)
            # keyboard.release(Key.up)
            # keyboard.release(Key.left)
            # keyboard.release(Key.right)
            # keyboard.release(Key.down)
        elif ss=='L':
            keyboard.press(Key.left)
            # keyboard.release(Key.down)
            # keyboard.release(Key.up)
            # keyboard.release(Key.right)
            # keyboard.release(Key.left)
        elif ss=='R':
            keyboard.press(Key.right)
            # keyboard.release(Key.down)
            # keyboard.release(Key.left)
            # keyboard.release(Key.up)
        elif ss=='S':
            keyboard.release(Key.down)
            keyboard.release(Key.left)
            keyboard.release(Key.up)
            keyboard.release(Key.right)
            
            # keyboard.release(Key.right)
      
        
    
    
    # keyboard.press('a')
    