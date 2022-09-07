from PIL import Image


def laplacian(path, name):
  inputImg = Image.open(path)
  width, height = inputImg.size

  laplacianFilter = [[0, 1, 0], [1, -4, 1], [0, 1, 0]]

  laplacianImage = Image.new(inputImg.mode, inputImg.size)

  for line in range(1, width-1):
    for column in range(1, height-1):
      sum = 0
      for i in range(3):
        for j in range(3):
          sum += laplacianFilter[i][j] * inputImg.getpixel((line+i-1, column+j-1))
          laplacianImage.putpixel((line, column), sum)

  for line in range(width):
    for column in range(height):
      inputImg.putpixel((line, column), -1*laplacianImage.getpixel((line, column)) + inputImg.getpixel((line, column)))

  # inputImg.show()
  inputImg.save(f"./images/{name}-laplacian.png")

  return inputImg

def unsharpMasking(path, name, k):
  inputImg = Image.open(path)
  width, height = inputImg.size
  suavizedImage = Image.new(inputImg.mode, inputImg.size)

  averageFilter = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

  for line in range(1, width-1):
    for column in range(1, height-1):
      sum = 0
      for i in range(3):
        for j in range(3):
          sum += averageFilter[i][j] * inputImg.getpixel((line+i-1, column+j-1))
      suavizedImage.putpixel((line, column), int(sum/9))

  maskImage = Image.new(inputImg.mode, inputImg.size)

  for line in range(width):
    for column in range(height):
      maskImage.putpixel((line, column), inputImg.getpixel((line, column)) - suavizedImage.getpixel((line, column)))
  
  for line in range(width):
    for column in range(height):
      inputImg.putpixel((line, column), int(k * maskImage.getpixel((line, column)) + inputImg.getpixel((line, column))))

  # inputImg.show()
  if k == 1:
    inputImg.save(f"./images/{name}-unsharpMasking.png")
  else: 
    inputImg.save(f"./images/{name}-highBoosted-k={k}.png")

  return inputImg

def prewittEdgeDetection(path, name):
  inputImg = Image.open(path)
  width, height = inputImg.size

  prewittFilterX = [[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]
  prewittFilterY = [[-1, -1, -1], [0, 0, 0], [1, 1, 1]]

  prewittImage = Image.new(inputImg.mode, inputImg.size)

  for line in range(1, width-1):
    for column in range(1, height-1):
      sumX = 0
      sumY = 0
      for i in range(3):
        for j in range(3):
          sumX += prewittFilterX[i][j] * inputImg.getpixel((line+i-1, column+j-1))
          sumY += prewittFilterY[i][j] * inputImg.getpixel((line+i-1, column+j-1))
      prewittImage.putpixel((line, column), int((sumX**2 + sumY**2)**(1/2)))

  for line in range(width):
    for column in range(height):
      inputImg.putpixel((line, column), prewittImage.getpixel((line, column)))

  # inputImg.show()
  inputImg.save(f"./images/{name}-prewittEdgeDetection.png")

  return inputImg

def sobelEdgeDetection(path, name):
  inputImg = Image.open(path)
  width, height = inputImg.size

  sobelFilterX = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
  sobelFilterY = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]

  sobelImage = Image.new(inputImg.mode, inputImg.size)

  for line in range(1, width-1):
    for column in range(1, height-1):
      sumX = 0
      sumY = 0
      for i in range(3):
        for j in range(3):
          sumX += sobelFilterX[i][j] * inputImg.getpixel((line+i-1, column+j-1))
          sumY += sobelFilterY[i][j] * inputImg.getpixel((line+i-1, column+j-1))
      sobelImage.putpixel((line, column), int((sumX**2 + sumY**2)**(1/2)))

  for line in range(width):
    for column in range(height):
      inputImg.putpixel((line, column), sobelImage.getpixel((line, column)))

  # inputImg.show()
  inputImg.save(f"./images/{name}-sobelEdgeDetection.png")

  return inputImg
  
# def getMinMax(inputMatrix):
#   minValue = 0
#   maxValue = 0
#   for i in range(len(inputMatrix)):
#     for j in range(len(inputMatrix[i])):
#       if i == j and i == 0:
#         minValue = inputMatrix[i][j]
#         maxValue = inputMatrix[i][j]
      
#       if inputMatrix[i][j] < minValue:
#         minValue = inputMatrix[i][j]
      
#       if inputMatrix[i][j] > maxValue:
#         maxValue = inputMatrix[i][j]
  
#   return minValue, maxValue

# def getImageMinMax(inputPixels, width, height):
#   minValue = 0
#   maxValue = 0
  
#   for i in range(width):
#     for j in range(height):
#       if i == j and i == 0:
#         minValue = inputPixels[i, j]
#         maxValue = inputPixels[i, j]
      
#       if inputPixels[i, j] < minValue:
#         minValue = inputPixels[i, j]
      
#       if inputPixels[i, j] > maxValue:
#         maxValue = inputPixels[i, j]

#   return minValue, maxValue
