# Russian LicensePlate Detection
import cv2
from cv2 import data
import urllib.request
from matplotlib import pyplot as plt
import numpy as np
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

carplate_haar_cascade = cv2.CascadeClassifier(data.haarcascades + 'haarcascade_russian_plate_number.xml')

def carplate_detect(image):
    carplate_overlay = image.copy() 
    carplate_rects = carplate_haar_cascade.detectMultiScale(carplate_overlay,scaleFactor=1.1, minNeighbors=3)
    for x,y,w,h in carplate_rects: 
        cv2.rectangle(carplate_overlay, (x,y), (x+w,y+h), (100,0,0), 5) 
    return carplate_overlay

def carplate_extract(image):
    
    carplate_rects = carplate_haar_cascade.detectMultiScale(image,scaleFactor=1.1, minNeighbors=5)
    for x,y,w,h in carplate_rects: 
        carplate_img = image[y+15:y+h-10 ,x+15:x+w-20] # Adjusted to extract specific region of interest i.e. car license plate   
    return carplate_img

def enlarge_img(image, scale_percent):
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized_image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    return resized_image

URL = 'http://www.olavsplates.com/foto_r/rus_o004oc777.jpg'
URL2 = 'https://qph.fs.quoracdn.net/main-qimg-a73dc3a311099274cd4158c969f9e02e'
URL3 = 'https://cdn.bmwblog.com/wp-content/uploads/2020/06/BMW-4-Series-Coupe-license-plate-03.jpg'
array = {URL, URL2, URL3}
i=0
for x in array:
    i+=1
    with urllib.request.urlopen(x) as url:
        with open('mod8ct1'+str(i)+'.jpg', 'wb') as f:
            f.write(url.read())

    carplate_img = cv2.imread('mod8ct1'+str(i)+'.jpg')
    carplate_img_rgb = cv2.cvtColor(carplate_img, cv2.COLOR_BGR2RGB)
    # plt.imshow(carplate_img_rgb)

    detected_carplate_img = carplate_detect(carplate_img_rgb)
    # plt.imshow(detected_carplate_img)

    # Display extracted car license plate image
    carplate_extract_img = carplate_extract(carplate_img_rgb)
    carplate_extract_img = enlarge_img(carplate_extract_img, 150)
    # plt.imshow(carplate_extract_img)

    # Convert image to grayscale
    carplate_extract_img_gray = cv2.cvtColor(carplate_extract_img, cv2.IMREAD_GRAYSCALE)

    carplate_extract_img_gray_blur = cv2.medianBlur(carplate_extract_img_gray,3)


    plt.axis('off')

    plt.subplot(3,2,2*i-1),plt.imshow(detected_carplate_img),plt.title('Original_'+str(i))
    plt.subplot(3,2,2*i),plt.imshow(carplate_extract_img_gray),plt.title('lic_'+str(i)+': '+pytesseract.image_to_string(carplate_extract_img_gray_blur, config = f'--psm 8 --oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'))

plt.show()


cv2.waitKey(30000)