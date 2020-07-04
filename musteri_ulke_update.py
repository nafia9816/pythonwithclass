import mysql.connector
from datetime import datetime
from connection import connection
from musteriler import musteriler


import random

 
class DbManager:
     def __init__(self):
         self.connection=connection
         self.cursor=self.connection.cursor()
         
     def guncelleUlke(self,musteriler: musteriler):
        
              sql="UPDATE musteriler SET ulke_id=%s WHERE id=%s"
              value=(musteriler.ulke_id,musteriler.id)
              self.cursor.execute(sql,value)
         
              self.connection.commit()


sayac=1
db=DbManager()
while(sayac<317): 
      sayac=sayac+1
      ulke=list(range(246)) #246 adet ülke var 
      ulke_id=random.choice(ulke)
      #mycursor = mydb.cursor()
      musteriler.ulke_id=str(ulke_id)
      musteriler.id=str(sayac)
     # ulke_guncelle="UPDATE musteriler SET ulke_id = '"+str(ulke_id)+"' WHERE id ="+str(sayac)
     # mycursor.execute(ulke_guncelle)
     # mydb.commit()
      db.guncelleUlke(musteriler)
      print("ulke degistirildi."+str(sayac))
      
      
      
      
      