import numpy as np
import cv2
import cv2.cv as cv


def main():
    cap = cv2.VideoCapture(0)

    while True:
        value = 0
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (5, 5), 2)

        # Perform some stuff
        circles = cv2.HoughCircles(gray, cv.CV_HOUGH_GRADIENT, 2, 70, param1=70, param2=50, minRadius=45, maxRadius=80)
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            # draw the outer circle
            cv2.circle(frame, (i[0], i[1]), i[2], (0, 255, 0), 2)
            # draw the center of the circle
            cv2.circle(frame, (i[0], i[1]), 2, (0, 0, 255), 3)

            if i[2] >= 68:
                value += 25
            if 60 <= i[2] <= 67:
                value += 5
            if 54 <= i[2] <= 59:
                value += 1
            if 40 <= i[2] <= 53:
                value += 10

        money = float(value)
        print '$', money/100

        cv2.imshow('Detected', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
