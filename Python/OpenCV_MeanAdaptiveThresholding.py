# Mean Adaptive Thresholding
import cv2
import urllib.request
from matplotlib import pyplot as plt
import numpy as np
# Read the image

URL = 'https://cdn.vox-cdn.com/thumbor/XgYWcRTKElyDeYxS6g_lTLvzcJ4=/0x0:4465x3324/920x613/filters:focal(1876x1305:2590x2019):format(webp)/cdn.vox-cdn.com/uploads/chorus_image/image/70603994/quality_bistro_outdoor_dining.0.jpg'
URL2 = 'https://www.pennington.com/-/media/Images/Pennington2-NA/US/blog/fertilizer/8-Steps-to-Growing-a-Healthy-Indoor-Garden-Anytime/how-to-grow-a-healthy-indoor-garden-h.jpg?h=480&la=en&w=1140&hash=C383D653ABCDBA4ADD51691E599105B1597B5860'
URL3 = 'https://eurekastreetfurniture.com.au/attachments/Product/13853/CHRALBURYPUBLK.tag.0.jpg?ts=1558418584'
array = {URL,URL2,URL3}
i=0
for x in array:
    i+=1
    with urllib.request.urlopen(x) as url:
        with open('mod6ct1'+str(i)+'.jpg', 'wb') as f:
            f.write(url.read())

    image = cv2.imread('mod6ct1'+str(i)+'.jpg',cv2.IMREAD_GRAYSCALE)
    cv2.imshow("Image", image)

    blurred = cv2.GaussianBlur(image, (7, 7), 0)
    thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 21, 8)
    cv2.imshow("Mean Adaptive Thresholding", thresh)
    plt.subplot(3,2,2*i-1),plt.imshow(image),plt.title('Original_'+str(i))
    plt.subplot(3,2,2*i),plt.imshow(thresh),plt.title('adap_'+str(i))

plt.show()


cv2.waitKey(30000)