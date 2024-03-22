from PySide6 import QtWidgets, QtSql

class Data:
    def __init__(self):
        super().__init__()

    def create_connection():
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('storage_db.db')

        if not db.open():
            QtWidgets.QMessageBox.critical(None, "Cannot open data base",
                                           "Click Cancel to exit", QtWidgets.QMessageBox.Cancel)
            return False
        
        quary = QtSql.QSqlQuery()
        quary.exec("CRATE TABLE IF NOT EXISTS storage (ID integer primary key AUTOINCREMENT, Name, Quant, Date)")
        return True
    
    def execute_quary_with_params(self, sql_quary, quary_values=None):
        quary = QtSql.QSqlQuery()
        quary.prepare(sql_quary)

        if quary_values is not None:
            for quary_value in quary_values:
                quary.addBindValue(quary_value)
        
        quary.exec()

    def add_new_position_quary(self, name, quant, date):
        sql_quary = "INSERT INTO storage (Name, Quant, Date) VALUES (?, ?, ?)"
        self.execute_quary_with_params(sql_quary, [name, quant, date])
