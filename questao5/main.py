from PIL import Image

import functions

imgQuadro = Image.open('./images/quadro.png').convert('RGB')
#Letra A
imgQuadroBinarized = Image.new('L', imgQuadro.size)

width, height = imgQuadro.size
for line in range(width):
  for column in range(height):
    imgQuadroBinarized.putpixel((line, column), 255 if imgQuadro.getpixel((line, column)) == (0, 0, 0) else 0)

imgQuadroBinarized.show()
imgQuadroFilled = functions.holeFilling(imgQuadroBinarized)
imgQuadroFilled.show()
