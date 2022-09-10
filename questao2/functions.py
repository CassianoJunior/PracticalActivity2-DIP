from PIL import Image


def medianFilter(inputImg, name, windowSize = 3):
  width, height = inputImg.size

  imageWithMedianFilter = Image.new(inputImg.mode, inputImg.size)

  for line in range(1, width-1):
    for column in range(1, height-1):
      values = []
      for i in range(windowSize):
        for j in range(windowSize):
          values.append(inputImg.getpixel((line+i-1, column+j-1)))
      values.sort()
      imageWithMedianFilter.putpixel((line, column), values[4])

  imageWithMedianFilter.save(f"./images/{name}-medianFilter.png")

  return imageWithMedianFilter

def averageFilter(inputImg, name, mask, sumOfMask):
  width, height = inputImg.size

  imageWithAverageFilter = Image.new(inputImg.mode, inputImg.size)

  for line in range(1, width-1):
    for column in range(1, height-1):
      value = 0
      for i in range(mask):
        for j in range(mask[i]):
          value += inputImg.getpixel((line+i-1, column+j-1)) * mask[i][j]
      imageWithAverageFilter.putpixel((line, column), int(value/sumOfMask))

  imageWithAverageFilter.show()
  imageWithAverageFilter.save(f"./images/{name}-averageFilter{sumOfMask}.png")

  return imageWithAverageFilter
