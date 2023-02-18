import cv2
import numpy as np

img = cv2.imread(r"C:\Users\moman\OneDrive\Desktop\task\last\mask\3.png", 0)
img = cv2.resize(img, (img.shape[1]//3, img.shape[0]//3), interpolation=cv2.INTER_CUBIC)
cv2.imshow("sss", img*50)


circle_class = np.uint8((img ==1) *255)
circle_class = cv2.erode(circle_class, (3,3), iterations=5)
circle_contours, _ = cv2.findContours(circle_class, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print("Number of circles found = " + str(len(circle_contours)))


cross_class = np.uint8((img ==2) *255)
cross_class = cv2.erode(cross_class, (3,3), iterations=5)
cross_contours, _ = cv2.findContours(cross_class, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print("Number of crosses found = " + str(len(cross_contours)))


square_class = np.uint8((img ==3) *255)
square_class = cv2.erode(square_class, (3,3), iterations=5)
square_contours, _ = cv2.findContours(square_class, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print("Number of squares found = " + str(len(square_contours)))


triangle_class = np.uint8((img ==4) *255)
triangle_class = cv2.erode(triangle_class, (3,3), iterations=5)
triangle_contours, _ = cv2.findContours(triangle_class, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print("Number of triangles found = " + str(len(triangle_contours)))

output_value = len(circle_contours)*20 + len(cross_contours)*5 + len(square_contours)*15 + len(triangle_contours)*10
print("Output Value : " + str(output_value))

cv2.imshow("Circles", circle_class)
cv2.imshow("Crosses", cross_class)
cv2.imshow("Squares", square_class)
cv2.imshow("Triangles", triangle_class)




cv2.waitKey(0)