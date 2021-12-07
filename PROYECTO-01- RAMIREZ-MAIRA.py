"""
SANTANDER TECNOLOGÍA: 
CIENCIA DE DATOS | EMTECH-FUNED

Maira Dolores Ramírez Mendiola

Tutor: Jaime Saúl Alonso Sánchez
Grupo: ANALISTAS: ADIÓS EXCEL 


"""

from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches

limpiarPantalla = '\n' * 20 #ya que no se cuenta con un comando para limpiar
#la consola se obta por usar esta estrategía


print('⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯LifeStore⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n ')



#LOGIN USUARIO
#primera parte para definir las entradas validas para el acceso


if __name__ == "__main__": 
    USUARIO1 = 'Jimmy'
    CONTRASENA1 = 'ymmij'
    
    USUARIO2='Mai'
    CONTRASENA2 = 'ariam'

#implementando seguridad con un cierre del código para quien 
#no ingrese el acceso de manera correcta

    INTENTOS = 3


    while True: #para que al equivocarse el usuario tenga una nueva 
                #oprtunidad de acceder

        if INTENTOS == 0:
            exit()

        username = input('Ingrese su nombre de usuario:')
        password = input('Ingrese la contraseña: ')

        if username == USUARIO1: #para que el programa corrobore cuales son los 
                                 #accesos permitidos 

            if password == CONTRASENA1:
                print(f"\n\n\nBienvenido a LifeStore, {USUARIO1}.\n")
                break

            else:
              INTENTOS = INTENTOS - 1
              print(f'\n!! Accesso invalido, {INTENTOS} intentos restantes !!\n')
        
        elif username == USUARIO2: 

            if password == CONTRASENA2:
                print(f"\n\n\nBienvenido a LifeStore, {USUARIO2}.\n")

                break

            else:
              INTENTOS = INTENTOS - 1
              print(f'\n!! Accesso invalido, {INTENTOS} intentos restantes !!\n')
        
        
        else:
            INTENTOS = INTENTOS - 1

            print(f'\n!! Usuario incorrecto, {INTENTOS} intentos restantes !!\n')

    print('▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄\n')
    
    


#se definen las cedanas de texto a buscar para poder divir la lista por meses
meses = ['/01/', '/02/', '/03/','/04/','/05/','/06/','/07/', '/08/', '/09/', 
         '/10/','/11/','/12/']

mes_nombre=['ENERO', 'FEBRERO', 'MARZO','ABRIL','MAYO','JUNIO','JULIO', 
            'AGOSTO', 'SEPTIEMBRE', 'OCTUBRE', 'NOVIEMBRE', 'DICIEMBRE']

cantidad_prod=len(lifestore_products) #para saber cuantos productos maneja 
                                      #LifeStore ya que esto nos especificara 
                                      #el tamaño de las buslistas para cada 
                                      #consigna.

#para hacer interactivo el codigo es necesario preguntarle al usuario cuales 
#son las opciones que quiere revisar 

mes=int(input('Ingrese el número del mes que desee consultar: '))
print('\n════════════════════════════════════════════════════════════════════\n')
print('                         REPORTE MENSUAL                                ')
print(f'                            {mes_nombre[mes-1]} \n                     ')
print('══════════════════════════════════════════════════════════════════════\n')



print(f'LifeStore cuenta con {cantidad_prod} productos distintos.\n ')

#a
op_elegida=int(input('Introduzca la opción que desee consultar:\n  1.-Ventas\n  2.-Busquedas\n  3.-Reseñas\n>'))


#______________________________________________________________________________

if op_elegida ==1: #VENTAS

#para la utilización del menú es necesario porner condicionales para ejecutar 
#la elección ingresada. 
    contador=0
    prod_ventas = []
    por_mes=[]
    ven_s0 = []
    
    #Este ciclo nos ayuda a generar una lista solo con el mes que deseamos consultar
    for venta in lifestore_sales: 
        fecha_venta = venta[3]
        vendidos=venta[1]
        if meses[mes-1] in fecha_venta:
            contador=contador+1
            por_mes.append(vendidos)

#en este ciclo realizmaos una lista en la cual almacenaremos las ventas ya que
#
    for id in range(cantidad_prod): 
        verdadero_id=id+1 
        renglon= [verdadero_id, 0]
        prod_ventas.append(renglon)
  

    for venta in por_mes:
        id_prod=venta
        prod_ventas[id_prod-1][1]=prod_ventas[id_prod-1][1]+1

    ven_s0 = []
    for j in prod_ventas:
        if j[1] != 0:
            ven_s0.append(j)


    op_elegida1=int(input('Introduzca la opción que desee consultar:\n  1.-Más Vendidos \n  2.Menos Vendidos\n>'))

   
    if op_elegida1==1: #MÁS VENDIDOS
    
        ventas_orden_mayor=sorted(ven_s0, key=lambda x:x[1], reverse=True)
        for i in ventas_orden_mayor[:5]:
            nombrep=lifestore_products[i[0]-1][1]
            print(f'* {nombrep[:20]} con {i[1]} ventas')

    elif op_elegida1==2: #MENOS VENDIDAS
        ventas_orden_menor=sorted(ven_s0, key=lambda x:x[1])
    
        for i in ventas_orden_menor[:5]:
            nombres=lifestore_products[i[0]-1][1]
            print(f'* {nombres[:20]} con {i[1]} ventas')
        
    else:
        print('Opción no valida')
        
#______________________________________________________________________________
elif op_elegida == 2: #Busquedas
    
    prod_busqueda = []
    top_busqueda=[]
    Bus_s0 = []
    cantidad_prod=len(lifestore_products)
         
       
    for id_p in range(cantidad_prod): 
        verdadero_id=id_p+1 
        renglon= [verdadero_id, 0]
        prod_busqueda.append(renglon)
    
    #print(prod_busqueda)
    
    for busq in lifestore_searches:
        prod_busqueda[busq[1]-1][1]=prod_busqueda[busq[1]-1][1]+1
    
    
    for j in prod_busqueda:
       if j[1] != 0:
           Bus_s0.append(j)
    


    op_elegida2=int(input('Introduzca la opción que desee consultar:\n  1.-Más Búscados \n  2.Menos Búscados\n>'))
    
    if op_elegida2==1: #MAS BUSCADOS
        Bus_mayor=sorted(Bus_s0, key=lambda x:x[1], reverse=True)
        
        for i in Bus_mayor[:10]:
            nombrep=lifestore_products[i[0]-1][1]
            print(f'* {nombrep[:20]} con {i[1]} búsquedas')
    
    elif op_elegida2==2: #MENOS BUSCADOS
        Bus_menor=sorted(Bus_s0, key=lambda x:x[1])
        print('no se muestran los que no tienen ninguna búsqueda\n')
        
        for i in Bus_menor[:10]:
            
            nombres=lifestore_products[i[0]-1][1]
            print(f'* {nombres[:20]} con {i[1]} búsqueda')
        
    else:
        print('Opción no valida')      

#______________________________________________________________________________
elif op_elegida == 3: #RESEÑA
    cont=0
    prod_reseñas = []
    por_mes2=[]
    res_final=[]
    op_elegida3=int(input('Introduzca la opción que desee consultar:\n  1.-Con las Mejores Reseñas \n  2.Con las Peores Reseñas\n>'))
    
    for reseña in lifestore_sales: 
        fecha_venta2=reseña[3]
        if meses[mes-1] in fecha_venta2:
            prod_res = [reseña[1], reseña[2]]
            por_mes2.append(prod_res)
    


    
    if op_elegida3==1:
        res_ord=sorted(por_mes2, key=lambda x:x[1], reverse=True)
        for i in res_ord:
            if cont==0: 
                nombrep=lifestore_products[i[0]-1][1]
                res_final.append(f'* {nombrep[:25]} con {i[1]} estrellas')
                
            else: 
                if i[0]!=res_ord[cont-1][0]:
                    nombrep=lifestore_products[i[0]-1][1]
                    res_final.append(f'* {nombrep[:25]} con {i[1]} estrellas')
                
            cont+=1
         
        for j in res_final[:5]:
            print(j) 
            
    elif op_elegida3==2:
        res_ord=sorted(por_mes2, key=lambda x:x[1])
        for i in res_ord:
            if cont==0: 
                nombrep=lifestore_products[i[0]-1][1]
                res_final.append(f'* {nombrep[:25]} con {i[1]} estrellas')
                
            else: 
                if i[0]!=res_ord[cont-1][0]:
                    nombrep=lifestore_products[i[0]-1][1]
                    res_final.append(f'* {nombrep[:25]} con {i[1]} estrellas')
                
            cont+=1
         
        for j in res_final[:5]:
            print(j) 

