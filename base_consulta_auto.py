



def insertar_base_auto(conn,d):

    try:
        cursor = conn.cursor()
        datoNuevo=[d[0],d[1],d[2],"$%.2f"%float(list(d).pop(3)),d[4]]
        cursor.execute("INSERT INTO db_auto(id_auto,marca,modelo,precio,condicion) VALUES (?,?,?,?,?)",datoNuevo)
        conn.commit()
    except ValueError:
        print("asd")

def borrar_base_auto(conn,idBorrar):
    if idBorrar != '':
        cursor = conn.cursor()
        cursor.execute("DELETE FROM db_auto WHERE id_auto=(?)", (idBorrar,))
        cursor.execute("UPDATE db_auto SET id_auto=id_auto-1 WHERE id_auto>(?);",(idBorrar,))
        conn.commit()
    else:
        print("No se a borrado ningun registro de autos")

def Buscar_auto(conn,idBuscarAuto):
    if idBuscarAuto=='' or idBuscarAuto.strip()=='':
        idBuscarAuto="0"
        #print("concha!")
    cursor=conn.cursor()
    #print("pase!!!!")
    cursor.execute("SELECT * FROM db_auto WHERE id_auto=(?) and EXISTS (SELECT * FROM db_auto WHERE id_auto=(?))",(idBuscarAuto,idBuscarAuto))
    autos = cursor.fetchall()
    #print("asd"
    #      "eee")
    #print(autos)
    if not autos:
        autos=[('','','','')]
    elif autos==[]:
        autos = [('', '', '', '')]
    else:pass
    return autos

def modificar_auto(conn,dato,idmod):   #el idmod es lo nuevo modificado
    actualizaPrecio=["$%.2f"%float(dato[1]),idmod]
    cursor=conn.cursor()
    cursor.execute("UPDATE db_auto SET precio=(?) WHERE id_auto=(?);", actualizaPrecio)
    conn.commit()
    
def buscar_determinados_autos(conn,dato):
    cursor=conn.cursor()
    cursor.execute ("SELECT * FROM db_auto WHERE marca like ? and modelo like ? and precio like ? and condicion like ?", dato)
    return cursor