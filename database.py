import sqlite3
from sqlite3 import Error
import colors

# Inicializamos Colors 
rainbow = colors

class Database:
    def __init__(self, db_file):
        """Inicializa la conexión a la base de datos"""
        self.conn = self.create_connection(db_file)

    def create_connection(self, db_file):
        """Crea una conexión a la base de datos SQLite"""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(rainbow.Color(color="green", text=f"[*] Successful connection to the  {db_file}"))
        except Error as e:
            print(rainbow.Color(color="red", text=f"[!] Alert connection error {e}"))
        return conn

    def create_table(self, create_table_sql):
        """Crea una tabla desde una sentencia SQL"""
        try:
            c = self.conn.cursor()
            c.execute(create_table_sql)
            return True
        except Error as e:
            return False

    def create_record(self, table, data):
        """Inserta un nuevo registro en la tabla"""
        keys = ', '.join(data.keys())
        question_marks = ', '.join(list('?' * len(data)))
        values = tuple(data.values())
        sql = f"INSERT INTO {table} ({keys}) VALUES ({question_marks})"
        cur = self.conn.cursor()
        cur.execute(sql, values)
        self.conn.commit()
        return cur.lastrowid

    def read_records(self, table):
        """Lee todos los registros de la tabla"""
        cur = self.conn.cursor()
        cur.execute(f"SELECT * FROM {table}")
        rows = cur.fetchall()
        return rows

    def update_record(self, table, data, condition):
        """Actualiza un registro en la tabla"""
        keys = ', '.join([f"{k} = ?" for k in data.keys()])
        values = tuple(data.values())
        sql = f"UPDATE {table} SET {keys} WHERE {condition}"
        cur = self.conn.cursor()
        cur.execute(sql, values)
        self.conn.commit()

    def delete_record(self, table, condition):
        """Elimina un registro de la tabla"""
        sql = f"DELETE FROM {table} WHERE {condition}"
        cur = self.conn.cursor()
        cur.execute(sql)
        self.conn.commit()

    def create_table_sql(self):
        query = """
        CREATE TABLE IF NOT EXISTS users (
            id integer PRIMARY KEY,
            username text NOT NULL,
            password text NOT NULL,
            app text NOT NULL
        );"""
        return query
    
