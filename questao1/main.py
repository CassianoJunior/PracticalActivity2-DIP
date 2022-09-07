from PIL import Image

import functions

# laplacianLena = functions.laplacian("./images/lena_gray.bmp", "lena_gray")

# unsharpMaskingLena = functions.unsharpMasking("./images/lena_gray.bmp", "lena_gray", 1)

# highBoostedLena = functions.unsharpMasking("./images/lena_gray.bmp", "lena_gray", 2)

# prewittLena = functions.prewittEdgeDetection("./images/lena_gray.bmp", "lena_gray")

sobelLena = functions.sobelEdgeDetection("./images/lena_gray.bmp", "lena_gray")
