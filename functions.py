from PIL import Image


def laplacian(path, name):
  inputImg = Image.open(path)
  pixelsMatrix = inputImg.load()
  copyImage = inputImg.copy()
  width = inputImg.width
  height = inputImg.height

  laplacianFilter = [[0, 1, 0], [1, -4, 1], [0, 1, 0]]
  laplacianValuesMatrix = [[0]*width]*height

  for line in range(1, width-1):
    for column in range(1, height-1):
      sum = 0
      for i in range(3):
        for j in range(3):
          sum += laplacianFilter[i][j] * pixelsMatrix[line+i-1, column+j-1]
          inputImg.putpixel((line, column), sum)
      
      laplacianValuesMatrix[line][column] = int(sum)

  pixelsMatrixWithLaplacian = inputImg.load()

  for line in range(width):
    for column in range(height):
      inputImg.putpixel((line, column), -1*pixelsMatrixWithLaplacian[line, column] + pixelsMatrix[line, column])

  # inputImg.show()
  inputImg.save(f"./images/{name}-laplacian.png")

  return inputImg

def unsharpMasking(path, name, k):
  inputImg = Image.open(path)
  pixelsMatrix = inputImg.load()
  width = inputImg.width
  height = inputImg.height
  suavizedPixelsMatrix = [[0]*width]*height

  medianFilter = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

  for line in range(1, width-1):
    for column in range(1, height-1):
      sum = 0
      for i in range(3):
        for j in range(3):
          sum += medianFilter[i][j] * pixelsMatrix[line+i-1, column+j-1]
      suavizedPixelsMatrix[line][column] = int(sum/9)
  
  mask = [[0]*width]*height

  for line in range(width):
    for column in range(height):
      mask[line][column] =  pixelsMatrix[line, column] - suavizedPixelsMatrix[line][column]
  
  for line in range(width):
    for column in range(height):
      inputImg.putpixel((line, column), int(k * mask[line][column] + pixelsMatrix[line, column]))

  # inputImg.show()
  inputImg.save(f"./images/{name}-unsharpMasking.png")

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
