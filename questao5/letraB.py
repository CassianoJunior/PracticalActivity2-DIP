import os
import sys
from email.mime import image

from PIL import Image

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


imgQuadro = Image.open('./images/quadro.png').convert('RGB')

imageOnlyBlackObjects = Image.new(imgQuadro.mode, imgQuadro.size)
width, height = imgQuadro.size

for line in range(width):
  for column in range(height):
    pixel = imgQuadro.getpixel((line, column))
    if pixel != (0, 0, 0):
      imageOnlyBlackObjects.putpixel((line, column), (255, 255, 255))
    else:
      imageOnlyBlackObjects.putpixel((line, column), (0, 0, 0))


# imageOnlyBlackObjects.show()
imageOnlyBlackObjects.save("./images/imageOnlyBlackObjects.png")

imageWithoutBlackObjects = Image.new(imgQuadro.mode, imgQuadro.size)
for line in range(width):
  for column in range(height):
    pixel = imgQuadro.getpixel((line, column))
    if pixel == (0, 0, 0):
      imageWithoutBlackObjects.putpixel((line, column), (255, 255, 255))
    else:
      imageWithoutBlackObjects.putpixel((line, column), pixel)
      
    
# imageWithoutBlackObjects.show()
imageWithoutBlackObjects.save("./images/imageWithoutBlackObjects.png")
