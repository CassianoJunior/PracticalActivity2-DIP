
import os
import sys
from turtle import width

from PIL import Image

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from questao3 import functions as setsFunctions
from questao4 import functions as morphologicalFunctions

import functions

imgQuadro = Image.open('./images/quadro.png').convert('RGB')
width, height = imgQuadro.size

imgQuadroBinarizedGreen = functions.binarizeImage(imgQuadro, (0, 255, 0))
imgQuadroBinarizedBlue = functions.binarizeImage(imgQuadro, (0, 0, 255))
imgQuadroBinarizedYellow = functions.binarizeImage(imgQuadro, (255, 255, 0))

# imgQuadroBinarizedGreen.show()
imgQuadroBinarizedBlue.show()
# imgQuadroBinarizedYellow.show()

# imgQuadroGreenFilled = functions.holeFilling(imgQuadroBinarizedGreen)
imgQuadroBlueFilled = functions.holeFilling(imgQuadroBinarizedBlue)
# imgQuadroYellowFilled = functions.holeFilling(imgQuadroBinarizedYellow)

# imgQuadroGreenFilled.show()
imgQuadroBlueFilled.show()
# imgQuadroYellowFilled.show()

# imgQuadroGreenFilledColor = functions.colorObject(imgQuadroGreenFilled, (0, 255, 0), (255, 255, 255))
# imgQuadroGreenFilledColor.save("./images/yellowObjectFilled.png")
# imgQuadroBlueFilledColor = functions.colorObject(imgQuadroBlueFilled, (0, 0, 255), (255, 255, 255))
# imgQuadroBlueFilledColor.save("./images/blueObjectFilled.png")
# imgQuadroYellowFilledColor = functions.colorObject(imgQuadroYellowFilled, (255, 255, 0), (255, 255, 255))
# imgQuadroYellowFilledColor.save("./images/greenObjectFilled.png")




