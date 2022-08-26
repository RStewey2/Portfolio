import cv2
import urllib.request
# Read the image

URL = 'https://frostlor-cdn-prod.courses.csuglobal.edu/lor/resources/src/89f79919-379b-3a8f-997a-98f3dd1d3a8a/shutterstock215592034--250.jpg'

with urllib.request.urlopen(URL) as url:
    with open('puppy.jpg', 'wb') as f:
        f.write(url.read())

image = cv2.imread('puppy.jpg',cv2.IMREAD_COLOR)

# Split the image
b,g,r = cv2.split(image)

# Show the original and all three channels 
cv2.imshow("original",image)
cv2.imshow("blue",b)
cv2.imshow("green",g)
cv2.imshow("red",r)

# Merge the channels back together
merged = cv2.merge([b,g,r])
cv2.imshow("merged",merged)

# Merge the image with red and blue swapped
swap_merged = cv2.merge([r,g,b])
cv2.imshow("swap_merged",swap_merged)

cv2.waitKey(30000)
