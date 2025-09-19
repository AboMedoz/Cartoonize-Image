import cv2


class CartoonImage:
    def __init__(self):
        pass

    def cartoonize_img(self):
        cap = cv2.VideoCapture(0)

        while True:
            _, frame = cap.read()

            color = frame

            for _ in range(2):
                color = cv2.bilateralFilter(color, 9, 75, 75)

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray = cv2.medianBlur(gray, 7)

            edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9
                                          , 2)

            cartoon = cv2.bitwise_and(color, color, mask=edges)

            _, buffer = cv2.imencode( '.jpg', cartoon)
            cartoon = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + cartoon + b'\r\n')