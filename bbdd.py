import mariadb
import config

def modificar_db(query):
    coneccion= mariadb.connect(**config.conn_params)
    cursor= coneccion.cursor()  
    cursor.execute(query)     
    coneccion.commit()
    return 

    
def consultar_db(query):
    connection= mariadb.connect(**config.conn_params)
    cursor= connection.cursor()
    cursor.execute(query)
    Result= cursor.fetchall() 
    return Result