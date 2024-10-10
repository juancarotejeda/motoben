

import bbdd


def verificacion(n_parada,n_cedula,password) :
    clave=[]
    query=f"SELECT password FROM tabla_index  WHERE nombre = '{n_parada}'" 
    ident=bbdd.consultar_db(query)
    if ident !=[]:  
      for valor in ident:
         clave=valor[0]
      query=f"SELECT  cedula FROM {n_parada} WHERE cedula = '{n_cedula}'"
      result=bbdd.consultar_db(query) 
      if result != []:                
            if password == clave:  
              return True        
      else:
        return False
    else:
      return False
    
def adm_verificacion(parada,adm_d,adm_p):
    clave=[]
    query=f"SELECT adm_password FROM tabla_index  WHERE nombre = '{parada}'" 
    ident=bbdd.consultar_db(query)
    for dato in ident:
      clave = dato[0]
    if clave == adm_p :
      query=f"SELECT cedula FROM {parada}  WHERE funcion = 'Presidente'" 
      ids=bbdd.consultar_db(query)
      for idx in ids: 
        id=idx[0] 
      if id == adm_d:
        return True 
    else:
       return False 
   
        
def listado_paradas():
    query="SELECT nombre FROM tabla_index " 
    db_paradas=bbdd.consultar_db(query)       
    return db_paradas

def info_parada(parada):
    query=f"SELECT * FROM  tabla_index  WHERE nombre='{parada}'" 
    infos=bbdd.consultar_db(query)      
    return infos

def info_cabecera(parada):
    presidente=[]
    veedor=[]
    cuota=[]
    pago=[]
    cant=[]
    query=f"SELECT cuota, pago FROM tabla_index WHERE nombre = '{parada}'"
    resp=bbdd.consultar_db(query)
    for repueta in resp:
      cuota=repueta[0]  
      pago=repueta[1]
             
    query=f'SELECT nombre FROM {parada}'
    seleccion=bbdd.consultar_db(query)
    cant=len(seleccion)
        
    query=f'SELECT nombre FROM {parada}  WHERE funcion = "Presidente"'   
    press=bbdd.consultar_db(query)
    for pres in press:
      presidente=pres[0] 
     
    query=f'SELECT nombre FROM {parada}  WHERE funcion = "Veedor"'   
    presd=bbdd.consultar_db(query)
    for prex in presd:
      veedor=prex[0] 
                   
    return (cuota,cant,pago,presidente,veedor)        

def lista_miembros(parada):
    listas=[]
    query=f"SELECT codigo, nombre, cedula, telefono, funcion FROM {parada}"
    miembros=bbdd.consultar_db(query)
    for miembro in miembros: 
        listas+=miembro
    lista=dividir_lista(listas,5)    
    return lista
    
def diario_general(parada):
    prestamos=[]
    ingresos=[]
    gastos=[]
    aporte=[]
    pendiente=[]
    abonos=[]
    balance_bancario=[]
    query = f"SELECT  prestamos, ingresos, gastos, aporte, pendiente, abonos, balance_banco FROM tabla_index WHERE nombre='{parada}' "   
    consult=bbdd.consultar_db(query)
    for valor in consult:
      prestamos=valor[0]
      ingresos=valor[1]
      gastos=valor[2]
      aporte=valor[3]
      pendiente=valor[4]
      abonos=valor[5]
      balance_bancario=valor[6]
    balance=(aporte + ingresos + abonos )-(gastos+prestamos)
    data=(balance,prestamos,ingresos,gastos,aporte,pendiente,abonos,balance_bancario)   
    return data

def dividir_lista(lista,lon) : 
    return [lista[n:n+lon] for n in range(0,len(lista),lon)]     


def aportacion(parada):                
    query=f"SELECT codigo, nombre, cedula, telefono, funcion FROM {parada}"
    data=bbdd.consultar_db(query)
    return data