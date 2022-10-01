import cv2
import pytesseract

# Read image
path = "images/img.png"
img = cv2.imread(path)

text = pytesseract.image_to_string(img)
print(text)
