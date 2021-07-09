import argparse
import cv2

# parse arguments
pa = argparse.ArgumentParser()
pa.add_argument("-i", "--image", type=str, default="../data/Tropical-tree.jpeg",
	help="image directory")
args = vars(pa.parse_args())

# spatioal dimension of the image.
image = cv2.imread(args["image"])
(h, w) = image.shape[:2]
cv2.imshow("Original", image)

# get the bgr of image @ (0,0)
# usually images are in RGB order. However, cv2
# has it in BGR order
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

# sample the color at (30,40)
(b, g, r) = image[30, 40]
print("Pixel at (50, 20) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

# Divide the image into 4 quadrants. Find the center.
(cX, cY) = (w // 2, h // 2)

# grab the top left corder of the image
tl = image[0:cY, 0:cX]
cv2.imshow("Top-Left Corner", tl)

# grab other 3 quadrants
tr = image[0:cY, cX:w]
br = image[cY:h, cX:w]
bl = image[cY:h, 0:cX]
cv2.imshow("Top-Right Corner", tr)
cv2.imshow("Bottom-Right Corner", br)
cv2.imshow("Bottom-Left Corner", bl)

# for heck of it, change top-left quadrant to green
image[0:cY, 0:cX] = (0, 255, 0)

cv2.imshow("Manipulated Image", image)
cv2.waitKey(0)