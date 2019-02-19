import qrcode
import sqlite3
from datetime import datetime

time = datetime.now().strftime("%Y%m%d%H%M%S")

print('ユーザー名を入力してください。')
name = input()

print('パスワードを設定してください。')
password = input()

# --- データベースに保存
con = sqlite3.connect('user.db')

cursor = con.cursor()

p = "INSERT INTO user(name, password) VALUES(?, ?)"
cursor.execute(p, (name, password))

con.commit()

# --- 

img = qrcode.make(password)
img.save('{}.png'.format(time))