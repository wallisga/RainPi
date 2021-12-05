import sqlite3
import appconfig

class connection():

    def __init__(self):
        self.__db_connection = sqlite3.connect(appconfig.sql['name'])

    def __del__(self):
        self._disconnect()
 
    def _execute(self, statement, values=None):
        cur = self.__db_connection.cursor()
        if statement == 0:
            cur.execute("SELECT * FROM "+ appconfig.sql['data'] +";")
        elif statement == 1:
            cur.execute("INSERT INTO "+ appconfig.sql['data'] +" VALUES (?, ?, ?)", (values['timestamp'], values['amount'], values['pi_id']))
            self.__db_connection.commit()
        return [{'timestamp':i[0], 'amount':i[1], 'pi_id':i[2]} for i in cur.fetchall()]

    def _disconnect(self):
        self.__db_connection.close()