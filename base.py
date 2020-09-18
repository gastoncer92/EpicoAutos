import sqlite3
from sqlite3 import Error

def conexion():
    try:
        conn = sqlite3.connect('base.db')
        return conn
    except Error:
        print("o rayos! :(")

def db_venta(conn):
    print("Creando base de datos para las ventas")
    cursor = conn.cursor()
    cursor.executescript("""
    CREATE TABLE IF NOT EXISTS "db_venta" (
    	"id_venta"	INTEGER,
	    "precio"	    VARCHAR(15)  NULL,
	    "pie"           VARCHAR(15)  NULL,
	    "deuda"         VARCHAR(15)  NULL,
	    "tia"           VARCHAR(15)  NULL,
	    "periodo"       VARCHAR(15)  NULL,
	    "pagoMensual"   VARCHAR(15)  NULL,
	    "pagoTotal"     VARCHAR(15)  NULL,
	    "costoFinan"    VARCHAR(15)  NULL,
	    "marca"         VARCHAR(15)  NULL,
	    "modelo"        VARCHAR(15)  NULL,
	    "condicion"     VARCHAR(15)  NULL,
	    "nomApeCli"     VARCHAR(15)  NULL,
	    "nomApeEmp"     VARCHAR(15)  NULL,
	        PRIMARY KEY("id_venta")
        );
    """)
    conn.commit()

def db_auto(conn):
    cursor=conn.cursor()
    cursor.executescript("""
    CREATE TABLE IF NOT EXISTS[db_auto] (
        [id_auto] INTEGER  NOT NULL PRIMARY KEY AUTOINCREMENT,
        [marca] VARCHAR(15)  NULL,
        [modelo] VARCHAR(15)  NULL,
        [precio] VARCHAR(15) NULL,
        [condicion] TEXT  NULL
        );
    """)
    conn.commit()

def db_cliente(conn):
    cursor=conn.cursor()
    cursor.executescript("""
    CREATE TABLE IF NOT EXISTS[db_cliente] (
        [id_cliente] INTEGER primary key AUTOINCREMENT,
        [nombre] VARCHAR(15)  NULL,
        [apellido] VARCHAR(15)  NULL,
        [domicilio] VARCHAR(15)  NULL,
        [visible] VARCHAR(2) NULL
        );
    """)
    conn.commit()

def db_empleado(conn):
    cursor=conn.cursor()
    cursor.executescript("""
    CREATE TABLE IF NOT EXISTS[db_empleado] (
        [id_empleado] INTEGER  NOT NULL PRIMARY KEY AUTOINCREMENT,
        [nombre] VARCHAR(15) NOT NULL,
        [apellido] VARCHAR(15) NOT NULL,
        [domicilio] VARCHAR(15) NOT NULL,
        [sueldo] FLOAT NOT NULL
        );
    """)
    conn.commit()

