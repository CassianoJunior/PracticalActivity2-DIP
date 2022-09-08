from PIL import Image

import functions

kernelDilation = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
imageToDilation = Image.open("./images/dilation.png")
imageWithDilation = functions.dilation(imageToDilation, kernelDilation, (1, 1))
# imageWithDilation.show()

imageToErosion = Image.open("./images/erosion.png")
kernelErosion = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
imageWithErosion = functions.erosion(imageToErosion, kernelErosion, (1, 1))
# imageWithErosion.show()


imageOpening = functions.opening(imageToErosion, kernelErosion, (1, 1))
# imageOpening.show()

imageClosing = functions.closing(imageToDilation, kernelErosion, (1, 1))
# imageClosing.show()
