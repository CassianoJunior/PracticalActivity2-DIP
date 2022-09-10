from PIL import Image

import functions

lena_gray = Image.open('./images/lena_gray.bmp').convert('L')

# laplacianLena = functions.laplacian(lena_gray, "lena_gray")

# unsharpMaskingLena = functions.unsharpMasking(lena_gray, "lena_gray", 1)

# highBoostedLena = functions.unsharpMasking(lena_gray, "lena_gray", 1.3)

prewittLena = functions.prewittEdgeDetection(lena_gray, "lena_gray")

sobelLena = functions.sobelEdgeDetection(lena_gray, "lena_gray")
