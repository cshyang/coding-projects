import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

img = cv2.imread("group_photo.jpeg")
#create a grey version of the original image
grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face = face_cascade.detectMultiScale(grey_img,
scaleFactor=1.05,
minNeighbors = 5 )

for x, y, w, h in face:
    img2 = cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 3)

print(face)
cv2.imshow("image",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
OpenCV steps by steps:
1. read image
2. show image
3. define wait time and destroy window

OpenCV cascade classifier:
1. create cascade variable
2. create an object that store the (x,y) coordinates of the face detected
"""