from digitalio import DigitalInOut, Direction, Pull
import board
import RPi.GPIO as GPIO


class BonnetInput:

    def setup_buttons(self):
        buttons = {
            "L": 27,
            "R": 23,
            "U": 17,
            "D": 22,
            "C": 4,
            "A": 5,
            "B": 6
        }

        GPIO.setmode(GPIO.BCM)
        for key in buttons:
            GPIO.setup(buttons[key], GPIO.IN, pull_up_down=GPIO.PUD_UP)

        return buttons

    def __init__(self):
        self.buttons = self.setup_buttons()

    def register_callback(self, button_name, callback_func):
        GPIO.add_event_detect(
            self.buttons[button_name], GPIO.FALLING, callback=callback_func, bouncetime=800)
