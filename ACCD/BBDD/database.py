import mysql.connector
from mysql.connector import errorcode
import constants


def connect_db():
    cnx = mysql.connector.connect(user='root', password='dbrootpass',
                                  host='edu-dbms',
                                  database='employees')

    try:
        cnx = mysql.connector.connect(user='root', password='dbrootpass',
                                      host='edu-dbms',
                                      database='employees')
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

    return cnx


def close_db(cnx):
    cnx.close()

    return 0


def create_db(cnx):
    # creamos un cursor: objeto para trabajar con la base de datos
    cursor = cnx.cursor()

    # creamos la base de datos
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(constants.DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

    # usamos la base de datos o nos situamos sobre la base de datos creada
    try:
        cursor.execute("USE {}".format(constants.DB_NAME))
    except mysql.connector.Error as err:
        print("Database {} does not exists.".format(constants.DB_NAME))
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_db(cnx)
            print("Database {} created successfully.".format(constants.DB_NAME))
            cnx.database = constants.DB_NAME
        else:
            print(err)
            exit(1)

    for table_name in constants.TABLES:
        table_description = constants.TABLES[table_name]
        try:
            print("Creating table {}: ".format(table_name), end='')
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")

    cursor.close()
