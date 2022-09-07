import functions

union = functions.union("./images/binaryImage1.png", "./images/binaryImage2.png")
# union.show()
union.save("./images/unionImage.png")

intersect = functions.intersect("./images/binaryImage1.png", "./images/binaryImage2.png")
# intersect.show()
intersect.save("./images/intersectImage.png")

difference = functions.difference("./images/binaryImage1.png", "./images/binaryImage2.png")
# difference.show()
difference.save("./images/differenceImage.png")
