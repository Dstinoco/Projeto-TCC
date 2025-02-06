import psycopg2

import os



class ConectarBanco:

    def __init__(self):

        self.db_config = {

            'dbname': os.getenv('POST_DB_DATABASE'),
            'user': os.getenv('POST_DB_USER'),
            'password': os.getenv('POST_DB_PASSWORD1') ,
            'host': os.getenv('POST_DB_HOST'),  
            'port': '5432' }

        self.mydb = psycopg2.connect(**self.db_config)
        self.cursor = self.mydb.cursor()

    def consulta_banco(self, query):

        self.cursor.execute(query)
        data = self.cursor.fetchall()
        columns =  [column[0] for column in self.cursor.description]
        result = [dict(zip(columns, row)) for row in data]
        self.mydb.close()

        return result
    






