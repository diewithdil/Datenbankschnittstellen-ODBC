import pyodbc

def getConn ():
    cnxn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                          "Server=141.56.2.45;"
                          "Database=iw21s83792;"
                          "uid=s83792;pwd=s83792")
    return cnxn
