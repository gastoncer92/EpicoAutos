from PyQt5 import QtWidgets
from PyQt5.QtGui import QIntValidator, QDoubleValidator
from PyQt5.QtWidgets import QApplication
from ui_main import Ui_MainWindow
from base import *
from base_consulta_empleado import *
from base_consulta_cliente import *
from base_consulta_auto import *
from ui_ventas import *
from ventanaVentas import *
from ui_manual import *


# terminado

class MainWindow (QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__ (self, *args):
        QtWidgets.QMainWindow.__init__ (self, *args)
        self.setupUi (self)
        self.actualizarEmpleado ()
        self.actualizarCliente ()
        self.lineEdit_borrar_emp.setText ("")
        self.pushButton_agregar.clicked.connect (self.agregarEmpleado)
        self.pushButton_borrar_emp.clicked.connect (self.borrarEmpleado)
        self.tableWidget_empleado.setHorizontalHeaderLabels (['ID', 'NOMBRE', 'APELLIDO', 'DIRECCION', 'SUELDO'])
        for i in [0, 1, 2, 3, 4]:
            self.tableWidget_empleado.resizeColumnToContents (i)
        self.pushButton_14.clicked.connect (self.buscarEmpleado)
        self.pushButton_9.clicked.connect (self.agregarCliente)
        self.pushButton_6.clicked.connect (self.borrarCliente)
        self.tableWidget_clientes.setHorizontalHeaderLabels (['ID', 'NOMBRE', 'APELLIDO', 'DIRECCION'])
        for i in [0, 1, 2, 3]:
            self.tableWidget_clientes.resizeColumnToContents (i)
        self.pushButton_11.clicked.connect (self.buscarCliente)
        self.pushButton_13.clicked.connect (self.modificarEmpleado)
        self.pushButton_10.clicked.connect (self.modificarCliente)
        self.tableWidget_empleado_3.setHorizontalHeaderLabels (['ID', 'MARCA', 'MODELO', 'PRECIO', 'CONDICION'])
        for i in [0, 1, 2, 3, 4]:
            self.tableWidget_empleado_3.resizeColumnToContents (i)
        self.pushButton_15.clicked.connect (self.agregarAuto)
        self.pushButton_8.clicked.connect (self.borrarAuto)
        self.pushButton_17.clicked.connect (self.buscarAuto)
        self.pushButton_16.clicked.connect (self.modificarAuto)
        self.actualizarAuto ()
        self.armarComboBox ()
        self.comboBox.currentIndexChanged.connect (self.elegirAuto)
        self.pushButton_2.clicked.connect (self.buscarClienteAgregar)
        self.pushButton_3.clicked.connect (self.actualizarCliente)
        self.pushButton_4.clicked.connect (self.buscarEmpleadoAgregar)
        self.pushButton_5.clicked.connect (self.actualizarEmpleado)
        self.pushButton_7.clicked.connect (self.buscarAutoAgregar)
        self.pushButton_12.clicked.connect (self.actualizarAuto)

        self.spinBox.valueChanged.connect (self.PonerInfoAuto)
        self.spinBox_2.valueChanged.connect (self.PonerInfoEmpleado)
        self.spinBox_3.valueChanged.connect (self.PonerInfoCliente)

        self.lineEdit_29.cursorPositionChanged.connect (self.agregarPIE)
        self.spinBox_4.valueChanged.connect (self.agregarTIA)
        self.comboBox_3.addItems (['', '12', '24', '36', '48', '60', '72', '84', '96'])
        self.comboBox_3.currentIndexChanged.connect (self.agregarPeriodo)
        self.pushButton_20.clicked.connect (self.calcular)
        self.pushButton_18.clicked.connect (self.registro)
        self.pushButton_18.setDisabled (True)
        self.pushButton_19.clicked.connect (self.deshacer)
        self.pushButton.clicked.connect (self.verVentas)
        self.pushButton_10.setDisabled (True)
        self.pushButton_13.setDisabled (True)
        self.pushButton_16.setDisabled (True)
        # self.lineEdit_41.setValidator(QIntValidator(1,999))
        # self.stop_loss_price_input.setValidator (QDoubleValidator (999999, -999999, 8))
        self.lineEdit_41.setValidator (QDoubleValidator (999999, -999999, 8))
        self.lineEdit_sueldo_emp.setValidator (QDoubleValidator (999999, -999999, 8))
        self.pushButton_21.clicked.connect (self.manual)

        self.lineEdit_16.setValidator (QIntValidator (1, 99999))
        self.lineEdit_16.setMaxLength (8)
        self.lineEdit_14.setValidator (QIntValidator (1, 99999))
        self.lineEdit_14.setMaxLength (8)
        self.lineEdit_19.setValidator (QIntValidator (1, 99999))
        self.lineEdit_19.setMaxLength (8)
        self.lineEdit_borrar_emp.setValidator (QIntValidator (1, 99999))
        self.lineEdit_borrar_emp.setMaxLength (8)

        self.lineEdit_18.setValidator (QIntValidator (1, 99999))
        self.lineEdit_18.setMaxLength (8)

        self.lineEdit_15.setValidator (QIntValidator (1, 99999))
        self.lineEdit_15.setMaxLength (8)

        self.lineEdit_43.setValidator(QDoubleValidator (999999, -999999, 8))
        self.lineEdit_43.setMaxLength (12)




    def manual (self):
        # manual = Manual ()
        # mainwindow.close ()
        print ("asdasd")
        manual.showMaximized ()
        # manual.showMaximized ()

    def verVentas (self):
        ventas.showMaximized ()

    def deshacer (self):
        self.pushButton_18.setDisabled (True)
        self.spinBox.setValue (0)
        self.spinBox_2.setValue (0)
        self.spinBox_3.setValue (0)
        self.spinBox_4.setValue (0)
        self.lineEdit_29.setText ('')
        self.comboBox_3.setCurrentIndex (0)

        self.spinBox.setEnabled (True)
        self.spinBox_2.setEnabled (True)
        self.spinBox_3.setEnabled (True)
        self.lineEdit_29.setEnabled (True)
        self.spinBox_4.setEnabled (True)
        self.comboBox_3.setEnabled (True)

    def registro (self):
        idAuto = self.spinBox.text ()
        idEmp = self.spinBox_2.text ()
        idCli = self.spinBox_3.text ()

        # self.pushButton_18.setDisabled(True)
        # self.deshacer()

        if idAuto != '0' or idCli != '0' or idEmp != '0':
            conn = conexion ()
            cursor = conn.cursor ()
            datoAuto = Buscar_auto (conn, idAuto)
            datoEmp = Buscar_empleado (conn, idEmp)
            datoCli = Buscar_cliente (conn, idCli)
            # pie =self.lineEdit_29.text()
            pie = self.lineEdit_29.text ()
            print (".........")
            print (pie)
            print (type (pie))
            print (".........")
            cursor.execute (
                "SELECT precio FROM db_auto where id_auto=(?) and EXISTS (SELECT * FROM db_auto WHERE id_auto=(?))",
                (idAuto, idAuto))
            valores = cursor.fetchone ()
            precio = float (valores[0])
            print ("////////////////////")
            print (precio)
            print (valores)
            print (type (valores[0][0]))
            print ("////////////////////")
            # deuda=precio-PIE
            deuda = float (valores[0]) - float (pie)  # deuda

            tia = float (self.spinBox_4.text ()) / 100  # tia
            periodo = self.comboBox_3.currentText ()
            n = float (periodo) / 12  # anual
            pagoMensual = (deuda * tia) / (((1 + tia) ** n) - 1)
            print ("asdasdasd")
            print (type (pie))
            pagoTotal = float (pie) + (pagoMensual * n)
            costoFinanciero = pagoTotal - float (valores[0])

            precio = str (round (precio, 2))
            pie = str (round (float (pie), 2))
            deuda = str (round (deuda, 2))
            tia = str (round (tia, 2))
            periodo = str (periodo)
            pagoMensual = str (round (pagoMensual, 2))
            pagoTotal = str (round (pagoTotal, 2))
            costoFinanciero = str (round (costoFinanciero, 2))
            nomApeEmp = "%s %s" % (datoEmp[0][1], datoEmp[0][2])
            nomApeCli = "%s %s" % (datoCli[0][1], datoCli[0][2])
            marca = "%s" % datoAuto[0][1]
            modelo = "%s" % datoAuto[0][2]
            condicion = "%s" % datoAuto[0][4]

            consulta = "SELECT COUNT(id_venta) FROM db_venta"
            cursor.execute (consulta)
            idAutoRegistro = cursor.fetchall ()[len (cursor.fetchall ())]
            idAutoRegistro = int (list (idAutoRegistro)[-1]) + 1
            registro = [idAutoRegistro, precio, pie, deuda, tia, periodo, pagoMensual, pagoTotal, costoFinanciero,
                        marca,
                        modelo, condicion, nomApeCli, nomApeEmp]
            cursor.execute (
                "INSERT INTO db_venta(id_venta,precio,pie,deuda,tia,periodo,pagoMensual,pagoTotal,costoFinan,marca,modelo,condicion,nomApeCli,nomApeEmp)VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?);",
                registro)
            conn.commit ()
            borrar_base_auto (conn, idAuto)
            self.actualizarAuto ()
            self.deshacer ()

        else:
            pass

    def calcular (self):
        try:
            pie = float (self.lineEdit_29.text ())
            print ("=======")
            print (pie)
            print ("=======")
            idAuto = self.spinBox.text ()
            conn = conexion ()
            cursor = conn.cursor ()
            cursor.execute (
                "SELECT precio FROM db_auto where id_auto=(?) and EXISTS (SELECT * FROM db_auto WHERE id_auto=(?))",
                (idAuto, idAuto))
            valores = cursor.fetchone ()
            print (valores[0].strip ("$"))
            mA = float (valores[0].strip ("$")) - pie  # deuda
            i = float (self.spinBox_4.text ()) / 100  # tia
            periodo = self.comboBox_3.currentText ()
            n = int (periodo) / 12  # anual
            pagoMensual = (mA * i) / (((1 + i) ** n) - 1)
            print (pagoMensual)
            self.label_5.setText ("Pago mensual: $ %.2f" % float (pagoMensual))
            pagoTotal = pie + (pagoMensual * n)
            self.label_7.setText ("Pago total: $ %.2f" % pagoTotal)
            costoFinanciero = pagoTotal - float (valores[0].strip ("$"))
            self.label_8.setText ("Costo financiamiento: $ %.2f" % costoFinanciero)
            self.spinBox.setDisabled (True)
            self.spinBox_2.setDisabled (True)
            self.spinBox_3.setDisabled (True)
            self.pushButton_18.setEnabled (True)
            self.lineEdit_29.setDisabled (True)
            self.spinBox_4.setDisabled (True)
            self.comboBox_3.setDisabled (True)
        except ValueError:
            print ("Error")
            self.lineEdit_29.setText ('')
        except TypeError:
            print ("error linea 145")

    def agregarPeriodo (self):
        periodo = self.comboBox_3.currentText ()
        # anual = int (periodo) / 12
        try:
            anual = int (periodo) / 12
            self.label_2.setText ("Periodos: %s meses (%d años)" % (periodo, anual))
        except ValueError:
            print ("asd")

    def agregarTIA (self):
        tia = self.spinBox_4.text ()
        try:
            self.label_4.setText ("Tasa Interés Anual:  %s%%" % tia)
        except ValueError:
            self.label_4.setText ("Tasa Interés Anual: 0%%")

    def agregarPIE (self):
        print ("asdasdasd")
        pie = self.lineEdit_29.text ()
        try:
            self.label_6.setText ("PIE: $ %.2f" % float (pie))
            idAuto = self.spinBox.text ()
            conn = conexion ()
            cursor = conn.cursor ()
            cursor.execute (
                "SELECT precio FROM db_auto where id_auto=(?) and EXISTS (SELECT * FROM db_auto WHERE id_auto=(?))",
                (idAuto, idAuto))
            valores = cursor.fetchone ()
            self.label_3.setText ("Deuda: $ %.2f" % (float (valores[0].strip ("$")) - float (pie)))
        except ValueError:
            self.label_6.setText ("PIE: $ 0")
        except TypeError:
            print ("a")

    def agregarFinanciado (self):
        pass

    def agregarContado (self):
        contado = self.lineEdit_12.text ()
        try:
            self.label_65.setText ("Pago al contado: $ %.2f" % (float (contado),))  # %.2f
        except ValueError:
            print ("error")

    def cargarFinanciado (self):
        if self.checkBox_2.isChecked ():
            self.lineEdit_9.setEnabled (True)
            self.spinBox_4.setEnabled (True)
            self.spinBox_5.setEnabled (True)
            self.label_66.setText ("Pago Financiado: ")
        elif not self.checkBox_2.isChecked ():
            self.lineEdit_9.setDisabled (True)
            self.spinBox_4.setDisabled (True)
            self.spinBox_5.setDisabled (True)
            self.lineEdit_9.setText ('')

    def cargarContado (self):
        if self.checkBox.isChecked ():
            self.lineEdit_12.setEnabled (True)
            self.label_65.setText ("Pago al contado: ")
        elif not self.checkBox.isChecked ():
            self.lineEdit_12.setDisabled (True)
            self.lineEdit_12.setText ('')
            self.label_65.setText ("Pago al contado:")

    def PonerInfoCliente (self):
        idInfoCliente = self.spinBox_3.text ()
        conn = conexion ()
        cursor = conn.cursor ()
        cursor.execute (
            "SELECT nombre,apellido FROM db_cliente where id_cliente=(?) and EXISTS (SELECT * FROM db_cliente WHERE id_cliente=(?))",
            (idInfoCliente, idInfoCliente))
        valores = cursor.fetchone ()
        try:
            self.label_64.setText ("Cliente: %s %s" % (
                valores[0], valores[1]))
        except TypeError:
            self.label_64.setText ("Cliente: --")

    def PonerInfoEmpleado (self):
        idInfoEmpleado = self.spinBox_2.text ()
        conn = conexion ()
        cursor = conn.cursor ()
        cursor.execute (
            "SELECT nombre,apellido FROM db_empleado where id_empleado=(?) and EXISTS (SELECT * FROM db_empleado WHERE id_empleado=(?))",
            (idInfoEmpleado, idInfoEmpleado))
        valores = cursor.fetchone ()
        try:
            self.label_63.setText ("Empleado: %s %s" % (
                valores[0], valores[1]))
        except TypeError:
            self.label_63.setText ("Empleado: --")

    def PonerInfoAuto (self):
        idInfoAuto = self.spinBox.text ()
        conn = conexion ()
        cursor = conn.cursor ()
        cursor.execute (
            "SELECT marca,modelo,precio,condicion FROM db_auto where id_auto=(?) and EXISTS (SELECT * FROM db_auto WHERE id_auto=(?))",
            (idInfoAuto, idInfoAuto))
        valores = cursor.fetchone ()
        try:
            self.label_62.setText ("Marca: %s \nModelo: %s \nCondicion: %s" % (
                valores[0], valores[1], valores[3]))
            self.label.setText ("Precio: $ %.2f" % float (valores[2].strip ("$")))
        except TypeError:
            self.label_62.setText ("Marca: -- \nModelo: -- \nPrecio: -- \nCondicion: --")
            self.label.setText ("Precio: $ %.2f" % float (0))

    def buscarAutoAgregar (self):
        marca = self.comboBox.currentText ()
        modelo = self.comboBox_4.currentText ()
        precio = self.lineEdit_41.text ()
        condicion = self.comboBox_2.currentText ()
        dato = [marca + '%', modelo + '%', precio + '%', condicion + '%']
        if dato != ['%', '%', '%', '%']:
            conn = conexion ()
            info = buscar_determinados_autos (conn, dato)
            self.tableWidget_empleado_3.setRowCount (0)
            for row_number, row_data in enumerate (info):
                self.tableWidget_empleado_3.insertRow (row_number)
                for column_number, data in enumerate (row_data):
                    self.tableWidget_empleado_3.setItem (row_number, column_number,
                                                         QtWidgets.QTableWidgetItem (str (data)))
            conn.close ()
        else:
            pass

    def buscarEmpleadoAgregar (self):
        nombre = self.lineEdit_nombre_emp.text ().strip ()
        apellido = self.lineEdit_apellido_emp.text ().strip ()
        domicilio = self.lineEdit_domicilio_emp.text ().strip ()
        sueldo = self.lineEdit_sueldo_emp.text ().strip ()
        dato = [nombre + '%', apellido + '%', domicilio + '%', sueldo + '%']
        if dato != ['%', '%', '%', '%']:
            conn = conexion ()
            info = buscar_determinados_empleados (conn, dato)
            self.tableWidget_empleado.setRowCount (0)
            for row_number, row_data in enumerate (info):
                self.tableWidget_empleado.insertRow (row_number)
                for column_number, data in enumerate (row_data):
                    self.tableWidget_empleado.setItem (row_number, column_number,
                                                       QtWidgets.QTableWidgetItem (str (data)))
            conn.close ()
        else:
            pass

    def armarComboBox (self):
        listaDeCoches = ['', "ABARTH", "ALFA ROMEO",
                         "BMW", "BYD", "CHEVROLET",
                         "AUDI", "ASTON MARTIN", "BENTLEY",
                         "CITROEN", "DACIA", 'DFSK', 'DS',
                         'FERRARI', 'FIAT', 'FORD', 'HONDA',
                         'HYUNDAI', 'INFINITI', 'ISUZU',
                         'JAGUAR', 'KIA', 'LAMBORGHINI',
                         'MASERATI', 'MERCEDES']
        self.comboBox.addItems (sorted (listaDeCoches))
        condicion = ['', 'Nuevo', 'Usado']
        self.comboBox_2.addItems (condicion)

    def elegirAuto (self):
        # if self.comboBox.setCurrentIndex(0)=='':
        # self.comboBox_4.setCurrentIndex(0)
        marca = self.comboBox.currentText ()

        modelosABARTH = ['', '500C', '500', '124 Spider']
        modelosALFAROMEO = ['', 'Giulietta', 'MiTo', '4C', 'Giulia', 'Stelvio']
        modelosBENTLEY = ['', 'Continental GT', 'Mulsanne', 'Flying Spur', 'Continental GTC', 'Bentayga']
        modelosBMW = ['', 'Serie 3', 'Serie 5', 'Serie 4', 'Serie 7', 'Z4', 'X5', 'Serie 1', 'X3', 'Serie 6', 'X1',
                      'X6',
                      'I3', 'Serie 2', 'X4', 'I8', 'Serie 2 Gran Tourer', 'Serie 2 Active Tourer', 'X2']
        modelosAudi = ['', 'A4', 'A8', 'A3', 'TT', 'A5', 'A4', 'Allroad', 'Quattro', 'A6', 'A7', 'Q3', 'Q5', 'S5', 'A1',
                       'A6', 'Allroad', 'Quattro', 'S7', 'S6', 'S8', 'RS4', 'RS5', 'R8', 'SQ5', 'Q7', 'RS6', 'RS7',
                       'RS', 'Q3', 'S3', 'S1', 'TTS', 'S4', 'RS3', 'SQ7', 'Q2', 'TTS', 'SQ7', 'S4', "S6", "S7"]
        modelosAstonMartin = ['', 'DB9', 'Vantage V8', 'Vanquish,', 'Vantage V12', 'Rapide']
        modelosBYD = ['', 'E6']
        modelosCHEVROLET = ['', 'Cruze', 'Aveo', 'Trax', 'Orlando', 'Spark', 'Camaro']
        modelosCITROEN = ['', 'C4', 'C3', 'C5', 'C3 Picasso', 'C4 Picasso', 'Grand C4 Picasso', 'C4 Aircross', 'Nemo',
                          'Berlingo', 'C - Elysée', 'C4 Cactus', 'C1', 'C - Zero', 'C - Elysée', 'Spacetourer',
                          'E - Mehari', 'C3 Aircross']
        modeloDACIA = ['', 'Logan', 'Lodgy', 'Sandero', 'Duster', 'Dokker']
        modeloDFSK = ['', 'Serie V', 'Serie K']
        modeloDS = ['', 'DS 4', 'DS 5', 'DS 3', 'DS 4 Crossback', 'DS 7 Crossback']
        modeloFERRARI = ['', '488', 'GTC4', 'California', 'F12', 'Portofino', '812']
        modeloFIAT = ['', 'Freemont', 'Doblò', 'Punto', 'Panda', '500', '500L', '500L', '500X', 'Qubo', 'Fiorino',
                      'Bravo',
                      'Doblò', 'Doblò', '500C', 'Tipo', '124 Spider']
        modeloFORD = ['', 'C - Max', 'Fiesta', 'Focus', 'Mondeo', 'Ka', 'S - MAX', 'B - MAX', 'Grand C - Max',
                      'Tourneo Custom', 'Kuga', 'Galaxy', 'Grand Tourneo Connect', 'Tourneo Connect', 'EcoSport',
                      'Tourneo Courier', 'Mustang', 'Transit Connect', 'Edge', 'Ka+']
        modeloHONDA = ['', 'Accord', 'Jazz', 'Civic', 'CR-V', 'HR-V']
        modeloHYUNDAI = ['', 'I20', 'Ix35', 'Ix20', 'I10', 'Santa Fe', 'Veloster', 'I40', 'Elantra', 'I30',
                         'Grand Santa Fe', 'Genesis', 'H-1 Travel', 'Tucson', 'I20 Active', 'IONIQ', 'Kona']
        modeloINFINITI = ['', 'Q70', 'Q50', 'QX70', 'QX50', 'Q60', 'Q30', 'QX30']
        modeloISUZU = ['', 'D-Max']
        modeloJAGUAR = ['', 'XF', 'Serie XK', 'F-Type', 'XJ', 'XE', 'F-Pace', 'E-Pace']
        modeloKIA = ['', 'Picanto', 'Rio', 'Sportage', 'Venga', 'Optima', 'Ceed', 'Ceed Sportswagon''Carens',
                     'Pro_ceed',
                     'Sorento', 'Soul', 'Niro', 'Soul EV', 'Pro_ceed GT', 'Stonic', 'Optima SW', 'Optima PHEV',
                     'Optima HÃ¯Brido Enchufable', 'Optima SW GT', 'Optima GT', 'Niro HÃ¯Brido Enchufable',
                     'Optima SW HÃ¯Brido Enchufable', 'Stinger']
        modeloLAMBORGHINI = ['', 'Aventador', 'Huracán']
        modeloMASERATI = ['', 'GranCabrio', 'Quattroporte', 'Ghibli', 'GranTurismo', 'Levante']
        modeloMERCEDES = ['', 'Clase SL', 'Clase SLK', 'Clase V', 'Clase C', 'Clase M', 'Clase G', 'Clase E',
                          'Clase CL',
                          'Clase S', 'Clase GLK', 'SLS AMG', 'Clase B', 'Clase A', 'Clase GL', 'Clase CLS', 'Clase CLA',
                          'Clase GLA', 'AMG GT', 'Vito', 'Clase GLE Coupé', 'Clase GLE', 'Clase GLE Coupé', 'Clase GLK',
                          'Clase GLC', 'Citan', 'Clase GLS', 'Clase SLC', 'GLC Coupé', 'Mercedes-AMG GT', 'CLS']

        if marca == "AUDI":
            self.comboBox_4.clear ()
            self.comboBox_4.addItems (modelosAudi)
        elif marca == 'ABARTH':
            self.comboBox_4.clear ()
            self.comboBox_4.addItems (modelosABARTH)
        elif marca == 'ALFA ROMEO':
            self.comboBox_4.clear ()
            self.comboBox_4.addItems (modelosALFAROMEO)
        elif marca == 'BMW':
            self.comboBox_4.clear ()
            self.comboBox_4.addItems (modelosBMW)
        elif marca == 'BYD':
            self.comboBox_4.clear ()
            self.comboBox_4.addItems (modelosBYD)
        elif marca == 'CHEVROLET':
            self.comboBox_4.clear ()
            self.comboBox_4.addItems (modelosCHEVROLET)
        elif marca == 'BENTLEY':
            self.comboBox_4.clear ()
            self.comboBox_4.addItems (modelosBENTLEY)
        elif marca == 'CITROEN':
            self.comboBox_4.clear ()
            self.comboBox_4.addItems (modelosCITROEN)
        elif marca == 'DACIA':
            self.comboBox_4.clear ()
            self.comboBox_4.addItems (modeloDACIA)
        elif marca == 'ASTON MARTIN':
            self.comboBox_4.clear ()
            self.comboBox_4.addItems (modelosAstonMartin)
        elif marca == 'DFSK':
            self.comboBox_4.clear ()
            self.comboBox_4.addItems (modeloDFSK)
        elif marca == 'DS':
            self.comboBox_4.clear ()
            self.comboBox_4.addItems (modeloDS)
        elif marca == 'FERRARI':
            self.comboBox_4.clear ()
            self.comboBox_4.addItems (modeloFERRARI)
        elif marca == 'FIAT':
            self.comboBox_4.clear ()
            self.comboBox_4.addItems (modeloFIAT)
        elif marca == 'FORD':
            self.comboBox_4.clear ()
            self.comboBox_4.addItems (modeloFORD)
        elif marca == 'HONDA':
            self.comboBox_4.clear ()
            self.comboBox_4.addItems (modeloHONDA)
        elif marca == 'HYUNDAI':
            self.comboBox_4.clear ()
            self.comboBox_4.addItems (modeloHYUNDAI)
        elif marca == 'INFINITI':
            self.comboBox_4.clear ()
            self.comboBox_4.addItems (modeloINFINITI)
        elif marca == 'ISUZU':
            self.comboBox_4.clear ()
            self.comboBox_4.addItems (modeloISUZU)
        elif marca == 'JAGUAR':
            self.comboBox_4.clear ()
            self.comboBox_4.addItems (modeloJAGUAR)
        elif marca == 'KIA':
            self.comboBox_4.clear ()
            self.comboBox_4.addItems (modeloKIA)
        elif marca == 'LAMBORGHINI':
            self.comboBox_4.clear ()
            self.comboBox_4.addItems (modeloLAMBORGHINI)
        elif marca == 'MASERATI':
            self.comboBox_4.clear ()
            self.comboBox_4.addItems (modeloMASERATI)
        elif marca == 'MERCEDES':
            self.comboBox_4.clear ()
            self.comboBox_4.addItems (modeloMERCEDES)

    ##  AUTO  ##
    def agregarAuto (self):
        conn = conexion ()
        cursor = conn.cursor ()
        consulta = "SELECT COUNT(id_auto) FROM db_auto"
        cursor.execute (consulta)
        idAut = cursor.fetchall ()[len (cursor.fetchall ())]
        conn.close ()
        idAut = int (list (idAut)[-1]) + 1
        marca = self.comboBox.currentText ()
        modelo = self.comboBox_4.currentText ()
        precio = self.lineEdit_41.text ()
        print (precio)
        print (type (precio))
        condicion = self.comboBox_2.currentText ()
        datoAuto = [idAut, marca, modelo, precio, condicion]
        if marca.strip () == '' or modelo.strip () == '' or precio.strip () == '':
            pass
        else:
            conn = conexion ()
            insertar_base_auto (conn, datoAuto)
            conn.close ()
            self.lineEdit_41.setText ("")
            self.actualizarAuto ()
            self.comboBox.setCurrentIndex (0)
            self.comboBox_4.setCurrentIndex (0)
            self.comboBox_2.setCurrentIndex (0)

    def borrarAuto (self):
        conn = conexion ()
        idBorrar = self.lineEdit_15.text ().lstrip ()

        if not idBorrar.isspace () or idBorrar == '':
            borrar_base_auto (conn, idBorrar)
            conn.close ()
            self.actualizarAuto ()
        else:
            print ("NO se borra NADA de nada! nadita")
        self.lineEdit_15.setText ("")

    def buscarAuto (self):
        idBuscarAuto = self.lineEdit_18.text ().lstrip ()
        if idBuscarAuto == '':
            idBuscarAuto = '0'
        conn = conexion ()
        try:
            dato = Buscar_auto (conn, idBuscarAuto)
            conn.close ()
            # indice = int (idBuscarAuto) - 1
            print ("dato", dato)
            self.label_59.setText (dato[0][1])  # marca
            self.label_60.setText (dato[0][2])  # modelo
            #"$%.2f" % float
            #self.lineEdit_43.setText (str(float(dato[0][3].strip('$','.00'))))  # precio
            print(dato[0][3])
            print (float(dato[0][3].strip("$")))
            print (int(float (dato[0][3].strip ("$"))))

            self.lineEdit_43.setText (str(float (dato[0][3].strip ("$"))))

            self.label_61.setText (dato[0][4])  # condicion
            self.pushButton_16.setEnabled (True)
            if self.lineEdit_43.text ().strip () == '':
                self.pushButton_17.setDisabled (True)

        except IndexError:
            print ("fuera de rango")
            self.lineEdit_18.setText ("")
        except ValueError:
            print ("valor incorrecto")
            self.lineEdit_18.setText ("")

    def modificarAuto (self):
        idMod = self.lineEdit_18.text ()
        precio = self.lineEdit_43.text ()
        datoAuto = [idMod, precio]
        conn = conexion ()
        modificar_auto (conn, datoAuto, idMod)
        conn.close ()
        self.lineEdit_18.setText ('')
        self.label_59.setText ('')
        self.label_60.setText ('')
        self.label_61.setText ('')
        self.lineEdit_43.setText ('')
        self.actualizarAuto ()
        if self.lineEdit_43.text () == '':
            self.pushButton_16.setDisabled (True)

    def actualizarAuto (self):
        conn = sqlite3.connect ('base.db')
        consulta = "SELECT * from db_auto"
        cursor = conn.cursor ()
        resultado = cursor.execute (consulta)
        self.tableWidget_empleado_3.setRowCount (0)
        for row_number, row_data in enumerate (resultado):
            self.tableWidget_empleado_3.insertRow (row_number)
            for column_number, data in enumerate (row_data):
                self.tableWidget_empleado_3.setItem (row_number, column_number, QtWidgets.QTableWidgetItem (str (data)))
        for i in [0, 1, 2, 3, 4]:
            self.tableWidget_empleado_3.resizeColumnToContents (i)

    ##  EMPLEADO  ##
    def agregarEmpleado (self):
        conn = sqlite3.connect ('base.db')
        cursor = conn.cursor ()
        consulta2 = "SELECT COUNT(id_empleado) FROM db_empleado"
        cursor.execute (consulta2)
        idCli = cursor.fetchall ()[len (cursor.fetchall ())]
        conn.close ()
        idCli = int (list (idCli)[-1]) + 1
        nombre = self.lineEdit_nombre_emp.text ()
        apellido = self.lineEdit_apellido_emp.text ()
        domicilio = self.lineEdit_domicilio_emp.text ()
        sueldo = self.lineEdit_sueldo_emp.text ()
        if nombre.strip () == '' or apellido.strip () == '' or domicilio.strip () == '' or sueldo.strip () == '':
            pass
        else:
            datoempleado = [idCli, nombre, apellido, domicilio, sueldo]
            conn = conexion ()
            insertar_base_empleado (conn, datoempleado)
            conn.close ()
            self.lineEdit_nombre_emp.setText ("")
            self.lineEdit_apellido_emp.setText ("")
            self.lineEdit_domicilio_emp.setText ("")
            self.lineEdit_sueldo_emp.setText ("")
            self.actualizarEmpleado ()
            self.comboBox.setCurrentIndex (0)

    def borrarEmpleado (self):
        idBorrar = self.lineEdit_borrar_emp.text ().lstrip ()
        if not (idBorrar.isspace () or idBorrar == ''):
            conn = conexion ()
            borrar_base_empleado (conn, idBorrar)
            conn.close ()
            self.actualizarEmpleado ()
        else:
            print ("NO se borra NADA")
        self.lineEdit_borrar_emp.setText ("")

    def buscarEmpleado (self):
        self.lineEdit_32.setText ('')
        self.lineEdit_33.setText ('')
        self.lineEdit_34.setText ('')
        self.lineEdit_35.setText ('')

        idBuscarEmpleado = self.lineEdit_19.text ()
        conn = conexion ()
        try:
            dato = Buscar_empleado (conn, idBuscarEmpleado)
            conn.close ()
            # indice = int (idBuscarEmpleado) - 1
            self.lineEdit_32.setText (dato[0][1])
            self.lineEdit_33.setText (dato[0][2])
            self.lineEdit_34.setText (dato[0][3])
            self.lineEdit_35.setText (str (dato[0][4]))
            if type (dato[0][1]) == str or type (dato[0][2]) == str or type (dato[0][3]) == str:
                self.pushButton_13.setEnabled (True)
            if self.lineEdit_19.text ().strip () == '':
                self.pushButton_13.setDisabled (True)

            # print(dato[0][4])
        except IndexError:
            print ("Fuera de rango")

    def modificarEmpleado (self):
        conn = conexion ()
        idMod = self.lineEdit_19.text ()
        nombre = self.lineEdit_32.text ()
        apellido = self.lineEdit_33.text ()
        domicilio = self.lineEdit_34.text ()
        sueldo = self.lineEdit_35.text ()
        dato = [nombre, apellido, domicilio, sueldo]
        modificar_empleado (conn, dato, idMod)
        conn.close ()
        self.lineEdit_32.setText ('')
        self.lineEdit_33.setText ('')
        self.lineEdit_34.setText ('')
        self.lineEdit_35.setText ('')
        self.lineEdit_19.setText ('')
        self.actualizarEmpleado ()
        if self.lineEdit_32.text () == '':
            self.pushButton_13.setDisabled (True)

    def actualizarEmpleado (self):
        conn = sqlite3.connect ('base.db')
        consulta = "SELECT * from db_empleado"
        cursor = conn.cursor ()
        resultado = cursor.execute (consulta)
        self.tableWidget_empleado.setRowCount (0)
        for row_number, row_data in enumerate (resultado):
            self.tableWidget_empleado.insertRow (row_number)
            for column_number, data in enumerate (row_data):
                self.tableWidget_empleado.setItem (row_number, column_number,
                                                   QtWidgets.QTableWidgetItem (str (data)))
        for i in [0, 1, 2, 3, 4]:
            self.tableWidget_empleado.resizeColumnToContents (i)

    ##  CLIENTE  ##
    def agregarCliente (self):
        conn = conexion ()
        cursor = conn.cursor ()
        consulta = "SELECT COUNT(id_cliente) FROM db_cliente"
        cursor.execute (consulta)
        idCli = cursor.fetchall ()[len (cursor.fetchall ())]
        conn.close ()
        idCli = int (list (idCli)[-1]) + 1
        nombre = self.lineEdit_25.text ()
        apellido = self.lineEdit_23.text ()
        domicilio = self.lineEdit_24.text ()

        if nombre.strip () == '' or apellido.strip () == '' or domicilio.strip () == '':
            pass
        else:
            datocliente = [idCli, nombre, apellido, domicilio]
            conn = conexion ()
            insertar_base_cliente (conn, datocliente)
            conn.close ()
            self.lineEdit_25.setText ("")
            self.lineEdit_23.setText ("")
            self.lineEdit_24.setText ("")
            self.actualizarCliente ()

    def borrarCliente (self):
        idBorrar = self.lineEdit_14.text ().lstrip ()
        if not idBorrar.isspace () or idBorrar == '':
            conn = conexion ()
            borrar_base_cliente (conn, idBorrar)
            conn.close ()
            self.actualizarCliente ()
        else:
            print ("NO se borra NADA")
        self.lineEdit_14.setText ("")

    def buscarCliente (self):
        self.lineEdit_26.setText ('')
        self.lineEdit_27.setText ('')
        self.lineEdit_28.setText ('')

        idBuscarCliente = self.lineEdit_16.text ()
        conn = conexion ()
        try:
            dato = Buscar_cliente (conn, idBuscarCliente)
            conn.close ()
            # indice = int (idBuscarCliente) - 1
            self.lineEdit_26.setText (dato[0][1])
            self.lineEdit_27.setText (dato[0][2])
            self.lineEdit_28.setText (dato[0][3])
            if self.lineEdit_26.text ().strip () == '':
                self.pushButton_10.setDisabled (True)
            elif type (self.lineEdit_26.text ()) == str:
                self.pushButton_10.setEnabled (True)
        except IndexError:
            print ("fuera de rango")

    def modificarCliente (self):
        idMod = self.lineEdit_16.text ()
        nombre = self.lineEdit_26.text ()
        apellido = self.lineEdit_27.text ()
        domicilio = self.lineEdit_28.text ()
        dato = [nombre, apellido, domicilio]
        conn = conexion ()
        modificar_cliente (conn, dato, idMod)
        conn.close ()
        self.lineEdit_16.setText ('')
        self.lineEdit_26.setText ('')
        self.lineEdit_27.setText ('')
        self.lineEdit_28.setText ('')
        self.actualizarCliente ()
        if self.lineEdit_26.text () == '':
            self.pushButton_10.setDisabled (True)

    def actualizarCliente (self):
        conn = sqlite3.connect ('base.db')
        consulta = "SELECT * from db_cliente"
        cursor = conn.cursor ()
        resultado = cursor.execute (consulta)
        self.tableWidget_clientes.setRowCount (0)
        for row_number, row_data in enumerate (resultado):
            self.tableWidget_clientes.insertRow (row_number)
            for column_number, data in enumerate (row_data):
                self.tableWidget_clientes.setItem (row_number, column_number, QtWidgets.QTableWidgetItem (str (data)))
        for i in [0, 1, 2, 3]:
            self.tableWidget_clientes.resizeColumnToContents (i)

    def buscarClienteAgregar (self):
        nombre = self.lineEdit_25.text ().strip ()
        apellido = self.lineEdit_23.text ().strip ()
        domicilio = self.lineEdit_24.text ().strip ()
        dato = [nombre + '%', apellido + '%', domicilio + '%']
        if dato != ['%', '%', '%']:
            conn = conexion ()
            info = buscar_determinados_clientes (conn, dato)
            self.tableWidget_clientes.setRowCount (0)
            for row_number, row_data in enumerate (info):
                self.tableWidget_clientes.insertRow (row_number)
                for column_number, data in enumerate (row_data):
                    self.tableWidget_clientes.setItem (row_number, column_number,
                                                       QtWidgets.QTableWidgetItem (str (data)))
            conn.close ()
        else:
            pass


class Manual (QtWidgets.QWidget, Ui_Form):
    def __init__ (self, *args):
        QtWidgets.QMainWindow.__init__ (self, *args)
        self.setupUi (self)
        print ("clase MANUAL")


# class MainWindow (QtWidgets.QMainWindow, Ui_MainWindow):
#    def __init__ (self, *args):
#        QtWidgets.QMainWindow.__init__ (self, *args)
#        self.setupUi (self)
#        self.actualizarEmpleado ()


app = QApplication ([])
###BASE DE DATOS###
conn = conexion ()
db_venta (conn)  # conn=connection
db_auto (conn)
db_cliente (conn)
db_empleado (conn)
###BASE DE DATOS###FIN
manual = Manual ()
mainwindow = MainWindow ()
ventas = VerVentas ()
mainwindow.showMaximized ()

print ("Mostrando main")
app.exec_ ()
