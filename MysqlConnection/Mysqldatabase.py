import mysql.connector
from mysql.connector import Error
class MySqlConnection():
    try:
        def Connect(self,host,username,password,database,port):
            self.hostname=host
            self.username=username
            self.password=password
            self.database=database
            self.port=port
            self.connect=mysql.connector.Connect(host= self.hostname,username=self.username,password=
            self.password,database=self.database,port=self.port)
            self.cursor = self.connect.cursor()
            print("Connected Successfully")
    except Error as e:
        print(e)
