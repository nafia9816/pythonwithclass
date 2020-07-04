from datetime import datetime
from connection import connection
from musteriler import musteriler

import random



 
class DbManager:
     def __init__(self):
         self.connection=connection
         self.cursor=self.connection.cursor()
     
     
     def getMusteri(self):
         sql="SELECT * FROM musteriler"
       # value(musteriler.id,)
         self.cursor.execute(sql)
         return self.cursor.fetchall()
         
         




musteriler=DbManager.getMusteri()
print(musteriler)

     
    
 
         
 