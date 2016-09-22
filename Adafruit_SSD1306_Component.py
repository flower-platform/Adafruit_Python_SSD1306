
from Adafruit_SSD1306 import SSD1306_128_64
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

RST = 24
"""
A light wrapper to offer easy suport to write text on SSD1306 128*64 oled display
@flower { isComponent=true }
"""
class Adafruit_SSD1306_Component(SSD1306_128_64):
    """
    @flowerChildParameter { ref = "rst", defaultValue=24 }
    """
    def __init__(self, rst=RST):
        SSD1306_128_64.__init__(self, rst)
        # load default font
        self.font = ImageFont.load_default()

    def printText(self, x, y, text):
        self.draw.text((x, y), text,  font=self.font, fill=100)
        
    def clear(self):
        self.draw.rectangle((0,0,self.width, self.height), outline=0, fill=0)
        self.display()
   
    def clearArea(self, x, y, width, height):
        self.draw.rectangle((x,y, width, height), outline=0, fill=0)
        self.display()
    
    # method used to write to display internal buffer
    def displayChanges(self):
        self.image(self.InternImage)
        self.display()
   
    def reset(self):
        self.InternImage = Image.new('1', (self.width, self.height))
        self.draw = ImageDraw.Draw(self.InternImage)

    """
    This method delete a text from screen
    """
    def clearTextFromPosition(self, x, y, text):
        # get size of text in pixels(font dependent)
        textWidth, textHeight = self.draw.textsize(text, self.font)
        self.clearArea(x, y, x + textWidth, y + textHeight)

    def setup(self):
        self.begin()

        # Clear display.
        self.clear()
        self.display()

        self.InternImage = Image.new('1', (self.width, self.height))
        self.draw = ImageDraw.Draw(self.InternImage)

    def setTrueTypeFont(self, fontPath, fontSize):
        self.font = ImageFont.truetype(fontPath, fontSize)

    def loop(self):
        return

    def stop(self):
        return

