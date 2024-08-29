import pyautogui  
import time  
from datetime import datetime, timedelta  

def move_mouse(end_time):  
    try:  
        # 获取当前鼠标位置  
        x, y = pyautogui.position()  
        print(f"初始鼠标位置: ({x}, {y})")  # 输出初始鼠标位置  
        
        print(f"程序将在 {end_time} 结束")  # 输出结束时间
        i=0  
        
        while datetime.now() < end_time:  # 在当前时间小于结束时间期间循环  
            
            new_x, new_y = x - 100, y + 100  # 计算新的位置  因为vs code 的执行按钮在右上角，所以设置如此计算
            print(f"移动到新位置: ({new_x}, {new_y})")  # 输出新位置  
            pyautogui.moveTo(new_x, new_y, duration=0.5)  
            pyautogui.moveTo(new_x - 200, new_y + 200, duration=0.5)  
            pyautogui.moveTo(x, y, duration=1)  
            print(f"返回原位置: ({x}, {y})")  # 输出返回原位置  
            i += 1
            
            # 每隔 300 秒移动一次  
            time.sleep(120)  # 调整时间间隔  
            print(f"已执行{i}次")
    
    except KeyboardInterrupt:  
        print("程序已停止")  # ctrl + c 终止程序

if __name__ == "__main__":  
    # 在main函数中计算结束时间  
    end_time = datetime.now() + timedelta(hours=2)  
    move_mouse(end_time)