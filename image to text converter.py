import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img = cv2.imread(r'sample1.jpg')
#image= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow('im',image)
print(pytesseract.image_to_string(img))
# OR explicit beforehand converting
#print(pytesseract.image_to_string(Image.fromarray(img))
