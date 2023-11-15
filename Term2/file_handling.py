# file = open("myfile.txt", "r")
# file = open("myfile.txt", "a")
# file.write("hello")
# file.close()

# file = open("myfile.txt", "w")
# file.write("hi")
# file.close()
# import os

# if not os.path.exists("myfile.txt"):
#     file = open("myfile.txt", "x")

# from PIL import Image

# img = Image.open("icon.png")
# img.show()
# import cv2
# img = cv2.imread("icon.png")

# cv2.imshow("image",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# import matplotlib.pyplot as plt
# plt.imshow(img)

# plt.waitforbuttonpress()

import cv2

img = cv2.imread('icon.png',0)


img = cv2.Canny(img, threshold1=100, threshold2 = 100)


cv2.imshow('my pic', img)

cv2.waitKey(0)