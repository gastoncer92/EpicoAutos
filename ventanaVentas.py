import sqlite3

from PyQt5 import QtWidgets

from ui_ventas import Ui_Form


class VerVentas (QtWidgets.QWidget, Ui_Form):
    def __init__ (self, *args):
        QtWidgets.QWidget.__init__ (self, *args)
        self.setupUi (self)
        #self.tableWidget.isMaximized()
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.setHorizontalHeaderLabels (["id_venta","Precio","Pago Inicial","Deuda","Tasa Int Anual","Periodo","Pago Mensual","Pago Total","Cost. Financiado","Marca","Modelo","Condicion","Cliente","Empleado"])
        for i in [0,1,2,3,4,5,6,7,8,9,10,11,12]:
            self.tableWidget.resizeColumnToContents(i)


        self.actualizarVentas()
        self.pushButton.clicked.connect(self.actualizarVentas)

    def actualizarVentas (self):
        conn=sqlite3.connect('base.db')
        consulta='select * from db_venta'
        cursor=conn.cursor()
        resultado=cursor.execute(consulta)
        self.tableWidget.setRowCount (0)
        for row_number, row_data in enumerate (resultado):
            self.tableWidget.insertRow (row_number)
            for column_number, data in enumerate (row_data):
                self.tableWidget.setItem (row_number, column_number, QtWidgets.QTableWidgetItem (str (data)))
        for i in [0,1,2,3,4,5,6,7,8,9,10,11,12]:
            self.tableWidget.resizeColumnToContents(i)
#ventas = VerVentas ()

