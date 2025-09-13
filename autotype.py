import time
import pyperclip
import pyautogui

def main():
    text = input("请输入要自动输入的文字：\n")
    print("请在 5 秒内把光标放到目标窗口…")
    time.sleep(5)

    # 把文字复制到剪贴板
    pyperclip.copy(text)

    # 模拟 Ctrl+V 粘贴
    pyautogui.hotkey("ctrl", "v")

    print("输入完成！")

if __name__ == "__main__":
    main()
