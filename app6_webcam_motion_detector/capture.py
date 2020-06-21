import cv2, time
import numpy as np
from _datetime import datetime
import pandas as pd

first_frame = None
status_list = [None]
start_times = []
end_times = []

video = cv2.VideoCapture(0)
time.sleep(1)


while True:
    check, frame = video.read()
    status = 0
    grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    grey_frame = cv2.GaussianBlur(grey_frame, (21,21),0)

    if first_frame is None:
        first_frame = grey_frame
        continue

    delta_frame = cv2.absdiff(first_frame, grey_frame)

    #create a threshold frame that contract between static image and moving object, moving object will be highlighted in white
    thresh_frame = cv2.threshold(delta_frame, 50, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations = 2)

    #contour is the area of the distinct objects having same color or intensity
    (contours,_) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    #only detect contour with greater than 20,000 pixels
    for contour in contours:
        if cv2.contourArea(contour) < 50000:
            continue

        status = 1
        (x,y,w,h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)

    status_list.append(status)
    cv2.imshow('Delta Frame', delta_frame)
    cv2.imshow('Threshold Frame', thresh_frame)
    cv2.imshow('Color Frame', frame)

    #check the item in the list, capture when 0 to 1 as start_time and and 1 to 0 as end_time
    if status_list[-1] == 1 and status_list[-2] == 0:
        start_times.append(datetime.now())
    if status_list[-1] == 0 and status_list[-2] == 1:
        end_times.append(datetime.now())

    if cv2.waitKey(20) & 0xFF == ord('q'):
        if status == 1:
            end_times.append(datetime.now())
        break

video.release()
cv2.destroyAllWindows()

start_end_time = list(zip(start_times, end_times))
df = pd.DataFrame(start_end_time, columns=['Start', 'End'])
print(df)

