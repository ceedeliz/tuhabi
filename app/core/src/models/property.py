import os
import datetime
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

USER = os.getenv('MYSQL_USER')
PASSWORD = os.environ.get('MYSQL_PASSWORD')
HOST = os.environ.get('MYSQL_HOST')
PORT = os.environ.get('MYSQL_PORT')


class PropertyModel():
    def properties(filter):
        cnx = mysql.connector.connect(
            user=USER, password=PASSWORD, host=HOST, port=PORT)
        cursor = cnx.cursor(dictionary=True)

        query = ("""select p.id,p.address,p.city,p.price,p.description,p.year, 
                 s.name as "status", max(sh.update_date) from habi_db.status_history  sh 
                 left join habi_db.status s on sh.status_id = s.id  join habi_db.property p 
                 on sh.property_id = p.id where s.name in ("pre_venta","en_venta","vendido") 
                 group by sh.property_id """)
        print(filter)
        count = 0
        for key in filter:
            if filter[key] is not None and key != "limit":
                print(filter[key])
                query += " AND "
                count = count + 1
                query += "{}='{}'".format(key, filter[key])

        query += " limit {};".format(filter["limit"])
        print("query")
        print(query)
        cursor.execute(query)
        data = cursor.fetchall()

        cursor.close()
        cnx.close()
        return data

    def property(id):
        cnx = mysql.connector.connect(
            user=USER, password=PASSWORD, host=HOST, port=PORT)
        cursor = cnx.cursor()

        query = ("SELECT * FROM habi_db.property where id = {}").format(id)
        print("query")
        print(query)
        cursor.execute(query)
        data = cursor.fetchall()

        cursor.close()
        cnx.close()
        return data
