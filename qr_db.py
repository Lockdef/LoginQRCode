import sqlite3

# データベースの接続
con = sqlite3.connect('user.db')

# カーソルオブジェクトの作成
cursor = con.cursor() 

# テーブルの作成
cursor.execute("CREATE TABLE user(name, password)")

# データベースに反映させる
con.commit()