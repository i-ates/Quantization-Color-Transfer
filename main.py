import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('1.png', 0)

ditheridImg = np.copy(img)

q = 64
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        ditheridImg[i][j] = round(img[i][j] / q) * q

floydImg = np.copy(img)

for y in range(ditheridImg.shape[1]-1):
    for x in range(ditheridImg.shape[0]-1):
        oldPixel = floydImg[x][y]
        newPixel = round(oldPixel / q) * q
        floydImg[x][y] = newPixel
        quantErr = oldPixel - newPixel
        floydImg[x + 1][y] = floydImg[x + 1][y] + quantErr *7 / 16
        floydImg[x - 1][y + 1] = floydImg[x - 1][y + 1] + quantErr *3 / 16
        floydImg[x][y + 1] = floydImg[x][y + 1] + quantErr *5 / 16
        floydImg[x + 1][y + 1] = floydImg[x + 1][y + 1] + quantErr *1 / 16

# show image
print("hi")
cv2.imwrite('quantized.png', ditheridImg)
cv2.imwrite('floydImg.png', floydImg)
