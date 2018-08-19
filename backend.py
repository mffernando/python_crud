#improt sqlite3
import sqlite3 as sql

class TransactionObject():
    database   = "customers.db"
    connection = None
    cursor     = None
    connected  = None

#database connection
    def connect(self):
        TransactionObject.connection = sql.connect(TransactionObject.database)
        TransactionObject.cursor     = TransactionObject.connection.cursor()
        TransactionObject.connected  = True

#database disconnection
    def disconnect(self):
        TransactionObject.connection.close()
        TransactionObject.connected = False

#sql execution
    def execute(self, sql, parameters = None):
        if TransactionObject.connected:
            if parameters == None:
                TransactionObject.cursor.execute(sql)
            else:
                    TransactionObject.cursor.execute(sql, parameters)
            return True
        else:
            return False

#select command
    def fetchall(self):
        return TransactionObject.cursor.fetchall()

#commit
    def persist(self):
        if TransactionObject.connected:
            TransactionObject.connection.commit()
            return True
        else:
            return False

#create table customers if not exists
    def initdatabase():
        transactionobject = TransactionObject()
        transactionobject.connect()
        transactionobject.execute("CREATE TABLE IF NOT EXISTS Customers (id INTEGER PRIMARY KEY, firstname TEXT, lastname TEXT, email TEXT, cpf TEXT)")
        transactionobject.persist()
        transactionobject.disconnect()
    initdatabase()

#view select from table
    def view(self):
        transactionobject = TransactionObject()
        transactionobject.connect()
        transactionobject.execute("SELECT * FROM customers")
        rows = transactionobject.fetchall()
        transactionobject.disconnect()
        return rows

#insert values into table
    def insert(self, firstname, lastname, email, cpf):
        transactionobject = TransactionObject()
        transactionobject.connect()
        transactionobject.execute("INSERT INTO customers VALUES ?, ?, ?, ?", (firstname, lastname, email, cpf))
        transactionobject.persist()
        transactionobject.disconnect()

#search values into table
    def search(self, firstname="", lastname="", email="", cpf=""):
        transactionobject = TransactionObject()
        transactionobject.connect()
        transactionobject.execute("SELECT * FROM customers WHERE firstname=? OR lastname=? OR email=? OR cpf=?", (firstname, lastname, email, cpf))
        rows = transactionobject.fetchall()
        transactionobject.disconnect()
        return rows

#update values into table
    def update(self, id, firstname, lastname, email, cpf):
        transactionobject = TransactionObject()
        transactionobject.connect()
        transactionobject.execute("UPDATE customers SET firstname=?, lastname=?, email=?, cpf=? WHERE id=?", (firstname, lastname, email, cpf, id))
        transactionobject.persist()
        transactionobject.disconnect()

#delete values from table
    def delete(self, id):
        transactionobject = TransactionObject()
        transactionobject.connect()
        transactionobject.execute("DELETE FROM customers WHERE id=?", (id))
        transactionobject.persist()
        transactionobject.disconnect()