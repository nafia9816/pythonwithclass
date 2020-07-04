import mysql.connector
from datetime import datetime
from connection import connection
from urunler import urunler

import xlrd 
import random

 
class DbManager:
     def __init__(self):
         self.connection=connection
         self.cursor=self.connection.cursor()
         
     def ekleUrun(self,urunler: urunler):
        
              sql="INSERT INTO urunler(ad,barkod,fiyat,puan) VALUES (%s,%s,%s,%s)"
              value=(urunler.ad,urunler.barkod,urunler.fiyat,urunler.puan)
              self.cursor.execute(sql,value)
         
              self.connection.commit()

loc = ("6EC59430.xlsx") 
sayac=1
db=DbManager()
while(True):
      wb = xlrd.open_workbook(loc)   #urun adı için
      sheet = wb.sheet_by_index(0) 
    
      sayac=sayac+1   #fiyat aralığı için
      liste=list(range(100)) 
      fiyat=random.choice(liste)
      
      puan=fiyat/4

      barkod_liste=(random.sample(range(12345,98765 ), 1000))
      barkod=random.choice(barkod_liste)
      
      ad=sheet.cell_value(sayac,0) #x,y koodinatları exelin. 
      
      urunler.ad=str(ad)
      urunler.barkod=str(barkod)
      urunler.fiyat=str(fiyat)
      urunler.puan=str(puan)
      db.ekleUrun(urunler)
      
      
      
      
      
      
      
      