""" displayer """
import framebuf
from pololu_3pi_2040_robot import robot

class Displayer:
    """ displayer class """
    def __init__(self):
        self.display = robot.Display()

    def show(self, text: str):
        """ draw function """
        self.display.fill(0)
        self.display.text(text, 0, 0, 1)
        self.display.show()

    def text(self, text:str):
        """ Draws text at 2x size (16x16 pixels per character). """
        # 1. Create a small buffer for the standard 8x8 text
        # Width = 8 pixels per char * number of chars
        # Height = 8 pixels
        self.display.fill(0)
        buf_w = len(text) * 8
        buf_h = 8
        buffer = bytearray(buf_w * buf_h // 8)
        fb_temp = framebuf.FrameBuffer(buffer, buf_w, buf_h, framebuf.MONO_HLSB)

        # 2. Write standard text to this temporary buffer
        fb_temp.text(text, 0, 0, 1)

        # 3. Manually draw pixels 2x scaled to the main display
        # We iterate over every pixel in the temp buffer
        for col in range(buf_h):
            for row in range(buf_w):
                if fb_temp.pixel(row, col):
                    # If pixel is set, draw a 2x2 block on the main display
                    self.display.fill_rect(row * 2, col * 2, 2, 2, 1)
        self.display.show()