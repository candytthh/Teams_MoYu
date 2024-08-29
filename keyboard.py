# import os
import pyautogui  
import time  
from datetime import datetime, timedelta


    

def press_keyboard(end_time):
    try:
        # print the end time 
        print(f"程序将在{end_time}结束")
        print("请迅速切换到一个文本窗口")
        time.sleep(5) # give you 5 seconds to switch to a txt window, in future optimize to create txt 
        i=0


        while datetime.now() < end_time:

            pyautogui.typewrite("Hello World!", interval=0.5) # simulate to press keyboard, time interval is half second between characters
            pyautogui.press('return')
            print("按下按键")  # print info
            i += 1
            print(f"已执行{i}次")

            time.sleep(120)  # set time interval for loop



    
    except KeyboardInterrupt:  
        print("程序已停止")  # ctrl + c to terminate




          





if __name__ == "__main__":  
    # caculate end time in main function
    end_time = datetime.now() + timedelta(hours=2)
    # create_folder_and_file() # optimiztion of creating folder and txt automatically, save and close at end
    press_keyboard(end_time)  