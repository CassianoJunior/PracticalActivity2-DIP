import functions

lenaWithMedianFilter = functions.medianFilter("./images/lena_ruido.bmp", "lena_ruido")

mask5 = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
lenaWithAverageFilter5 = functions.averageFilter("./images/lena_ruido.bmp", "lena_ruido", mask5, 5)

mask9 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
lenaWithAverageFilter9 = functions.averageFilter("./images/lena_ruido.bmp", "lena_ruido", mask9, 9)

mask32 = [[1, 3, 1], [3, 16, 3], [1, 3, 1]]
lenaWithAverageFilter32 = functions.averageFilter("./images/lena_ruido.bmp", "lena_ruido", mask32, 32)

mask8 = [[0, 1, 0], [1, 4, 1], [0, 1, 0]]
lenaWithAverageFilter8 = functions.averageFilter("./images/lena_ruido.bmp", "lena_ruido", mask8, 8)
