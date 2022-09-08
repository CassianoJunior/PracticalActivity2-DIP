from PIL import Image

from questao4 import functions as morphologicalFunctions
from questao5 import functions as holeFillingFunctions

img = Image.new('L', (5, 5))

matriz = [
  [255, 255, 255, 255, 255],
  [255, 0, 0, 0, 255],
  [255, 0, 0, 0, 255], 
  [255, 0, 0, 0, 255],
  [255, 255, 255, 255, 255]
]

for line in range(img.width):
  for column in range(img.height):
    img.putpixel((line, column), matriz[column][line])


# imgDilation = functions.dilation(img, [[0, 1, 0], [1, 1, 1], [0, 1, 0]])
# imgDilation.show()
# img.show()

imgFilled = holeFillingFunctions.holeFilling(img)
imgFilled.show()
