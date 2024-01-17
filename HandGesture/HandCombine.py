import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier

import numpy as np
import math
import socket

# Khai báo biến imgOutput
imgOutput = np.zeros((480, 640, 3), np.uint8)

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)
classifier = Classifier("Model/keras_model.h5", "Model/labels.txt")

offset = 20
imgSize = 300

xMean, yMean, zMean = 0, 0, 0

labels = ["Picking","Dropping", "Hi The World", "Pointing"]

# Vẽ một khung hình xung quanh màn hình
cv2.rectangle(imgOutput, (0, 0), (imgOutput.shape[1], imgOutput.shape[0]), (255, 0, 0), 4)

while True:
    success, img = cap.read()

    # Gán lại giá trị cho imgOutput
    imgOutput = img.copy()

    hands, img = detector.findHands(img)
    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']

        # Kiểm tra xem bàn tay có trong khung hình hay không
        if x < 0 or y < 0 or x + w > imgOutput.shape[1] or y + h > imgOutput.shape[0]:
            continue

        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255
        imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]

        imgCropShape = imgCrop.shape

        aspectRatio = h / w

        if aspectRatio > 1:
            k = imgSize / h
            wCal = math.ceil(k * w)
            imgResize = cv2.resize(imgCrop, (wCal, imgSize))
            imgResizeShape = imgResize.shape
            wGap = math.ceil((imgSize - wCal) / 2)
            imgWhite[:, wGap:wCal + wGap] = imgResize
            prediction, index = classifier.getPrediction(imgWhite, draw=False)
            print(prediction, index)

        else:
            k = imgSize / w
            hCal = math.ceil(k * h)
            imgResize = cv2.resize(imgCrop, (imgSize, hCal))
            imgResizeShape = imgCrop.shape
            hGap = math.ceil((imgSize - hCal) / 2)
            imgWhite[hGap:hCal + hGap, :] = imgResize
            prediction, index = classifier.getPrediction(imgWhite, draw=False)

        cv2.imshow("ImageCrop", imgCrop)


        cv2.rectangle(imgOutput, (x - offset, y - offset-50),
                      (x - offset+90, y - offset-50+50), (255, 0, 255), cv2.FILLED)
        cv2.putText(imgOutput, labels[index], (x, y - 26), cv2.FONT_HERSHEY_COMPLEX, 1.7, (255, 255, 255), 2)
        cv2.rectangle(imgOutput, (x-offset, y-offset),
                      (x + w+offset, y + h+offset), (255, 0, 255), 4)

        prediction, index = classifier.getPrediction(imgWhite, draw=False)

        # Khai báo biến lmList
        lmList = []

        # tọa độ Socket cho cử chỉ Picking
        if index == 0:
            if hands:
                # Hand 1
                hand = hands[0]
                lmList = hand["lmList"]  # List of 21 Landmark points
                # Tọa độ tâm bàn tay
                xMean, yMean, zMean = 0, 0, 0
                for lm in lmList:
                    xMean += lm[0]
                    yMean += lm[1]
                    zMean += lm[2]
                xMean = xMean / len(lmList)
                yMean = yMean / len(lmList)
                zMean = zMean / len(lmList)

            xSocket = xMean
            ySocket = yMean
            zSocket = zMean

            x1Socket = -0.008942862 + xMean
            y1Socket = 0.9925628 + yMean
            z1Socket = 0.04000697 + zMean

            x2Socket = 26.363
            y2Socket = -77.289
            z2Socket = 83.927

            x3Socket = -23.625
            y3Socket = -30.994
            z3Socket = -2.974

            x4Socket = 0
            y4Socket = 0
            z4Socket = 0

            x5Socket = -26.357
            y5Socket = -3.12
            z5Socket = 6.166

            x6Socket = -19.928
            y6Socket = -2.032
            z6Socket = 4.428

            x7Socket = -31.791
            y7Socket = -4.278
            z7Socket = 7.842

            x8Socket = 0
            y8Socket = 0
            z8Socket = 0

            x9Socket = -26.88
            y9Socket = -3.221
            z9Socket = 6.318

            x10Socket = -37.787
            y10Socket = -7.37
            z10Socket = 13.469

            x11Socket = -12.284
            y11Socket = -0.527
            z11Socket = 2.795

            x12Socket = 0
            y12Socket = 0
            z12Socket = 0

            x13Socket = -20.352
            y13Socket = -2.096
            z13Socket = 4.536

            x14Socket = -40.124
            y14Socket = -6.643
            z14Socket = 10.958

            x15Socket = -6.97
            y15Socket = -0.521
            z15Socket = 1.439

            x16Socket = 0
            y16Socket = 0
            z16Socket = 0

            x17Socket = 0
            y17Socket = 0
            z17Socket = 0

            x18Socket = -32.128
            y18Socket = -4.358
            z18Socket = 7.954

            x19Socket = -41.469
            y19Socket = -7.112
            z19Socket = 11.544

            x20Socket = 0
            y20Socket = 0
            z20Socket = 0

        # tọa độ Socket cho cử chỉ Dropping
        elif index == 1:
            if hands:
                # Hand 1
                hand = hands[0]
                lmList = hand["lmList"]  # List of 21 Landmark points
                # Tọa độ tâm bàn tay
                xMean, yMean, zMean = 0, 0, 0
                for lm in lmList:
                    xMean += lm[0]
                    yMean += lm[1]
                    zMean += lm[2]
                xMean = xMean / len(lmList)
                yMean = yMean / len(lmList)
                zMean = zMean / len(lmList)

            xSocket = xMean
            ySocket = yMean
            zSocket = zMean

            x1Socket = -0.3663113 + xMean
            y1Socket = 0.9623113 + yMean
            z1Socket = -0.307443 + zMean

            x2Socket = 8.499
            y2Socket = -10.12
            z2Socket = 31.958

            x3Socket = -23.625
            y3Socket = -30.994
            z3Socket = -2.974

            x4Socket = 0
            y4Socket = 0
            z4Socket = 0

            x5Socket = -3.088
            y5Socket = -0.209
            z5Socket = 0.628

            x6Socket = 0.236
            y6Socket = 0.015
            z6Socket = -0.047

            x7Socket = -6.207
            y7Socket = -0.455
            z7Socket = 1.278

            x8Socket = 0
            y8Socket = 0
            z8Socket = 0

            x9Socket = -0.647
            y9Socket = -0.041
            z9Socket = 0.131

            x10Socket = 0.785
            y10Socket = -1.088
            z10Socket = 2.343

            x11Socket = -8.19
            y11Socket = -0.282
            z11Socket = 1.841

            x12Socket = 0
            y12Socket = 0
            z12Socket = 0

            x13Socket = -8.755
            y13Socket = -0.685
            z13Socket = 1.822

            x14Socket = 10.801
            y14Socket = 0.47
            z14Socket = -2.137

            x15Socket = -6.97
            y15Socket = -0.521
            z15Socket = 1.439

            x16Socket = 0
            y16Socket = 0
            z16Socket = 0

            x17Socket = 10.082
            y17Socket = 0.451
            z17Socket = -1.996

            x18Socket = -11.188
            y18Socket = -0.929
            z18Socket = 2.357

            x19Socket = -12.436
            y19Socket = -1.064
            z19Socket = 2.637

            x20Socket = 0
            y20Socket = 0
            z20Socket = 0

        # tọa độ Socket cho cử chỉ Hi The World
        elif index == 2:
            if hands:
                # Hand 1
                hand = hands[0]
                lmList = hand["lmList"]  # List of 21 Landmark points
                # Tọa độ tâm bàn tay
                xMean, yMean, zMean = 0, 0, 0
                for lm in lmList:
                    xMean += lm[0]
                    yMean += lm[1]
                    zMean += lm[2]
                xMean = xMean / len(lmList)
                yMean = yMean / len(lmList)
                zMean = zMean / len(lmList)

            xSocket = xMean
            ySocket = yMean
            zSocket = zMean

            x1Socket = -0.008942862 + xMean
            y1Socket = 0.9925628 + yMean
            z1Socket = 0.04000697 + zMean

            x2Socket = -34.964
            y2Socket = -21.774
            z2Socket = -20.66

            x3Socket = -40.993
            y3Socket = -22.598
            z3Socket = -10.244

            x4Socket = 0
            y4Socket = 0
            z4Socket = 0

            x5Socket = -1.418
            y5Socket = -0.279
            z5Socket = 8.805

            x6Socket = 0.236
            y6Socket = 0.015
            z6Socket = -0.047

            x7Socket = -6.207
            y7Socket = -0.455
            z7Socket = 1.278

            x8Socket = 0
            y8Socket = 0
            z8Socket = 0

            x9Socket = -1.822
            y9Socket = -0.095
            z9Socket = -5.719

            x10Socket = 0.785
            y10Socket = -1.088
            z10Socket = 2.343

            x11Socket = -8.19
            y11Socket = -0.282
            z11Socket = 1.841

            x12Socket = 0
            y12Socket = 0
            z12Socket = 0

            x13Socket = -52.521
            y13Socket = -168.188
            z13Socket = 184.131

            x14Socket = -22.236
            y14Socket = 0.078
            z14Socket = 7.923

            x15Socket = -35.462
            y15Socket = -5.217
            z15Socket = 9.118

            x16Socket = 0
            y16Socket = 0
            z16Socket = 0

            x17Socket = -53.461
            y17Socket = -143.575
            z17Socket = 169.256

            x18Socket = -41.105
            y18Socket = 7.134
            z18Socket = 7.241

            x19Socket = 2.021
            y19Socket = -1.086
            z19Socket = 0.524

            x20Socket = 0
            y20Socket = 0
            z20Socket = 0

        # tọa độ Socket cho cử chỉ Pointing
        else:
            if hands:
                # Hand 1
                hand = hands[0]
                lmList = hand["lmList"]  # List of 21 Landmark points
                # Tọa độ tâm bàn tay
                xMean, yMean, zMean = 0, 0, 0
                for lm in lmList:
                    xMean += lm[0]
                    yMean += lm[1]
                    zMean += lm[2]
                xMean = xMean / len(lmList)
                yMean = yMean / len(lmList)
                zMean = zMean / len(lmList)

            xSocket = xMean
            ySocket = yMean
            zSocket = zMean

            x1Socket = -60.787 + xMean
            y1Socket = -20 + yMean
            z1Socket = 25.033 + zMean

            x2Socket = -36.974
            y2Socket = -41.855
            z2Socket = 2.976

            x3Socket = -36.227
            y3Socket = -19.664
            z3Socket = -10.08

            x4Socket = 0
            y4Socket = 0
            z4Socket = 0

            x5Socket = -11.034
            y5Socket = -0.912
            z5Socket = 2.322

            x6Socket = -4.943
            y6Socket = -0.351
            z6Socket = 1.013

            x7Socket = -9.347
            y7Socket = -0.742
            z7Socket = 1.951

            x8Socket = 0
            y8Socket = 0
            z8Socket = 0

            x9Socket = -44.392
            y9Socket = -148.97
            z9Socket = 159.974

            x10Socket = -15.739
            y10Socket = 0.152
            z10Socket = 9.783

            x11Socket = -32.046
            y11Socket = -3.132
            z11Socket = 12.768

            x12Socket = 0
            y12Socket = 0
            z12Socket = 0

            x13Socket = -32.457
            y13Socket = -150.483
            z13Socket = 161.186

            x14Socket = 1.996
            y14Socket = 7.424
            z14Socket = 7.997

            x15Socket = -27.957
            y15Socket = -1.439
            z15Socket = 9.526

            x16Socket = 0
            y16Socket = 0
            z16Socket = 0

            x17Socket = -50.723
            y17Socket = -153.393
            z17Socket = 165.8

            x18Socket = -18.927
            y18Socket = 3.842
            z18Socket = 6.622

            x19Socket = -38.307
            y19Socket = 1.951
            z19Socket = 3.249

            x20Socket = 0
            y20Socket = 0
            z20Socket = 0

        # Tọa độ Socket cuối cùng
        data = [xSocket, ySocket, zSocket, x1Socket, y1Socket, z1Socket, x2Socket, y2Socket, z2Socket, x3Socket,
                y3Socket, z3Socket, x4Socket, y4Socket, z4Socket, x5Socket, y5Socket, z5Socket, x6Socket, y6Socket,
                z6Socket, x7Socket, y7Socket, z7Socket, x8Socket, y8Socket, z8Socket, x9Socket, y9Socket, z9Socket,
                x10Socket, y10Socket, z10Socket, x11Socket, y11Socket, z11Socket, x12Socket, y12Socket, z12Socket,
                x13Socket, y13Socket, z13Socket, x14Socket, y14Socket, z14Socket, x15Socket, y15Socket, z15Socket,
                x16Socket, y16Socket, z16Socket, x17Socket, y17Socket, z17Socket, x18Socket, y18Socket, z18Socket,
                x19Socket, y19Socket, z19Socket, x20Socket, y20Socket, z20Socket]
        print(data)

        # Gửi dữ liệu Socket đến server
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        serverAddressPort = ("127.0.0.1", 5052)
        sock.sendto(str.encode(str(data)), serverAddressPort)
        sock.close()

    cv2.imshow("Image", imgOutput)
    cv2.waitKey(1)
