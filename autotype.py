import time
import pyautogui
from pypinyin import lazy_pinyin

# 标点符号集合（遇到这些就触发候选确认）
SEPARATORS = set("，。！？：；、“”‘’（）()《》〈〉【】『』—… \n\t,.!?;:\"'()[]{}-")

def main():
    text = input("请输入要自动输入的文字：\n")
    print("请在 5 秒内把光标放到目标窗口…")
    time.sleep(5)

    buffer = ""  # 拼音缓冲区
    for char in text:
        if '\u4e00' <= char <= '\u9fff':  # 中文字符
            buffer += lazy_pinyin(char)[0]
        elif char in SEPARATORS:  # 碰到分隔符
            if buffer:
                pyautogui.typewrite(buffer)  # 输出缓冲区拼音
                pyautogui.press("space")     # 确认中文
                buffer = ""
            pyautogui.typewrite(char)        # 输出标点
        else:  # 英文、数字、符号
            if buffer:
                pyautogui.typewrite(buffer)
                pyautogui.press("space")
                buffer = ""
            pyautogui.typewrite(char)
        time.sleep(0.05)  # 模拟打字速度

    # 处理最后残留的拼音
    if buffer:
        pyautogui.typewrite(buffer)
        pyautogui.press("space")

    print("输入完成！")

if __name__ == "__main__":
    main()
