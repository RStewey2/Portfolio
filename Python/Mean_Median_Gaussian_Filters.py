import cv2
import urllib.request
from matplotlib import pyplot as plt
# Read the image

URL = 'https://www.math.cuhk.edu.hk/~rchan/paper/chn/50percentnoise_files/image005.jpg'

with urllib.request.urlopen(URL) as url:
    with open('mod4ct1.jpg', 'wb') as f:
        f.write(url.read())

img = cv2.imread('mod4ct1.jpg')
cv2.imshow("original",img)


mean_3 = cv2.blur(img,(3,3))
median_3 = cv2.medianBlur(img,3)
gaus_3_0=cv2.GaussianBlur(img,(3,3),0)
gaus_3_2=cv2.GaussianBlur(img,(3,3),15)
mean_5 = cv2.blur(img,(5,5))
median_5 = cv2.medianBlur(img,5)
gaus_5_0=cv2.GaussianBlur(img,(5,5),0)
gaus_5_2=cv2.GaussianBlur(img,(5,5),15)
mean_7 = cv2.blur(img,(7,7))
median_7 = cv2.medianBlur(img,7)
gaus_7_0=cv2.GaussianBlur(img,(7,7),0)
gaus_7_2=cv2.GaussianBlur(img,(7,7),15)

plt.subplot(3,4,1),plt.imshow(mean_3),plt.title('Mean')
plt.subplot(342),plt.imshow(median_3),plt.title('Median')
plt.subplot(343),plt.imshow(gaus_3_0),plt.title('Gauss_0')
plt.subplot(344),plt.imshow(gaus_3_2),plt.title('Gauss_2')
plt.subplot(345),plt.imshow(mean_3),plt.title('Mean')
plt.subplot(346),plt.imshow(median_3),plt.title('Median')
plt.subplot(347),plt.imshow(gaus_3_0),plt.title('Gauss_0')
plt.subplot(348),plt.imshow(gaus_3_2),plt.title('Gauss_2')
plt.subplot(349),plt.imshow(mean_3),plt.title('Mean')
plt.subplot(3,4,10),plt.imshow(median_3),plt.title('Median')
plt.subplot(3,4,11),plt.imshow(gaus_3_0),plt.title('Gauss_0')
plt.subplot(3,4,12),plt.imshow(gaus_3_2),plt.title('Gauss_2')
plt.show()


cv2.waitKey(30000)