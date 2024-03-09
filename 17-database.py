import mysql.connector

conn = mysql.connector.connect(host='localhost', user='root', password='blacky062005',auth_plugin='mysql_native_password')

my_cursor=conn.cursor()

my_cursor.execute("""

       CREATE DATABASE IF NOT EXISTS MANISH 
       """)
# my_cursor.execute(""" 

#        """)
# my_cursor.execute("""
#        use MANISH; 
#        CREATE TABLE STUDENTS(
#        SID INTEGER PRIMARY KEY,
#        S_NAME VARCHAR(100) NOT NULL,
#        S_BRANCH VARCHAR(100) NOT NULL,  
#        S_SPECIFICATION VARCHAR(100) NOT NULL
#        );
#        """)

conn.commit()
conn.close()
