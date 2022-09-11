from PIL import Image

import functions

img1 = Image.open("./images/binaryImage1.png").convert('L')
img2 = Image.open("./images/binaryImage2.png").convert('L')

# union = functions.union("./images/binaryImage1.png", "./images/binaryImage2.png")
# union.show()
# union.save("./images/unionImage.png")

# intersect = functions.intersect("./images/binaryImage1.png", "./images/binaryImage2.png")
# intersect.show()
# intersect.save("./images/intersectImage.png")

difference = functions.difference(img1, img2)
# difference.show()
difference.save("./images/differenceImage.png")
