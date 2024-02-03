#installed easyOCR , matplotlib , pip install opencv-python-headless
# for this project
 
import cv2
import matplotlib.pyplot as plt  
import easyocr

# read image

img = cv2.imread(r"C:\Users\om\Desktop\CV\o.jpg")

# helps detect text

reader = easyocr.Reader(['en'], gpu=False)


# detect text on image

text_ = reader.readtext(img)

# print(text) , this shovvs the text but its not organized

# shovvs text in organized form 
for t in text_:
    bbox, text , score = t 

# dravv box and text
for t in text_:

    print(t)

    bbox, text , score = t 

    cv2.rectangle(img, bbox[0], bbox[2], (0,255,0),5 )

    cv2.putText(img, text, bbox[0] , cv2.FONT_HERSHEY_COMPLEX,0.7,(2555,0,0),2)


plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()