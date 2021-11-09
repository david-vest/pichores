import asyncio
import os
import board
import importlib
import busio
from buttons import BonnetInput
import buttons
from digitalio import DigitalInOut, Direction, Pull
from PIL import Image, ImageDraw
import adafruit_ssd1306
from ui.windowcontroller import WindowController
from windows import *


def main():
    loop = asyncio.get_event_loop()

    i2c = busio.I2C(board.SCL, board.SDA)
    oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)
    
    buttons = BonnetInput()

    window_controller = WindowController(loop, oled)

    # for file_name in os.listdir("windows"):
    #     if file_name.endswith(".py"):
    #         windowid = file_name[:-3]
    #         module = importlib.import_module(f"windows.{windowid}")
    #         windowclass = getattr(module, windowid.capitalize())
    #         window = windowclass(window_controller)
    #         window_controller.add_window(windowid, window)
    
    # window_controller.set_window("start")

    oled.fill(0)
    oled.show()

    width = oled.width
    height = oled.height

    image = Image.new("1", (width, height))
    draw = ImageDraw.Draw(image)
    
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    buttons.register_callback("A", a_pressed(draw))
    
    loop.run_forever()

def a_pressed(draw):
    draw.polygon([(20, 20), (30, 2), (40, 20)], outline=255, fill=1)

if __name__ == '__main__':
    main()