import os
from pynput import mouse, keyboard


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def on_click(x, y, button, pressed):
    if pressed:
        print(f"{x}, {y}")


def on_press(key):
    # 按 F5 清屏
    if key == keyboard.Key.f5:
        clear_console()
        # print("控制台已清空")


if __name__ == "__main__":
    print("开始记录鼠标点击位置，按 F5 清空屏幕")

    keyboard_listener = keyboard.Listener(on_press=on_press)
    keyboard_listener.start()

    with mouse.Listener(on_click=on_click) as mouse_listener:
        mouse_listener.join()

    keyboard_listener.join()
