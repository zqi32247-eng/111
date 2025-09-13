import time
import pyautogui
from pypinyin import lazy_pinyin
import tkinter as tk
from tkinter import simpledialog

# 标点符号集合
SEPARATORS = set("，。！？：；、“”‘’（）()《》〈〉【】『』—… \n\t,.!?;:\"'()[]{}-")

def get_text_from_user():
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    text = simpledialog.askstring("自动打字", "请输入要自动输入的文字：")
    root.destroy()
    return text

def main():
    text = get_text_from_user()
    if not text:
        return

    print("请在 5 秒内把光标放到目标窗口…")
    time.sleep(5)

    buffer = ""  # 拼音缓冲区
    for char in text:
        if '\u4e00' <= char <= '\u9fff':  # 中文字符
            buffer += lazy_pinyin(char)[0]
        elif char in SEPARATORS:  # 碰到分隔符
            if buffer:
                pyautogui.typewrite(buffer)
                pyautogui.press("space")
                buffer = ""
            pyautogui.typewrite(char)
        else:  # 英文、数字、符号
            if buffer:
                pyautogui.typewrite(buffer)
                pyautogui.press("space")
                buffer = ""
            pyautogui.typewrite(char)
        time.sleep(0.05)

    if buffer:
        pyautogui.typewrite(buffer)
        pyautogui.press("space")

    print("输入完成！")

if __name__ == "__main__":
    main()
