import cv2

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    color = frame

    for _ in range(2):
        color = cv2.bilateralFilter(color, 9, 75, 75)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 7)

    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 2)

    cartoon = cv2.bitwise_and(color, color, mask=edges)

    cv2.imshow('Cartoon Image', cartoon)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
