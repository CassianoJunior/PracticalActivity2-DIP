from PIL import Image

import functions

laplacianLena = functions.laplacian("../lena_gray.bmp", "lena_gray")

unsharpMaskingLena = functions.unsharpMasking("../lena_gray.bmp", "lena_gray", 1)

highBoostedLena = functions.unsharpMasking("../lena_gray.bmp", "lena_gray", 1.5)
