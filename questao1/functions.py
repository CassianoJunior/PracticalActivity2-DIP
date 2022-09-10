from PIL import Image


def laplacian(inputImg, name):
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

  laplacianImage.show()

  for line in range(width):
    for column in range(height):
      inputImg.putpixel((line, column), -1*laplacianImage.getpixel((line, column)) + inputImg.getpixel((line, column)))

  # inputImg.show()
  inputImg.save(f"./images/{name}-laplacian.png")

  return inputImg

def unsharpMasking(inputImg, name, k):
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
  # suavizedImage.show()

  maskImage = Image.new(inputImg.mode, inputImg.size)

  for line in range(width):
    for column in range(height):
      maskImage.putpixel((line, column), inputImg.getpixel((line, column)) - suavizedImage.getpixel((line, column)))
  
  # maskImage.show()

  for line in range(width):
    for column in range(height):
      inputImg.putpixel((line, column), int(k * maskImage.getpixel((line, column)) + inputImg.getpixel((line, column))))

  # inputImg.show()
  if k == 1:
    inputImg.save(f"./images/{name}-unsharpMasking.png")
  else: 
    inputImg.save(f"./images/{name}-highBoosted-k={k}.png")

  return inputImg

def prewittEdgeDetection(inputImg, name):
  width, height = inputImg.size

  prewittFilterX = [[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]
  prewittFilterY = [[-1, -1, -1], [0, 0, 0], [1, 1, 1]]

  prewittImage = Image.new(inputImg.mode, inputImg.size)
  prewittImageX = Image.new(inputImg.mode, inputImg.size)
  prewittImageY = Image.new(inputImg.mode, inputImg.size)

  for line in range(1, width-1):
    for column in range(1, height-1):
      sumX = 0
      sumY = 0
      for i in range(3):
        for j in range(3):
          sumX += prewittFilterX[i][j] * inputImg.getpixel((line+i-1, column+j-1))
          sumY += prewittFilterY[i][j] * inputImg.getpixel((line+i-1, column+j-1))
      prewittImageX.putpixel((line, column), sumX)
      prewittImageY.putpixel((line, column), sumY)
      prewittImage.putpixel((line, column), int((sumX**2 + sumY**2)**(1/2)))

  # inputImg.show()
  prewittImageX.save(f"./images/{name}-prewittEdgeDetection-XEdges.png")
  prewittImageY.save(f"./images/{name}-prewittEdgeDetection-YEdges.png")
  prewittImage.save(f"./images/{name}-prewittEdgeDetection.png")

  return prewittImage, prewittImageX, prewittImageY

def sobelEdgeDetection(inputImg, name):
  width, height = inputImg.size

  sobelFilterX = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
  sobelFilterY = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]

  sobelImage = Image.new(inputImg.mode, inputImg.size)
  sobelImageX = Image.new(inputImg.mode, inputImg.size)
  sobelImageY = Image.new(inputImg.mode, inputImg.size)

  for line in range(1, width-1):
    for column in range(1, height-1):
      sumX = 0
      sumY = 0
      for i in range(3):
        for j in range(3):
          sumX += sobelFilterX[i][j] * inputImg.getpixel((line+i-1, column+j-1))
          sumY += sobelFilterY[i][j] * inputImg.getpixel((line+i-1, column+j-1))
      sobelImageX.putpixel((line, column), sumX)
      sobelImageY.putpixel((line, column), sumY)
      sobelImage.putpixel((line, column), int((sumX**2 + sumY**2)**(1/2)))


  # inputImg.show()
  sobelImageX.save(f"./images/{name}-sobelEdgeDetection-XEdges.png")
  sobelImageY.save(f"./images/{name}-sobelEdgeDetection-YEdges.png")
  sobelImage.save(f"./images/{name}-sobelEdgeDetection.png")

  return sobelImage, sobelImageX, sobelImageY
 