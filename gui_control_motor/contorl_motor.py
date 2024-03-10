import tkinter as tk
#import RPi.GPIO as gpio
import time
import threading

DIR = 12
PUL = 18

"""gpio.setmode(gpio.BOARD)
gpio.setup([PUL, DIR], gpio.OUT)"""


"""pwmPUL = gpio.PWM(PUL, 2085)  
pwmPUL.start(0)
"""

fixed_rotation="cw" #固定順時針

def rotate(angle, direction):
    """
    ccw:逆,cw:顺
    """
    if direction == "ccw":
        gpio.output(DIR, gpio.LOW)
    elif direction == "cw":
        gpio.output(DIR, gpio.HIGH)
    else:
        return
    pwmPUL.ChangeDutyCycle(50)
    time.sleep(angle / 360)
    pwmPUL.ChangeDutyCycle(0)



def run_motor():#馬達運作
   
    def run():
        """gpio.setmode(gpio.BOARD)
        gpio.setup([PUL, DIR], gpio.OUT)
        
        pwmPUL.start(0)"""

      
        while True:
            
            angle=1
            rotate(angle,fixed_rotation)
            run_motor_label.config(text=f"motor is running now!")

    thread=threading.Thread(target=run)
    thread.start()
    


def stop_motor():#暫停馬達
    
    angle =0
    """pwmPUL.stop()
    gpio.cleanup()"""
    run_motor_label.config(text=f"motor stopping")



# 創建視窗
window = tk.Tk()
window.title("control_motor_platform")
window.geometry('380x380')
window.config(bg="#323232")

# 創建元件
run_motor_label = tk.Label(window,text="press button to start motor")
stop_motor_button=tk.Button(window,text="stop",command=stop_motor,bg="red",width=10,height=5)
run_button = tk.Button(window, text="start_running", command=run_motor,bg="yellow",width=10,height=5)


# 放置元件
run_motor_label.pack()
run_button.pack(side="top")
stop_motor_button.pack(side="top")

# 開始運行視窗
window.mainloop()
