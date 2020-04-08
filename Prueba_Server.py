import pyodbc 

servidor = 'LAPTOP-JRUPDFPR\SQLEXPRESS'  # Nombre del servidor SQL con el cual se hará la conexión
bddatos = 'Tasty_server'  # Nombre de la base de datos SQL
puerto = '1433'
usuario = 'prueba' # Nombre del usuario de SQL
clave = '00159753'  # Contraseña del usuario de SQL
conn = pyodbc.connect('DRIVER={SQL Server};'
                       'SERVER='+servidor+';'
                       'DATABASE='+bddatos+';'
                       'UID='+usuario+';'
                       'PWD='+clave+'')

def run_queryServer (consulta = "",parametro=0):
    consulta = consulta
    parametro = parametro
    cursor = conn.cursor ()
    cursor.execute (consulta+parametro)
    return cursor


def run_queryServer2 (consulta = ""):
    consulta = consulta
    cursor = conn.cursor ()
    devol = cursor.execute (consulta)
    for cur in cursor: 
        print (cur)
    cursor.commit ()
    return cursor

def run_queryServer3 (consulta = "",parametro=''):
    consulta = consulta
    parametro = parametro
    cursor = conn.cursor ()
    cursor.executemany (consulta,parametro)
    cursor.commit ()
    return cursor

def run_queryServer4 (consulta = ""):
    consulta = consulta
    cursor = conn.cursor ()
    devol = cursor.execute (consulta)
    for cur in cursor: 
        return cur

def run_queryServer5 (consulta = ""):
    consulta = consulta
    cursor = conn.cursor ()
    cursor.execute (consulta)
    cursor.commit ()

def run_queryServer6 (consulta = ""):
    consulta = consulta
    cursor = conn.cursor ()
    cursor.execute (consulta)
    cursor.commit ()

def run_queryServer7 (consulta = ""):
    consulta = consulta
    cursor = conn.cursor ()
    devol = cursor.execute (consulta)
    return devol

def run_queryServer8 (consulta = ""):
    consulta = consulta
    cursor = conn.cursor ()
    devol = cursor.execute (consulta)
    for val in devol:
        return val
def cerrar_conexion ():
    conn.close()


