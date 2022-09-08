from PIL import Image


def union(image1, image2):
  width, height = image1.size

  unionImage = Image.new(image1.mode, image1.size)

  for line in range(width):
    for column in range(height):
      value = image1.getpixel((line, column)) or image2.getpixel((line, column))
      unionImage.putpixel((line, column), value)

  return unionImage

def intersect(image1, image2):
  width, height = image1.size

  intersectImage = Image.new(image1.mode, image1.size)

  for line in range(width):
    for column in range(height):
      value = image1.getpixel((line, column)) and image2.getpixel((line, column))
      intersectImage.putpixel((line, column), value)

  return intersectImage

def difference(image1, image2):
  width, height = image1.size

  differenceImage = Image.new(image1.mode, image1.size)

  for line in range(width):
    for column in range(height):
      value = image1.getpixel((line, column)) - image2.getpixel((line, column))
      differenceImage.putpixel((line, column), abs(value))

  return differenceImage
