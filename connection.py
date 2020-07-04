import mysql.connector


connection = mysql.connector.connect(  #VERİTABANI İLE BAĞLANTI KURULDU
  host="127.0.0.1",
  port="3307",
  user="root",
  passwd="root",
  database="market_2"
)



