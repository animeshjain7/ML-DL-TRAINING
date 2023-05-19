import cv2,skimage
vid = cv2.VideoCapture(0)
while True:
    flag,img = vid.read()  #BGR
    if flag:
        gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        blue_img = cv2.subtract(img[:,:,-3],gray_img)
        th , blue_binary = cv2.threshold(blue_img,55,255,cv2.THRESH_BINARY)
        blue_binary2 = skimage.morphology.remove_small_objects(blue_binary.astype(bool),134)
        strel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(10,10))
        blue_binary3 = cv2.dilate(blue_binary2.astype('uint8'),strel,iterations=1)
        blue_binary4 = skimage.morphology.remove_small_holes(blue_binary3.astype(bool),5000)
        labels = skimage.measure.label(blue_binary4)
        rp = skimage.measure.regionprops(labels,blue_binary4)

        img_orig = img.copy()

        if len(rp)>0:
            (y1,x1,y2,x2) = rp[0].bbox
            cv2.rectangle(img_orig,pt1=(x1,y1),pt2=(x2,y2),color=(255,255,0),thickness=10)
        cv2.imshow('preview',img_orig)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
cv2.destroyAllWindows()
vid.release()