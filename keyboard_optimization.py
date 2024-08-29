import os
import pyautogui  
import time  
from datetime import datetime, timedelta



def create_folder_and_file():

    #caputre path of Desktop
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    #create path of folder whose name is keyboard_record
    folder_name = "keyboard_record"
    folder_path = os.path.join(desktop_path, folder_name)

    # create such a folder if it not exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"创建文件夹: {folder_path}")
    else:
        print(f"文件夹已存在: {folder_path}")


    #caputre today's date and convert to a string
    today_date = datetime.now().strftime("%Y-%m-%d")

    #create the path of txt
    file_name = f"{today_date}.txt"
    file_path = os.path.join(folder_path, file_name)


        




def press_keyboard(end_time):
    try:
        # print the end time 
        print(f"程序将在{end_time}结束")
        print("请迅速切换到一个文本窗口")
        time.sleep(5) # give you 5 seconds to switch to a txt window, in future optimize to create txt 
        i=0


        while datetime.now() < end_time:

            pyautogui.typewrite("Hello World!", interval=0.5) # simulate to press keyboard
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
    create_folder_and_file()
    press_keyboard(end_time)  