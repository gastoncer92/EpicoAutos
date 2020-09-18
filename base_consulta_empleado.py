import sqlite3

#SELECT * from db_empleado;
#SELECT ALL id_empleado FROM db_empleado
#SELECT count(*) FROM db_empleado
#UPDATE db_empleado SET id_empleado=id_empleado-1 WHERE id_empleado>1

#def actualizar(self):
#    conn = sqlite3.connect('base.db')
#    consulta="SELECT * from db_empleado"
#    cursor=conn.cursor()
#    resultado=cursor.execute(consulta)
#    #self.tableWidget_empleado.setRowCount(0)
#    for row_number, row_data in enumerate(resultado):
#        self.tableWidget.insertRow(row_number)
#        for column_number, data in enumerate(row_data):
#            self.tableWidget.setItem(row_number, column_number,QtWidgets.QTableWidgetItem(str(data)))
#    conn.close()
#    print("hakuna matata!")
def extraer_cantidad_empleados():
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(id_empleado) FROM db_empleado")
    resultado=int(list(cursor.fetchall()[len(cursor.fetchall())])[-1] + 1)
    return resultado

def insertar_base_empleado(conn,empleado):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO db_empleado(id_empleado,nombre,apellido,domicilio,sueldo) VALUES (?,?,?,?,?)",empleado)
    conn.commit()

def extraer_base_empleado(conn):
    cursor=conn.cursor()
    cursor.execute("SELECT id_empleado,nombre,apellido,domicilio,sueldo FROM db_empleado")
    return cursor

def borrar_base_empleado(conn,idBorrar):
    if idBorrar!='':
        cursor=conn.cursor()
        cursor.execute("DELETE FROM db_empleado WHERE id_empleado=(?);",(idBorrar,))
        cursor.execute("UPDATE db_empleado SET id_empleado=id_empleado-1 WHERE id_empleado>(?);", (idBorrar,))
        conn.commit()
    else:
        print("No se a borrado ningun registro")


def Buscar_empleado(conn,idBuscar):
    if idBuscar=='' or idBuscar.strip()=='':
        idBuscar="0"
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM db_empleado WHERE id_empleado=(?) and EXISTS (SELECT * FROM db_empleado WHERE id_empleado=(?))",(idBuscar,idBuscar)) #id_empleado=?
    empleado =cursor.fetchall()
    if not empleado:  #empleado==[]
        empleado=[('','','','','')]
    else:pass
    return empleado

def modificar_empleado(conn,dato,idmod):
    actualizaNombre=[dato[0],idmod]
    actualizaApellido=[dato[1],idmod]
    actualizaDomicilio=[dato[2],idmod]
    actualizaSueldo=[dato[3],idmod]
    cursor=conn.cursor()

    cursor.execute("UPDATE db_empleado SET nombre=(?) WHERE id_empleado=(?);",actualizaNombre)
    cursor.execute("UPDATE db_empleado SET apellido=(?) WHERE id_empleado=(?);", actualizaApellido)
    cursor.execute("UPDATE db_empleado SET domicilio=(?) WHERE id_empleado=(?);", actualizaDomicilio)
    cursor.execute("UPDATE db_empleado SET sueldo=(?) WHERE id_empleado=(?);", actualizaSueldo)

    print("aleluya!")
    conn.commit()

def buscar_determinados_empleados(conn,dato):
    cursor=conn.cursor()
    cursor.execute ("SELECT * FROM db_empleado WHERE nombre like ? and apellido like ? and domicilio like ? and sueldo like ?", dato)
    return cursor
