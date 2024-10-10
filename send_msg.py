
import requests 
import json 
from datetime import datetime
from fpdf import FPDF
import app
import config




def report_pdf(parada,tipo,string,sum_hoy,rest_hoy,fecha_c):
    fecha = datetime.strftime(datetime.now(),"%Y %m %d - %H:%M:%S") 
    fecha_c=datetime.strftime(datetime.now(),"%Y_%m_%d" ) 
    nombre=[];direccion=[];municipio=[];provincia=[];zona=[]
    cuota=[];cant=[];presidente=[];pago=[];fiador=[]
    datas=app.info_parada(parada)
    for dat in datas:
        nombre=dat[2]
        direccion=dat[3]
        municipio=dat[4]
        provincia=dat[5]
        zona=dat[6] 
    cabeza=app.info_cabecera(parada)
    cuota = cabeza[0]    
    cant = cabeza[1] 
    pago = cabeza[2] 
    presidente = cabeza[3]  
    fiador=cabeza[4]       
    pdf = FPDF(orientation='P',unit='mm',format='Letter')
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_line_width(0.0)
    pdf.rect(7.0, 7.0, 204.0, 265.0)
    pdf.image('./static/images/logo_motoben.png', 20.0, 15.0, link='', type='', w=30.0, h=30.0)
    pdf.set_font('arial', 'B', 12.0)
    pdf.set_xy(60.0, 10.0)
    pdf.cell(w=0.0, h=6.0,ln=1, align='L',  txt=f'Parada:{nombre} ', border=0)
    pdf.set_xy(60.0, 17.0)
    pdf.cell(w=0.0, h=6.0,ln=1, align='L', txt=f'Domicilio:{direccion}', border=0)
    pdf.set_xy(60.0, 23.0)
    pdf.cell(w=0.0, h=6.0, align='L', txt=f'Municipio:{municipio}', border=0)
    pdf.set_xy(60.0, 29.0)
    pdf.cell(w=0.0, h=6.0, align='L', txt=f'Provincia:{provincia}', border=0)
    pdf.set_xy(60.0, 35.0)
    pdf.cell(w=0.0, h=6.0, align='L', txt=f'Zona:{zona}', border=0)
    pdf.set_xy(60.0, 41.0)
    pdf.cell(w=0.0, h=6.0, align='L', txt=f'Codigo:', border=0)  
    pdf.set_xy(80.0, 10.0)
    pdf.cell(w=0.0, h=6.0,txt=f'Fecha:{fecha}', border=0,ln=1,align='R',fill=0)
    pdf.set_xy(80.0, 17.0)
    pdf.cell(w=0.0, h=6.0,txt=f'Aporte por miembro:{cuota} ',border=0,ln=1,align='R',fill=0)
    pdf.set_xy(80.0, 23.0)
    pdf.cell(w=0.0, h=6.0,txt=f'Forma de aporte :{pago} ',border=0,ln=1,align='R',fill=0)
    pdf.set_xy(80.0, 29.0)
    pdf.cell(w=0.0, h=6.0,txt=f'Numero de miembros:{cant}',border=0,ln=1,align='R',fill=0)
    pdf.set_xy(80.0, 35.0)
    pdf.cell(w=0.0, h=6.0,txt=f'Presidente:{presidente}',border=0,ln=1,align='R',fill=0)   
    pdf.set_xy(80.0, 41.0)
    pdf.cell(w=0.0, h=6.0,txt=f'Fiador:{fiador}',border=0,ln=1,align='R',fill=0)
    pdf.set_font('Arial', 'B', 15)
    pdf.set_xy(10.0,50.0)
    pdf.cell(w=0.0, h=10.0,ln=1,align="C", txt= f'RELACION DE APORTE DE MIEMBROS PARA EL-{fecha_c}', border=0)
    pdf.set_font('Times', '', 12)
    pdf.set_y(60)
    pdf.cell(w=30.0, h=10.0, txt='ID',border=1,ln=0,align='C',fill=0)
    pdf.cell(w=90.0, h=10.0, txt='NOMBRE DEL ASOCIADO',border=1,ln=0,align='C',fill=0)
    pdf.cell(w=40.0, h=10.0,txt= 'CEDULA',border=1,ln=0,align='C',fill=0)
    pdf.multi_cell(w=30.0, h=10.0, txt='APORTE',border=1,align='C',fill=0)
    pdf.set_font('arial', '', 11.0)                      
    for valor in string :
                pdf.cell(w=30.0,h= 10.0, txt=str(valor[0]),border=1,ln=0,align='C',fill=0)
                pdf.cell(w=90.0, h=10.0,txt=str(valor[2]),border=1,ln=0,align='L',fill=0)
                pdf.cell(w=40.0, h=10.0,txt=str(valor[3]),border=1,ln=0,align='C',fill=0)
                pdf.multi_cell(w=30.0, h=10.0,txt=str(valor[1]),border=1,align='C',fill=0)
    pdf.ln(5)
    pdf.set_font('arial', 'B', 12.0)
    pdf.cell(w=0.0, h=10.0,txt=f'TOTAL APORTADO RD$ {sum_hoy} ',border=0,ln=1,align='R',fill=0)       
    pdf.cell(w=0.0, h=10.0,txt=f'TOTAL PENDIENTES RD$ {rest_hoy}',border=0,ln=1,align='R',fill=0)  
    pdf.output(f'C:/adm_mariadb/facturas/facturas_{parada}/facturas_{tipo}/cuotas_{fecha_c}.pdf', 'F')   
    archivo=f'C:/adm_mariadb/facturas/facturas_{parada}/facturas_{tipo}/cuotas_{fecha_c}.pdf'
    info_msg=f"Relacion de pagos de cuotas parada:{parada}"
    app.send_mensaje(archivo,config.geremias,config.tokenBot,info_msg)
    app.send_mensaje(archivo,config.moreno,config.tokenBot,info_msg)
    return  


def finanzas_pdf(parada,finanza):
    fecha = datetime.strftime(datetime.now(),"%Y %m %d - %H:%M:%S") 
    fecha_c=datetime.strftime(datetime.now(),"%Y_%m_%d" ) 
    nombre=[];direccion=[];municipio=[];provincia=[];zona=[]
    cuota=[];cant=[];presidente=[];pago=[];fiador=[]
    datas=app.info_parada(parada)
    for dat in datas:
        nombre=dat[2]
        direccion=dat[3]
        municipio=dat[4]
        provincia=dat[5]
        zona=dat[6] 
    cabeza=app.info_cabecera(parada)
    cuota = cabeza[0]    
    cant = cabeza[1] 
    pago = cabeza[2] 
    presidente = cabeza[3]  
    fiador=cabeza[4]       
    pdf = FPDF(orientation='P',unit='mm',format='Letter')
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_line_width(0.0)
    pdf.rect(7.0, 7.0, 204.0, 265.0)
    pdf.image('./static/images/logo_motoben.png', 20.0, 15.0, link='', type='', w=30.0, h=30.0)
    pdf.set_font('arial', 'B', 12.0)
    pdf.set_xy(60.0, 10.0)
    pdf.cell(w=0.0, h=6.0,ln=1, align='L',  txt=f'Parada:{nombre} ', border=0)
    pdf.set_xy(60.0, 17.0)
    pdf.cell(w=0.0, h=6.0,ln=1, align='L', txt=f'Domicilio:{direccion}', border=0)
    pdf.set_xy(60.0, 23.0)
    pdf.cell(w=0.0, h=6.0, align='L', txt=f'Municipio:{municipio}', border=0)
    pdf.set_xy(60.0, 29.0)
    pdf.cell(w=0.0, h=6.0, align='L', txt=f'Provincia:{provincia}', border=0)
    pdf.set_xy(60.0, 35.0)
    pdf.cell(w=0.0, h=6.0, align='L', txt=f'Zona:{zona}', border=0)
    pdf.set_xy(60.0, 41.0)
    pdf.cell(w=0.0, h=6.0, align='L', txt=f'Codigo:', border=0)  
    pdf.set_xy(80.0, 10.0)
    pdf.cell(w=0.0, h=6.0,txt=f'Fecha:{fecha}', border=0,ln=1,align='R',fill=0)
    pdf.set_xy(80.0, 17.0)
    pdf.cell(w=0.0, h=6.0,txt=f'Aporte por miembro:{cuota} ',border=0,ln=1,align='R',fill=0)
    pdf.set_xy(80.0, 23.0)
    pdf.cell(w=0.0, h=6.0,txt=f'Forma de aporte :{pago} ',border=0,ln=1,align='R',fill=0)
    pdf.set_xy(80.0, 29.0)
    pdf.cell(w=0.0, h=6.0,txt=f'Numero de miembros:{cant}',border=0,ln=1,align='R',fill=0)
    pdf.set_xy(80.0, 35.0)
    pdf.cell(w=0.0, h=6.0,txt=f'Presidente:{presidente}',border=0,ln=1,align='R',fill=0)   
    pdf.set_xy(80.0, 41.0)
    pdf.cell(w=0.0, h=6.0,txt=f'Fiador:{fiador}',border=0,ln=1,align='R',fill=0)
    pdf.set_font('Arial', 'B', 15)
    pdf.set_xy(10.0,50.0)
    pdf.cell(w=0.0, h=10.0,ln=1,align="C", txt= f'INFORMACION FINANCIERA DE LA PARADA PARA EL-{fecha_c}', border=0) 
    pdf.set_font('Times', '', 12)
    pdf.set_y(60)
    pdf.cell(w=30.0, h=10.0, txt='ITEM',border=1,ln=0,align='C',fill=0)
    pdf.cell(w=90.0, h=10.0, txt='NOMBRE DEL ITEM',border=1,ln=0,align='C',fill=0)
    pdf.cell(w=40.0, h=10.0,txt= 'MONEDA',border=1,ln=0,align='C',fill=0)
    pdf.multi_cell(w=30.0, h=10.0, txt='VALOR',border=1,align='C',fill=0)
    pdf.set_font('arial', '', 11.0)                      
  
    pdf.cell(w=30.0,h= 10.0, txt='1',border=1,ln=0,align='C',fill=0)
    pdf.cell(w=90.0, h=10.0,txt='BALANCE',border=1,ln=0,align='L',fill=0)
    pdf.cell(w=40.0, h=10.0,txt='RD$',border=1,ln=0,align='C',fill=0)
    pdf.multi_cell(w=30.0, h=10.0,txt=str(finanza[0]),border=1,align='C',fill=0)

    pdf.cell(w=30.0,h= 10.0, txt='2',border=1,ln=0,align='C',fill=0)
    pdf.cell(w=90.0, h=10.0,txt='PRESTAMOS',border=1,ln=0,align='L',fill=0)
    pdf.cell(w=40.0, h=10.0,txt='RD$',border=1,ln=0,align='C',fill=0)
    pdf.multi_cell(w=30.0, h=10.0,txt=str(finanza[1]),border=1,align='C',fill=0)

    pdf.cell(w=30.0,h= 10.0, txt='3',border=1,ln=0,align='C',fill=0)
    pdf.cell(w=90.0, h=10.0,txt='INGRESOS',border=1,ln=0,align='L',fill=0)
    pdf.cell(w=40.0, h=10.0,txt='RD$',border=1,ln=0,align='C',fill=0)
    pdf.multi_cell(w=30.0, h=10.0,txt=str(finanza[2]),border=1,align='C',fill=0)
    
    pdf.cell(w=30.0,h= 10.0, txt='4',border=1,ln=0,align='C',fill=0)
    pdf.cell(w=90.0, h=10.0,txt='GASTOS',border=1,ln=0,align='L',fill=0)
    pdf.cell(w=40.0, h=10.0,txt='RD$',border=1,ln=0,align='C',fill=0)
    pdf.multi_cell(w=30.0, h=10.0,txt=str(finanza[3]),border=1,align='C',fill=0)
    
    pdf.cell(w=30.0,h= 10.0, txt='5',border=1,ln=0,align='C',fill=0)
    pdf.cell(w=90.0, h=10.0,txt='APORTES',border=1,ln=0,align='L',fill=0)
    pdf.cell(w=40.0, h=10.0,txt='RD$',border=1,ln=0,align='C',fill=0)
    pdf.multi_cell(w=30.0, h=10.0,txt=str(finanza[4]),border=1,align='C',fill=0)
    
    pdf.cell(w=30.0,h= 10.0, txt='6',border=1,ln=0,align='C',fill=0)
    pdf.cell(w=90.0, h=10.0,txt='PENDIENTES',border=1,ln=0,align='L',fill=0)
    pdf.cell(w=40.0, h=10.0,txt='RD$',border=1,ln=0,align='C',fill=0)
    pdf.multi_cell(w=30.0, h=10.0,txt=str(finanza[5]),border=1,align='C',fill=0)
    
    pdf.cell(w=30.0,h= 10.0, txt='7',border=1,ln=0,align='C',fill=0)
    pdf.cell(w=90.0, h=10.0,txt='ABONOS',border=1,ln=0,align='L',fill=0)
    pdf.cell(w=40.0, h=10.0,txt='RD$',border=1,ln=0,align='C',fill=0)
    pdf.multi_cell(w=30.0, h=10.0,txt=str(finanza[6]),border=1,align='C',fill=0)
    
    pdf.cell(w=30.0,h= 10.0, txt='8',border=1,ln=0,align='C',fill=0)
    pdf.cell(w=90.0, h=10.0,txt='BALANCE EN BANCO',border=1,ln=0,align='L',fill=0)
    pdf.cell(w=40.0, h=10.0,txt='RD$',border=1,ln=0,align='C',fill=0)
    pdf.multi_cell(w=30.0, h=10.0,txt=str(finanza[7]),border=1,align='C',fill=0)
                                
    pdf.output(f'C:/adm_mariadb/facturas/facturas_{parada}/facturas_finanzas/finanza_{fecha_c}.pdf', 'F')   
    archivo=f'C:/adm_mariadb/facturas/facturas_{parada}/facturas_finanzas/finanza_{fecha_c}.pdf'
    info_msg=f"Actualidad Financiera de la parada:{parada}"
    #app.send_mensaje(archivo,config.geremias,config.tokenBot,info_msg)
    app.send_mensaje(archivo,config.moreno,config.tokenBot,info_msg)
    return

def miembros_pdf(parada,miembros):
    nombre=[];direccion=[];municipio=[];provincia=[];zona=[]
    cuota=[];cant=[];presidente=[];pago=[];fiador=[]
    datas=app.info_parada(parada)
    for dat in datas:
        nombre=dat[2]
        direccion=dat[3]
        municipio=dat[4]
        provincia=dat[5]
        zona=dat[6] 
    cabeza=app.info_cabecera(parada)
    cuota = cabeza[0]    
    cant = cabeza[1] 
    pago = cabeza[2] 
    presidente = cabeza[3]  
    fiador=cabeza[4]     
    fecha = datetime.strftime(datetime.now(),"%Y %m %d - %H:%M:%S") 
    fecha_c=datetime.strftime(datetime.now(),"%Y_%m_%d" ) 
   
    pdf = FPDF(orientation='P',unit='mm',format='Letter')
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_line_width(0.0)
    pdf.rect(7.0, 7.0, 204.0, 265.0)
    pdf.image('./static/images/logo_motoben.png', 20.0, 15.0, link='', type='', w=30.0, h=30.0)      
    #pdf.set_y(-15)
    #pdf.set_font('Arial', 'I', 8)
    #pdf.cell(0, 10, 'Page ' + str(pdf.page_no()) + '/{nb}', 0, 1, 'C')
    pdf.set_font('Arial', 'B', 15)
    pdf.set_xy(10.0,50.0)
    pdf.cell(w=0.0, h=10.0,ln=1,align="C", txt= f'LISTADOS DE MIEMBROS Y SU FUNCION-{fecha_c}', border=0)
    pdf.set_font('arial', 'B', 12.0)
    pdf.set_xy(60.0, 10.0)
    pdf.cell(w=0.0, h=6.0,ln=1, align='L',  txt=f'Parada:{nombre} ', border=0)
    pdf.set_xy(60.0, 17.0)
    pdf.cell(w=0.0, h=6.0,ln=1, align='L', txt=f'Domicilio:{direccion}', border=0)
    pdf.set_xy(60.0, 23.0)
    pdf.cell(w=0.0, h=6.0, align='L', txt=f'Municipio:{municipio}', border=0)
    pdf.set_xy(60.0, 29.0)
    pdf.cell(w=0.0, h=6.0, align='L', txt=f'Provincia:{provincia}', border=0)
    pdf.set_xy(60.0, 35.0)
    pdf.cell(w=0.0, h=6.0, align='L', txt=f'Zona:{zona}', border=0)
    pdf.set_xy(60.0, 41.0)
    pdf.cell(w=0.0, h=6.0, align='L', txt=f'Codigo:', border=0)
    
    pdf.set_xy(80.0, 10.0)
    pdf.cell(w=0.0, h=6.0,txt=f'Fecha:{fecha}', border=0,ln=1,align='R',fill=0)
    pdf.set_xy(80.0, 17.0)
    pdf.cell(w=0.0, h=6.0,txt=f'Aporte por miembro:{cuota} ',border=0,ln=1,align='R',fill=0)
    pdf.set_xy(80.0, 23.0)
    pdf.cell(w=0.0, h=6.0,txt=f'Forma de aporte :{pago} ',border=0,ln=1,align='R',fill=0)
    pdf.set_xy(80.0, 29.0)
    pdf.cell(w=0.0, h=6.0,txt=f'Numero de miembros:{cant}',border=0,ln=1,align='R',fill=0)
    pdf.set_xy(80.0, 35.0)
    pdf.cell(w=0.0, h=6.0,txt=f'Presidente:{presidente}',border=0,ln=1,align='R',fill=0)   
    pdf.set_xy(80.0, 41.0)
    pdf.cell(w=0.0, h=6.0,txt=f'Fiador:{fiador}',border=0,ln=1,align='R',fill=0) 
    pdf.set_font('Times', '', 12)
    pdf.set_y(60)
    pdf.cell(w=30.0, h=10.0, txt='ITEM',border=1,ln=0,align='C',fill=0)
    pdf.cell(w=90.0, h=10.0, txt='NOMBRE DEL ASOCIADO',border=1,ln=0,align='C',fill=0)
    pdf.cell(w=40.0, h=10.0,txt= 'CEDULA',border=1,ln=0,align='C',fill=0)
    pdf.multi_cell(w=30.0, h=10.0, txt='FUNCION',border=1,align='C',fill=0)
    pdf.set_font('arial', '', 11.0)                      
    for valor in miembros :
                pdf.cell(w=30.0,h= 10.0, txt=str(valor[0]),border=1,ln=0,align='C',fill=0)
                pdf.cell(w=90.0, h=10.0,txt=str(valor[1]),border=1,ln=0,align='L',fill=0)
                pdf.cell(w=40.0, h=10.0,txt=str(valor[2]),border=1,ln=0,align='C',fill=0)
                pdf.multi_cell(w=30.0, h=10.0,txt=str(valor[4]),border=1,align='C',fill=0)
   
    pdf.output(f'C:/adm_mariadb/facturas/facturas_{parada}/lista_miembros/lista_{fecha_c}.pdf', 'F')   
    archivo=f'C:/adm_mariadb/facturas/facturas_{parada}/lista_miembros/lista_{fecha_c}.pdf'
    info_msg=f"Relacion de Miembros parada:{parada}"
    app.send_mensaje(archivo,config.moreno,config.tokenBot,info_msg)
    return 

def gastos_pdf(parada,gasto):
    nombre=[];direccion=[];municipio=[];provincia=[];zona=[]
    cuota=[];cant=[];presidente=[];pago=[];fiador=[]
    datas=app.info_parada(parada)
    for dat in datas:
        nombre=dat[2]
        direccion=dat[3]
        municipio=dat[4]
        provincia=dat[5]
        zona=dat[6] 
    cabeza=app.info_cabecera(parada)
    cuota = cabeza[0]    
    cant = cabeza[1] 
    pago = cabeza[2] 
    presidente = cabeza[3]  
    fiador=cabeza[4]     
    fecha = datetime.strftime(datetime.now(),"%Y %m %d - %H:%M:%S") 
    fecha_c=datetime.strftime(datetime.now(),"%Y_%m_%d" ) 
   
    pdf = FPDF(orientation='P',unit='mm',format='Letter')
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_line_width(0.0)
    pdf.rect(7.0, 7.0, 204.0, 265.0)
    pdf.image('./static/images/logo_motoben.png', 20.0, 15.0, link='', type='', w=30.0, h=30.0)      
    #pdf.set_y(-15)
    #pdf.set_font('Arial', 'I', 8)
    #pdf.cell(0, 10, 'Page ' + str(pdf.page_no()) + '/{nb}', 0, 1, 'C')
    pdf.set_font('Arial', 'B', 15)
    pdf.set_xy(10.0,50.0)
    pdf.cell(w=0.0, h=10.0,ln=1,align="C", txt= f'LISTADOS DE MIEMBROS Y SU FUNCION-{fecha_c}', border=0)
    pdf.set_font('arial', 'B', 12.0)
    pdf.set_xy(60.0, 10.0)
    pdf.cell(w=0.0, h=6.0,ln=1, align='L',  txt=f'Parada:{nombre} ', border=0)
    pdf.set_xy(60.0, 17.0)
    pdf.cell(w=0.0, h=6.0,ln=1, align='L', txt=f'Domicilio:{direccion}', border=0)
    pdf.set_xy(60.0, 23.0)
    pdf.cell(w=0.0, h=6.0, align='L', txt=f'Municipio:{municipio}', border=0)
    pdf.set_xy(60.0, 29.0)
    pdf.cell(w=0.0, h=6.0, align='L', txt=f'Provincia:{provincia}', border=0)
    pdf.set_xy(60.0, 35.0)
    pdf.cell(w=0.0, h=6.0, align='L', txt=f'Zona:{zona}', border=0)
    pdf.set_xy(60.0, 41.0)
    pdf.cell(w=0.0, h=6.0, align='L', txt=f'Codigo:', border=0)
    
    pdf.set_xy(80.0, 10.0)
    pdf.cell(w=0.0, h=6.0,txt=f'Fecha:{fecha}', border=0,ln=1,align='R',fill=0)
    pdf.set_xy(80.0, 17.0)
    pdf.cell(w=0.0, h=6.0,txt=f'Aporte por miembro:{cuota} ',border=0,ln=1,align='R',fill=0)
    pdf.set_xy(80.0, 23.0)
    pdf.cell(w=0.0, h=6.0,txt=f'Forma de aporte :{pago} ',border=0,ln=1,align='R',fill=0)
    pdf.set_xy(80.0, 29.0)
    pdf.cell(w=0.0, h=6.0,txt=f'Numero de miembros:{cant}',border=0,ln=1,align='R',fill=0)
    pdf.set_xy(80.0, 35.0)
    pdf.cell(w=0.0, h=6.0,txt=f'Presidente:{presidente}',border=0,ln=1,align='R',fill=0)   
    pdf.set_xy(80.0, 41.0)
    pdf.cell(w=0.0, h=6.0,txt=f'Fiador:{fiador}',border=0,ln=1,align='R',fill=0) 
    pdf.set_font('Times', '', 12)
    pdf.set_y(60)


def ingresos_pdf(parada,ingresos):
    fecha = datetime.strftime(datetime.now(),"%Y %m %d - %H:%M:%S") 
    fecha_c=datetime.strftime(datetime.now(),"%Y_%m_%d" ) 
    nombre=[];direccion=[];municipio=[];provincia=[];zona=[]
    cuota=[];cant=[];presidente=[];pago=[];fiador=[]
    datas=app.info_parada(parada)
    for dat in datas:
        nombre=dat[2]
        direccion=dat[3]
        municipio=dat[4]
        provincia=dat[5]
        zona=dat[6] 
    cabeza=app.info_cabecera(parada)
    cuota = cabeza[0]    
    cant = cabeza[1] 
    pago = cabeza[2] 
    presidente = cabeza[3]  
    fiador=cabeza[4]       
    pdf = FPDF(orientation='P',unit='mm',format='Letter')
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_line_width(0.0)
    pdf.rect(7.0, 7.0, 204.0, 265.0)
    pdf.image('./static/images/logo_motoben.png', 20.0, 15.0, link='', type='', w=30.0, h=30.0)
    pdf.set_font('arial', 'B', 12.0)
    pdf.set_xy(60.0, 10.0)
    pdf.cell(w=0.0, h=6.0,ln=1, align='L',  txt=f'Parada:{nombre} ', border=0)
    pdf.set_xy(60.0, 17.0)
    pdf.cell(w=0.0, h=6.0,ln=1, align='L', txt=f'Domicilio:{direccion}', border=0)
    pdf.set_xy(60.0, 23.0)
    pdf.cell(w=0.0, h=6.0, align='L', txt=f'Municipio:{municipio}', border=0)
    pdf.set_xy(60.0, 29.0)
    pdf.cell(w=0.0, h=6.0, align='L', txt=f'Provincia:{provincia}', border=0)
    pdf.set_xy(60.0, 35.0)
    pdf.cell(w=0.0, h=6.0, align='L', txt=f'Zona:{zona}', border=0)
    pdf.set_xy(60.0, 41.0)
    pdf.cell(w=0.0, h=6.0, align='L', txt=f'Codigo:', border=0)  
    pdf.set_xy(80.0, 10.0)
    pdf.cell(w=0.0, h=6.0,txt=f'Fecha:{fecha}', border=0,ln=1,align='R',fill=0)
    pdf.set_xy(80.0, 17.0)
    pdf.cell(w=0.0, h=6.0,txt=f'Aporte por miembro:{cuota} ',border=0,ln=1,align='R',fill=0)
    pdf.set_xy(80.0, 23.0)
    pdf.cell(w=0.0, h=6.0,txt=f'Forma de aporte :{pago} ',border=0,ln=1,align='R',fill=0)
    pdf.set_xy(80.0, 29.0)
    pdf.cell(w=0.0, h=6.0,txt=f'Numero de miembros:{cant}',border=0,ln=1,align='R',fill=0)
    pdf.set_xy(80.0, 35.0)
    pdf.cell(w=0.0, h=6.0,txt=f'Presidente:{presidente}',border=0,ln=1,align='R',fill=0)   
    pdf.set_xy(80.0, 41.0)
    pdf.cell(w=0.0, h=6.0,txt=f'Fiador:{fiador}',border=0,ln=1,align='R',fill=0)
    pdf.set_font('Arial', 'B', 15)
    pdf.set_xy(10.0,50.0)
    pdf.cell(w=0.0, h=10.0,ln=1,align="C", txt= f'RECIBO DE INGRESOS DE LA PARADA PARA EL-{fecha_c}', border=0) 
    pdf.set_font('Times', '', 12)
    pdf.set_y(60)
    
    pdf.output(f'C:/adm_mariadb/facturas/facturas_{parada}/facturas_ingresos/ingreso_{fecha}_.pdf', 'F')
    #os.system(f'C:/adm_mariadb/facturas/facturas_{parada}/facturas_{tipo.lower()}/factura_{fecha}_.pdf')
    archivo=f'C:/adm_mariadb/facturas/facturas_{parada}/facturas_ingresos/ingreso_{fecha}_.pdf'
    info_msg=f"Comprovante de ingresos de la parada:{parada}"
    #app.send_mensaje(archivo,config.geremias,config.tokenBot,info_msg)
    app.send_mensaje(archivo,config.moreno,config.tokenBot,info_msg)     
    return

def prestamos_pdf(parada,beneficiado):
    fecha = datetime.strftime(datetime.now(),"%Y %m %d - %H:%M:%S") 
    fecha_c=datetime.strftime(datetime.now(),"%Y_%m_%d" ) 
    nombre=[];direccion=[];municipio=[];provincia=[];zona=[]
    cuota=[];cant=[];presidente=[];pago=[];fiador=[]
    datas=app.info_parada(parada)
    for dat in datas:
        nombre=dat[2]
        direccion=dat[3]
        municipio=dat[4]
        provincia=dat[5]
        zona=dat[6] 
    cabeza=app.info_cabecera(parada)
    cuota = cabeza[0]    
    cant = cabeza[1] 
    pago = cabeza[2] 
    presidente = cabeza[3]  
    fiador=cabeza[4]       
    pdf = FPDF(orientation='P',unit='mm',format='Letter')
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_line_width(0.0)
    pdf.rect(7.0, 7.0, 204.0, 265.0)
    pdf.image('./static/images/logo_motoben.png', 20.0, 15.0, link='', type='', w=30.0, h=30.0)
    pdf.set_font('arial', 'B', 12.0)
    pdf.set_xy(60.0, 10.0)
    pdf.cell(w=0.0, h=6.0,ln=1, align='L',  txt=f'Parada:{nombre} ', border=0)
    pdf.set_xy(60.0, 17.0)
    pdf.cell(w=0.0, h=6.0,ln=1, align='L', txt=f'Domicilio:{direccion}', border=0)
    pdf.set_xy(60.0, 23.0)
    pdf.cell(w=0.0, h=6.0, align='L', txt=f'Municipio:{municipio}', border=0)
    pdf.set_xy(60.0, 29.0)
    pdf.cell(w=0.0, h=6.0, align='L', txt=f'Provincia:{provincia}', border=0)
    pdf.set_xy(60.0, 35.0)
    pdf.cell(w=0.0, h=6.0, align='L', txt=f'Zona:{zona}', border=0)
    pdf.set_xy(60.0, 41.0)
    pdf.cell(w=0.0, h=6.0, align='L', txt=f'Codigo:', border=0)  
    pdf.set_xy(80.0, 10.0)
    pdf.cell(w=0.0, h=6.0,txt=f'Fecha:{fecha}', border=0,ln=1,align='R',fill=0)
    pdf.set_xy(80.0, 17.0)
    pdf.cell(w=0.0, h=6.0,txt=f'Aporte por miembro:{cuota} ',border=0,ln=1,align='R',fill=0)
    pdf.set_xy(80.0, 23.0)
    pdf.cell(w=0.0, h=6.0,txt=f'Forma de aporte :{pago} ',border=0,ln=1,align='R',fill=0)
    pdf.set_xy(80.0, 29.0)
    pdf.cell(w=0.0, h=6.0,txt=f'Numero de miembros:{cant}',border=0,ln=1,align='R',fill=0)
    pdf.set_xy(80.0, 35.0)
    pdf.cell(w=0.0, h=6.0,txt=f'Presidente:{presidente}',border=0,ln=1,align='R',fill=0)   
    pdf.set_xy(80.0, 41.0)
    pdf.cell(w=0.0, h=6.0,txt=f'Fiador:{fiador}',border=0,ln=1,align='R',fill=0)
    pdf.set_font('Arial', 'B', 15)
    pdf.set_xy(10.0,50.0)
    pdf.cell(w=0.0, h=10.0,ln=1,align="C", txt= f'COMPROBANTE DE PRESTAMOS A FAVOR DE {beneficiado} en fecha-{fecha_c}', border=0) 
    pdf.set_font('Times', '', 12)
    pdf.set_y(60)
    
    pdf.output(f'C:/adm_mariadb/facturas/facturas_{parada}/facturas_prestamos/prestamo_{fecha}_.pdf', 'F')
    #os.system(f'C:/adm_mariadb/facturas/facturas_{parada}/facturas_{tipo.lower()}/factura_{fecha}_.pdf')
    archivo=f'C:/adm_mariadb/facturas/facturas_{parada}/facturas_prestamos/prestamo_{fecha}_.pdf'
    info_msg=f"Comprovante de ingresos de la parada:{parada}"
    #app.send_mensaje(archivo,config.geremias,config.tokenBot,info_msg)
    app.send_mensaje(archivo,config.moreno,config.tokenBot,info_msg)     
    return



def send_telegram_message(message: str, moreno: str, tokenBot):  
    proxies = None  
    headers = {'Content-Type': 'application/json', 'Proxy-Authorization': 'Basic base64'} 
    data_dict = {'chat_id': moreno, 'Document': message, 'parse_mode': 'HTML', 'disable_notification': True}
    data = json.dumps(data_dict) 
    url = f'https://api.telegram.org/bot{tokenBot}/sendDocument' 
    response = requests.post(url, data=data, headers=headers, proxies=proxies, verify=False) 
    return response 