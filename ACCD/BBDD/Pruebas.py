import mysql.connector
cnx = mysql.connector .connect(user='root', password ='dbrootpass',
                               host ='127.0.0.1' ,
                               database ='employees' )
cnx.close()