import mysql.connector
from datetime import datetime
from connection import connection
from musteriler import musteriler
from il import il


import random

 
class DbManager:
     def __init__(self):
         self.connection=connection
         self.cursor=self.connection.cursor()
         
     def guncelleil(self,musteriler: musteriler):
        
             musteriler="select * from musteriler"
             self.cursor.execute(musteriler)
             musteri_liste=self.cursor.fetchall()
             
             
             self.cursor.execute(sql,value)
         
             self.connection.commit()

sayac=0

#musteriler="select * from musteriler"
#mycursor.execute(musteriler)
#musteri_liste=mycursor.fetchall()
for musteri in musteri_liste:
    ulke_id=musteri[4]  #MÜSTERİ TABLOSUNDA 4. SUTUNYANİ ÜLKE ID Sİ OLAN KOLON
    musteri_id=musteri[0] #MÜSTERİ İD Sİ
    print(musteri[4])
    iller="SELECT * FROM il where country_id="+str(ulke_id)
    mycursor.execute(iller)
    iller_liste=mycursor.fetchall()
    for il in iller_liste:
        iladi=il[1]
        il_id=il[0]
        print(iladi)
        mycursor = mydb.cursor()
        isimekle="UPDATE musteriler SET ulke_il_id = '"+str(il_id)+"' WHERE id ="+str(musteri_id)
        mycursor.execute(isimekle)
        mydb.commit()
    