import mysql.connector
from datetime import datetime
from connection import connection
from musteriler import musteriler

import xlrd
import random


class DbManager:
    def __init__(self):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def ekleMusteri(self, musteriler: musteriler):
        sql = "INSERT INTO musteriler(numara,referans_no,ad,soyad,email,ulke_id,ulke_il_id,ulke_ilce_id,kayit_tarihi) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        value = (musteriler.numara, musteriler.referans_no, musteriler.ad, musteriler.soyad, musteriler.email,
                 musteriler.ulke_id, musteriler.ulke_il_id, musteriler.ulke_ilce_id, musteriler.kayit_tarihi)
        self.cursor.execute(sql, value)

        self.connection.commit()


loc = ("name.xlsx")
sayac = 1
db = DbManager()
while (True):
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    sayac = sayac + 1
    liste = list(range(10000))  # 10000 tane isimden rastgele seç liste oluştur onlar soyad olacak
    soyad = random.choice(liste)

    ad = sheet.cell_value(sayac, 0)  # x,y koodinatları exelin.
    soyad = sheet.cell_value(soyad, 0)
    email = ad + soyad + "@gmail.com"

    musteriler.numara = "123J584768A"
    musteriler.referans_no = "1"
    musteriler.ad = str(ad)
    musteriler.soyad = str(soyad)
    musteriler.email = str(email)
    musteriler.ulke_id = "1"
    musteriler.ulke_il_id = "1"
    musteriler.ulke_ilce_id = "1"
    musteriler.kayit_tarihi = "2020-06-25 15:13:16"
    db.ekleMusteri(musteriler)




