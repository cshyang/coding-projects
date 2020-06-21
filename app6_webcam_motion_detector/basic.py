import cv2
import os

def resize(folder_name):

    for i in os.listdir(folder_name):
        if i.endswith(".jpg") or i.endswith(".png"):
            img = cv2.imread(folder_name + "/" + i, 0)
            resized_img = cv2.resize( img, ( int(img.shape[1]/2), int(img.shape[0]/2)) )
            cv2.imshow('myImage',resized_img)
            cv2.waitKey(2000)
            cv2.imwrite( i.split(".")[0] + "_resized"+ ".jpeg", resized_img)
        else:
            continue

    cv2.destroyAllWindows()

resize("cv2_images")
