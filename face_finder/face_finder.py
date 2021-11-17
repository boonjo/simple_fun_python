import cv2
import os

image = cv2.imread("saka_smithrowe.jpg")

# Make a copy to prevent any changes to the original image
color_img = image.copy()

filename = os.path.basename("saka_smithrowe.jpg")

# OpenCV works best with gray images
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Use OpenCV's built in Haar classifier
haar_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')

faces = haar_classifier.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5)
print('Number of faces found: {faces}'.format(faces=len(faces)))

for (x, y, width, height) in faces:
    cv2.rectangle(color_img, (x, y), (x+width, y+height), (0, 255, 0), 2)
    
# Show the faces found
cv2.imshow(filename, color_img)
cv2.waitKey(0)
cv2.destroyAllWindows()