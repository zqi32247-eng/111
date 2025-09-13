import tkinter as tk
import time
import threading
import pyautogui

def start_typing():
    text = text_box.get("1.0", tk.END).strip()
    if not text:
        return
    
    def run_typing():
        countdown_label.config(text="5 秒后开始...")
        time.sleep(5)
        countdown_label.config(text="正在输入...")
        for char in text:
            pyautogui.write(char)
            time.sleep(0.08)  # 打字速度，可调整
        countdown_label.config(text="完成！")

    threading.Thread(target=run_typing, daemon=True).start()

# GUI界面
root = tk.Tk()
root.title("自动打字小工具")
root.geometry("400x300")

label = tk.Label(root, text="请输入要自动输入的文字：")
label.pack(pady=5)

text_box = tk.Text(root, height=10, width=40)
text_box.pack(pady=5)

start_button = tk.Button(root, text="开始打字", command=start_typing)
start_button.pack(pady=10)

countdown_label = tk.Label(root, text="")
countdown_label.pack()

root.mainloop()
