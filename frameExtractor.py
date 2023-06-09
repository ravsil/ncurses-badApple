import cv2

video = cv2.VideoCapture("badApple.mp4")
frameCount = 0

notFinished = True
while True:
    notFinished, frame = video.read()

    if not notFinished:
        break

    newFrame = cv2.resize(frame, (64, 36))
    cv2.imwrite(f"frames/{frameCount}.png", newFrame)
    frameCount += 1

    print(f"Extracted {frameCount} frames!")

video.release()
