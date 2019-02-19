import sqlite3
import numpy as np
import cv2

con = sqlite3.connect('user.db')
cursor = con.cursor()
cursor.execute('SELECT * FROM user')
user = cursor.fetchall()
user_list = {i[1]:i[0] for i in user}

cap = cv2.VideoCapture(0)

qr_list = []

while True:
    ret, frame = cap.read()

    qr = cv2.QRCodeDetector()
    data, points, straight_qrcode = qr.detectAndDecode(frame)

    cv2.imshow('frame', frame)

    if data and data not in qr_list:
        qr_list.append(data)
        if data in user_list:
            data = None
            print("ログイン完了")
            print(user_list[data])
        else:
            print('ログイン失敗')

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
