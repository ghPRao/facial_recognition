# To run from the project directory: 
# python src/fr_load_mage.py -- image data/Tropical-tree.jpeg
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="Image path")

args = vars(ap.parse_args())

# load the image from disk using "cv2.imread" 
image = cv2.imread(args["image"])
(h, w, c) = image.shape[:3]

# display the image width, height, and number of channels
print("width: {} pixels".format(w))
print("height: {}  pixels".format(h))
print("channels: {}".format(c))

# show the image and wait for a keypress
cv2.imshow("Image", image)
cv2.waitKey(0)

# save the image back to disk (OpenCV handles converting image filetypes automatically)
cv2.imwrite("newimage.jpg", image)
