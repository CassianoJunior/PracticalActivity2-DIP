from PIL import Image


def union(image1, image2):
  width, height = image1.size

  unionImage = Image.new(image1.mode, image1.size)

  for line in range(width):
    for column in range(height):
      if image1.getpixel((line, column)) or image2.getpixel((line, column)):
        if image1.getpixel((line, column)):
          unionImage.putpixel((line, column), image1.getpixel((line, column)))
        else:
          unionImage.putpixel((line, column), image2.getpixel((line, column)))

  return unionImage

def intersection(image1, image2):
  width, height = image1.size

  intersectImage = Image.new(image1.mode, image1.size)

  for line in range(width):
    for column in range(height):
      value = image1.getpixel((line, column)) and image2.getpixel((line, column))
      intersectImage.putpixel((line, column), value)

  return intersectImage

def difference(image1, image2):
  return intersection(image1, complement(image2))

def complement(img):
  img = img.convert('L')
  width, height = img.size

  imageComplement = Image.new(img.mode, img.size)

  for line in range(width):
    for column in range(height):
      imageComplement.putpixel((line, column), 255 - img.getpixel((line, column)))

  return imageComplement
