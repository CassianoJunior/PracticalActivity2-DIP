from PIL import Image


def dilation(img, kernel, pixelInterest = (1, 1)):
  img = img.convert('L')
  width, height = img.size
  xInterest, yInterest = pixelInterest

  imageWithDilation = Image.new(img.mode, img.size)

  for line in range(xInterest, width-xInterest):
    for column in range(yInterest, height-yInterest):
      if img.getpixel((line, column)) == 255:
        for kernelLine in range(len(kernel)):
          for kernelColumn in range(len(kernel[kernelLine])):
            if kernel[kernelLine][kernelColumn] == 1:
              imageWithDilation.putpixel((line + kernelLine - xInterest, column + kernelColumn - yInterest), 255)

  return imageWithDilation

def erosion(img, kernel, pixelInterest = (1, 1)):
  img = img.convert('L')
  width, height = img.size
  xInterest, yInterest = pixelInterest

  imageWithErosion = Image.new(img.mode, img.size)

  for line in range(xInterest, width-xInterest):
    for column in range(yInterest, height-yInterest):
      if img.getpixel((line, column)) == 255:
        match = True
        for kernelLine in range(len(kernel)):
          for kernelColumn in range(len(kernel[kernelLine])):
            if kernel[kernelLine][kernelColumn] == 1:
              if img.getpixel((line + kernelLine - xInterest, column + kernelColumn - yInterest)) != 255:
                match = False
                break
          if not match: break
        
        if match: imageWithErosion.putpixel((line, column), 255)

  return imageWithErosion

def opening(img, kernel, pixelInterest = (1, 1)):
  imageAfterOpening = dilation(erosion(img, kernel, pixelInterest), kernel, pixelInterest)
  return imageAfterOpening

def closing(img, kernel, pixelInterest = (1, 1)):
  imageAfterClosing = erosion(dilation(img, kernel, pixelInterest), kernel, pixelInterest)
  return imageAfterClosing
