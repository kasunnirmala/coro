import serial
from pynput.keyboard import Key, Controller
ser = serial.Serial("COM30", 9600)

release =True

while True:
    bytesToRead = ser.inWaiting()
    keyboard = Controller()
    cc=str(ser.readline())
    print(cc)
    ss=(cc[2:3])
 
    while not ser.inWaiting():
        print(ss)

        if ss=='U':
            release =True
            keyboard.press(Key.up)
            #  keyboard.release(Key.down)
            #  keyboard.release(Key.left)
            #  keyboard.release(Key.right)
            #  keyboard.release(Key.up)
        elif ss== 'D':
            release =True
            keyboard.press(Key.down)
            # keyboard.release(Key.up)
            # keyboard.release(Key.left)
            # keyboard.release(Key.right)
            # keyboard.release(Key.down)
        elif ss=='L':
            release =True
            keyboard.press(Key.left)
            # keyboard.release(Key.down)
            # keyboard.release(Key.up)
            # keyboard.release(Key.right)
            # keyboard.release(Key.left)
        elif ss=='R':
            release =True
            keyboard.press(Key.right)
            # keyboard.release(Key.down)
            # keyboard.release(Key.left)
            # keyboard.release(Key.up)
        elif ss=='S':
            if release:
                release=False
                keyboard.release(Key.down)
                keyboard.release(Key.left)
                keyboard.release(Key.up)
                keyboard.release(Key.right)
                keyboard = Controller()
            # keyboard.release(Key.down)
            # keyboard.release(Key.left)
            # keyboard.release(Key.up)
            # keyboard.release(Key.right)
            
    # keyboard.release(Key.right)
      
        
    
    
    # keyboard.press('a')
    