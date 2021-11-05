import asyncio
import buttons
import board
import busio
from digitalio import DigitalInOut, Direction, Pull
from PIL import Image, ImageDraw
import adafruit_ssd1306


def main():
    loop = asyncio.get_event_loop()

    i2c = busio.I2C(board.SCL, board.SDA)
    oled = adafruit_ssd1306.I2C(128, 64, i2c)
    
    buttons = BonnetInput()

    






if __name__ == '__main__':
    main()