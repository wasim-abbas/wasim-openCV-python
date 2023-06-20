import cv2

# for import and read image
img = cv2.imread("Resources/lena.png")  # read  image 0 for grayscale, 1 for color
cv2.imshow("output", img)
cv2.waitKey(0)

# # //// for import and read video
cap = cv2.VideoCapture("Resources/car.mp4")  # read video
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # press q to quit
        break

# # //// for import and read webcam
cap = cv2.VideoCapture(0)  # read webcam
cap.set(3, 640)  # set width
cap.set(4, 480)  # set height
cap.set(10, 100)  # set brightness

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # press q to quit
        break


