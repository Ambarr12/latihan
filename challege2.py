import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database = "5230411147"
)

def guru():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM guru")
    result = cursor.fetchall()
    print(result)

def siswa():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM siswa")
    result = cursor.fetchall()
    print(result)

def menu():
    print("======DATA SEKOLAH======")
    print("1.DATA GURU")
    print("2.DATA SISWA")
    print("3.EXIT")
while True:
    menu()
    inputMenu = int(input("Masukkan Menu [1-3] : "))
    if inputMenu == 1:
        guru()
    elif inputMenu == 2:
        siswa()
    elif inputMenu == 3:
        break
    else:
        print("input eror")
        continue


