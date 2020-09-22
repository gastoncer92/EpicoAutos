import sqlite3


# def extraer_cantidad_empleados():
#    conn = sqlite3.connect('base.db')
#    cursor = conn.cursor()
#    cursor.execute("SELECT COUNT(id_cliente) FROM db_cliente")
#    resultado=int(list(cursor.fetchall()[len(cursor.fetchall())])[-1] + 1)
#    return resultado

def insertar_base_cliente (conn, cliente):
    cursor = conn.cursor ()
    cursor.execute ("INSERT INTO db_cliente(id_cliente,nombre,apellido,domicilio) VALUES (?,?,?,?)", cliente)
    conn.commit ()


def extraer_base_cliente (conn):
    cursor = conn.cursor ()
    cursor.execute ("SELECT id_cliente,nombre,apellido,domicilio FROM db_cliente")
    return cursor


def borrar_base_cliente (conn, idBorrar):
    if idBorrar != '':
        cursor = conn.cursor ()
        cursor.execute ("DELETE FROM db_cliente WHERE id_cliente=(?)", (idBorrar,))
        cursor.execute ("UPDATE db_cliente SET id_cliente=id_cliente-1 WHERE id_cliente>(?);", (idBorrar,))
        conn.commit ()
    else:
        print ("No se a borrado ningun registro de cliente")


def Buscar_cliente (conn, idBuscar):
    if idBuscar == '' or idBuscar.strip () == '':
        idBuscar = "0"
    cursor = conn.cursor ()
    cursor.execute (
        "SELECT * FROM db_cliente WHERE id_cliente=(?) and EXISTS (SELECT * FROM db_cliente WHERE id_cliente=(?))",
        (idBuscar, idBuscar))  # id_empleado=?
    clientes = cursor.fetchall ()
    if not clientes:  # cliente==[]
        clientes = [('', '', '', '')]
    else:
        pass
    return clientes


def modificar_cliente (conn, dato, idmod):
    actualizaNombre = [dato[0], idmod]
    actualizaApellido = [dato[1], idmod]
    actualizaDomicilio = [dato[2], idmod]
    cursor = conn.cursor ()
    cursor.execute ("UPDATE db_cliente SET nombre=(?) WHERE id_cliente=(?);", actualizaNombre)
    cursor.execute ("UPDATE db_cliente SET apellido=(?) WHERE id_cliente=(?);", actualizaApellido)
    cursor.execute ("UPDATE db_cliente SET domicilio=(?) WHERE id_cliente=(?);", actualizaDomicilio)
    conn.commit ()


def buscar_determinados_clientes (conn, dato):
    cursor = conn.cursor ()
    cursor.execute ("SELECT * FROM db_cliente WHERE nombre like ? and apellido like ? and domicilio like ?", dato)
    return cursor
