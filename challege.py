import numpy as np
import matplotlib.pyplot as plt

listMahasiswa = [
    {
        "nim": "5230412",
        "nama": "Ambar",
        "matkul": {
            "kalkulus": 90,
            "pti": 100,
            "alpro": 95,
        },
    },
    {
        "nim": "5230447",
        "nama": "Hamidah",
        "matkul": {
            "kalkulus": 80,
            "pti": 90,
            "alpro": 80,
        },
    },
    {
        "nim": "5230426",
        "nama": "Ayu",
        "matkul": {
            "kalkulus": 95,
            "pti": 90,
            "alpro": 88,
        },
    },
    {
        "nim": "5230419",
        "nama": "Mareza",
        "matkul": {
            "kalkulus": 85,
            "pti": 90,
            "alpro": 80,
        },
    },
    {
        "nim": "5230452",
        "nama": "Anisa",
        "matkul": {
            "kalkulus": 80,
            "pti": 90,
            "alpro": 80,
        },
    },
]


def printMenu():
    print("\n1. Cari Mahasiswa")
    print("2. Keluar")


def cariMahasiswa(nim):
    for mahasiswa in listMahasiswa:
        if mahasiswa["nim"] == nim:
            return mahasiswa

    return None


while True:
    printMenu()
    menu = input("Masukkan pilihan menu [1-2] : ")

    if menu == "1":
        nim = input("Masukan NIM : ")
        mahasiswa = cariMahasiswa(nim)

        if mahasiswa == None:
            print("\n=========================")
            print("Mahasiswa Tidak Ditemukan")
            print("=========================")
            continue

        y = np.array(
            [
                mahasiswa["matkul"]["matematika"],
                mahasiswa["matkul"]["inggris"],
                mahasiswa["matkul"]["alpro"],
            ]
        )
        labels = ["Matematika", "Inggris", "Alpro"]
        plt.pie(y, labels=labels, autopct="%1.0f%%")
        plt.title(mahasiswa["nama"])
        plt.legend()
        plt.show()

    elif menu == "2":
        break
    else:
        print("\n===================")
        print("Pilihan Tidak Valid")
        print("===================")