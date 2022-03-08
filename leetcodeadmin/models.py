import sqlite3


def create_model():
    conn = sqlite3.connect('users')
    cur = conn.cursor()

    cur.execute('''CREATE TABLE "Userlogin" (
    "UserID" INTEGER NOT NULL UNIQUE,
    "FirstName" NVARCHAR(300) NOT NULL,
    "LastName" NVARCHAR(300) NOT NULL,
    "Email" NVARCHAR(300) NOT NULL,
    "Password" NVARCHAR(300) NOT NULL,
    PRIMARY KEY("UserID" AUTOINCREMENT)
    )''')

    conn.commit()
    conn.close()