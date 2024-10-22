import database

if __name__ == '__main__':
    cnx = database.connect_db()
    database.create_db(cnx)
