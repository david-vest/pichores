from digitalio import DigitalInOut, Direction, Pull
import board

class Input:
    A = DigitalInOut(board.D5)
    A.direction = Direction.INPUT
    A.pull = Pull.UP

    B = DigitalInOut(board.D6)
    B.direction = Direction.INPUT
    B.pull = Pull.UP

    L = DigitalInOut(board.D27)
    L.direction = Direction.INPUT
    L.pull = Pull.UP

    R = DigitalInOut(board.D23)
    R.direction = Direction.INPUT
    R.pull = Pull.UP

    U = DigitalInOut(board.D17)
    U.direction = Direction.INPUT
    U.pull = Pull.UP

    D = DigitalInOut(board.D22)
    D.direction = Direction.INPUT
    D.pull = Pull.UP

    C = DigitalInOut(board.D4)
    C.direction = Direction.INPUT
    C.pull = Pull.UP

    buttons = {
        "A": A,
        "B": B,
        "C": C,
        "LEFT": L, 
        "RIGHT": R,
        "UP": U,
        "DOWN": D,
    }

    def __init__(self):
        pass

    def get_pressed(self):
        pressed = []
        for key in buttons:
            if not key.value:
                pressed.append(key)
        return pressed