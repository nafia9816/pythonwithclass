import mysql.connector
from datetime import datetime
from connection import connection
from musteriler import musteriler

import random
import string
import secrets


 
class DbManager:
     def __init__(self):
         self.connection=connection
         self.cursor=self.connection.cursor()
         
     def guncelleNumara(self,musteriler: musteriler):
        
              sql="UPDATE musteriler SET numara=%s WHERE id=%s"
              value=(musteriler.numara,musteriler.id)
              self.cursor.execute(sql,value)
         
              self.connection.commit()

      

 
    
    

sayac=1
db=DbManager()
while(sayac<317): 
      #sayac=sayac+1
      numara=''.join(secrets.choice( string.ascii_uppercase + string.digits) for _ in range(11))
      print(numara)
      
      sayac=sayac+1
      musteriler.numara=str(numara)
      musteriler.id=str(sayac)
      db.guncelleNumara(musteriler)
      print("numara degistirildi."+str(sayac))
      


     
      
     
     
     
     