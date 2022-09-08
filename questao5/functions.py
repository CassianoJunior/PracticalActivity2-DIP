import os
import sys

from PIL import Image

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from questao3 import functions as setsFunctions
from questao4 import functions as morphologicalFunctions


def complement(img):
  img = img.convert('L')
  width, height = img.size

  imageComplement = Image.new(img.mode, img.size)

  for line in range(width):
    for column in range(height):
      imageComplement.putpixel((line, column), 255 - img.getpixel((line, column)))

  return imageComplement

def holeFilling(img):
  holes = detectHolesInImage(img)

  imagesToSum = []

  imageComplement = complement(img)
  kernel = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]

  for hole in holes:    
    firstImage = Image.new(img.mode, img.size, 0)
    firstImage.putpixel(hole, 255)

    while True:
      imageIterable = morphologicalFunctions.dilation(firstImage, kernel)
      imageIterable = setsFunctions.intersect(imageIterable, imageComplement)
      # imageIterable.show()
      # firstImage.show()
      if isSameImage(firstImage, imageIterable): break
      firstImage = imageIterable
    
    imagesToSum.append(setsFunctions.union(img, firstImage))

  resultImage = imagesToSum[0]
  for image in range(len(imagesToSum) - 1):
    resultImage = setsFunctions.union(resultImage, imagesToSum[image + 1])
  
  return resultImage


def isSameImage(image1, image2):
  width, height = image1.size

  difference = setsFunctions.difference(image1, image2)
  # difference.show()

  for line in range(width):
    for column in range(height):
      if difference.getpixel((line, column)) != 0:
        return False
  
  return True

def detectHolesInImage(img):
  width, height = img.size

  holes = []
  objects = []

  for line in range(width):
    for column in range(height):
      if img.getpixel((line, column)) == 0:
        if isHoleInObjectAlreadyDetected(objects, line, column):
          continue
        upHaveObjectBool, topEdge = upHaveObject(img, line, column)
        downHaveObjectBool, bottomEdge = downHaveObject(img, line, column)
        leftHaveObjectBool, leftEdge = leftHaveObject(img, line, column)
        rightHaveObjectBool, rightEdge = rightHaveObject(img, line, column)

        if (upHaveObjectBool and downHaveObjectBool and 
            leftHaveObjectBool and rightHaveObjectBool):
          objects.append({
            'topEdge': topEdge,
            'bottomEdge': bottomEdge,
            'leftEdge': leftEdge,
            'rightEdge': rightEdge
          })
          holes.append((line, column))

  return holes

def upHaveObject(img, line, column):
  xDisplacement = 0
  while line + xDisplacement >= 0:
    if img.getpixel((line + xDisplacement, column)) == 255:
      return True, line + xDisplacement
    xDisplacement -= 1
  
  return False, None

def downHaveObject(img, line, column):
  xDisplacement = 0
  while line + xDisplacement < img.width:
    if img.getpixel((line + xDisplacement, column)) == 255:
      return True, line + xDisplacement
    xDisplacement += 1
  
  return False, None

def leftHaveObject(img, line, column):
  yDisplacement = 0
  while column + yDisplacement >= 0:
    if img.getpixel((line, column + yDisplacement)) == 255:
      return True, column + yDisplacement
    yDisplacement -= 1
  
  return False, None

def rightHaveObject(img, line, column):
  yDisplacement = 0
  while column + yDisplacement < img.height:
    if img.getpixel((line, column + yDisplacement)) == 255:
      return True, column + yDisplacement
    yDisplacement += 1
  
  return False, None

def isHoleInObjectAlreadyDetected(objects, line, column):
  for object in objects:
    if line >= object['topEdge'] and line <= object['bottomEdge'] and column >= object['leftEdge'] and column <= object['rightEdge']:
      return True
  
  return False
