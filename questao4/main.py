from PIL import Image

import functions

kernelDilation = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
image = Image.open("./images/erosion.png")
imageWithDilation = functions.dilation(image, kernelDilation, (1, 1))
imageWithDilation.save('./images/imageDilated.png')

kernelErosion = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
imageWithErosion = functions.erosion(image, kernelErosion, (1, 1))
# imageWithErosion.show()

imageWithErosion.save('./images/imageEroded.png')

imageOpening = functions.opening(image, kernelErosion, (1, 1))
# imageOpening.show()

imageClosing = functions.closing(image, kernelErosion, (1, 1))
# imageClosing.show()
