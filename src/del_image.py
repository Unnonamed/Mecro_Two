import cv2

image = cv2.imread('sample.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

close_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15,3))
close = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, close_kernel, iterations=1)

dilate_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,3))
dilate = cv2.dilate(close, dilate_kernel, iterations=1)

cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]

for c in cnts:
    area = cv2.contourArea(c)
    if area > 800 and area < 15000:
        x,y,w,h = cv2.boundingRect(c) 
        cv2.rectangle(image, (x, y), (x + w, y + h), (222,228,251), -1)

cv2.imshow('image', thresh)
cv2.waitKey()