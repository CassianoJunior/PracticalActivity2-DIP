import os
import sys

from PIL import Image

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from questao3 import functions as setsFunctions
from questao4 import functions as morphologicalFunctions

import functions

imgQuadro = Image.open('./images/quadro.png').convert('RGB')

imgQuadroBinarized = functions.binarizeImage(imgQuadro, (0, 0, 0))

width, height = imgQuadro.size

imgQuadroBinarized.show()
kernel = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
imgClosed = morphologicalFunctions.closing(imgQuadroBinarized, kernel, (2, 2))
imgFilledHolesOnBlackObjects = functions.complement(imgClosed)

# imgFilledHolesOnBlackObjects.save("./images/imgFilledHolesOnBlackObjects.png")
imgWithoutBlackHoles = Image.new(imgQuadro.mode, imgQuadro.size)
for line in range(width):
  for column in range(height):
    if (imgQuadro.getpixel((line, column)) == (255, 255, 255) 
        and imgFilledHolesOnBlackObjects.getpixel((line, column)) == 0):
      imgWithoutBlackHoles.putpixel((line, column), 0)
    else:
      imgWithoutBlackHoles.putpixel((line, column), imgQuadro.getpixel((line, column)))

# imgWithoutBlackHoles.save("./images/imgWithoutBlackHoles.png")

