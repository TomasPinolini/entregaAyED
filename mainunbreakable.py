# Carpeta que permite ocultar la contraseña al ingresarla.
import getpass

USUARIOS = []

# Carga de los usuarios que utilizarían el programa.
def cargaU(arr):
    us = []
    us.append(1) 
    us.append("admin@shopping.com") 
    us.append("12345") 
    us.append("administrador") 
    arr.append(us)
    us = []
    us.append(4) 
    us.append("localA@shopping.com") 
    us.append("AAAA1111") 
    us.append("dueño") 
    arr.append(us)    
    us = []
    us.append(6) 
    us.append("localB@shopping.com") 
    us.append("BBBB2222") 
    us.append("dueño") 
    arr.append(us)
    us = []
    us.append(9) 
    us.append("unCliente@shopping.com") 
    us.append("33xx33") 
    us.append("cliente") 
    arr.append(us)
    us = []
    us.append(10) 
    us.append("1") 
    us.append("2") 
    us.append("administrador") 
    arr.append(us)
    
# Declaración de contadores de rubros, y de auxiliares para la validación de usuario.  
intentos = 1
aux = 0
tdc = ""
codu = 0
locales = [[0, 0, 0, 0, 0, 0, "B"]]*50
c = 0
# ind = 0
# perf = 0
# com = 0   
a = 0
   
cargaU(USUARIOS)

# Procedure de creación de lista con los id de los dueños existentes. 
duenos = [0]*50
for i in USUARIOS:
    if i[3] == "dueño":
        duenos[a] = i[0]
        a = a + 1

def separacion():
    print('-----------------------------------------------------------------------------------------')
  
# Procedures que ordenan listas de manera creciente y decreciente. 
def ordenadoC(N, filas, ref, col):
    for i in range(0, filas-1):
        for j in range(i+1, filas):
            if N[i][ref] > N[j][ref]:
                for k in range(col):
                    aux = N[i][k]
                    N[i][k] = N[j][k]
                    N[j][k] = aux    
    return N

def ordenadoD(N, filas, ref, col):
    for i in range(0, filas-1):
        for j in range(i+1, filas):
            if N[i][ref] < N[j][ref]:
                for k in range(col):
                    aux = N[i][k]
                    N[i][k] = N[j][k]
                    N[j][k] = aux    
    return N
                  
# Menu Principal donde un administrador de local puede hacer lo que quiera.
def menuPrincipalAdmin():
    separacion()
    print('''Opciones de Menú principal de Administradores:

        1- Gestión de locales.
        2- Crear cuenta de dueños de locales.
        3- Aprobar/Denegar solicitudes de cuentas.
        4- Gestión de novedades.
        5- Reporte de utilización de descuentos.
        0- Salir.
        ''')
    separacion()
    eleccion = input("Seleccione una número: ")
    while eleccion != '1' and eleccion != '2' and eleccion != '3' and eleccion != '4' and eleccion != '5' and eleccion != '0':
        print("Elección no válida.")
        eleccion = input("Seleccione una opción: ")
        separacion()
    match eleccion:
        case '0':
            print("Saliendo.")
        case '1':
            gestionDeLocales()
        case '2':
            print("En construcción...")
            menuPrincipalAdmin() 
        case '3':
            print("En construcción...")
            menuPrincipalAdmin()
        case '4':
            gestionDeNovedades()
        case '5':
            print("En construcción...")
            menuPrincipalAdmin()
    separacion()
   
# Localizacion de id de dueños para el ingreso de locales a la lista.    
def buscarLocalD(x,y,z):
    global m
    loc = ordenadoC(x, y, 0, 6)
    com = 0
    fin = c - 1
    while com <= fin:
        med = (com + fin) // 2
        if loc[med][0] == z:
            print(loc[med])
            m = med
            return True
        elif loc[med][0] > z:
            fin = med - 1
        else:
            com = med + 1
    return False

# Procedure donde el usuario modifica algún campo de un local seleccionado previamente.
def modificacion(x,y):
    global duenos
    y = y + 1
    print("1- Nombre: ", x[y][1])
    print("2- Ubicación: ", x[y][2])
    print("3- Rubro: ", x[y][3])
    print("4- Codigo de usuario: ", str(x[y][4]))
    pos = int(input("Dato a modificar? (1,2,3,4): "))
    while pos not in [1,2,3,4]:
        pos = int(input("Dato a modificar? (1,2,3,4): "))
    match pos: 
        case 4:
            codigo = int(input("-> "))   
            while codigo not in duenos or codigo == 0:
                codigo = int(input("->  "))
            x[y][pos] = codigo
        case 3:
            print('''
            a- Indumentaria.
            b- Perfumería.
            c- Gastronomía.
            ''')
            b = input("-> ").lower()
            while b not in ["a", "b", "c"]:
                print('Selección no válida.')
                b = input("-> ").lower()            
            match b:
                case "a":
                    b = "Indumentaria."
                case "b":
                    b = "Perfumería."
                case "c":
                    b = "Gastronomía."  
            x[y][pos] = b
        case 2:
            x[y][pos] = input("-> ")   
        case 1:
            auxN = False
            while auxN == False:
                nombre = input("Ingrese el nombre del nuevo local: ")
                auxN = True
                for i in range(c):
                    if nombre == locales[i][1]:
                        auxN = False
            x[y][pos] = nombre
                
# Procedure que permite al admin administrar nuevos locales.
def gestionDeLocales():   
        global locales, c, ind, perf, com, duenos
        separacion()
        print('''
            Opciones de gestión de locales:
            
                a) Crear locales.
                b) Modificar local.
                c) Eliminar local.
                d) Mapa de locales.
                e) Volver.
        ''')
        separacion()
        
        eleccion = input("Seleccione una opción: ")
        while eleccion != 'a' and eleccion != 'b' and eleccion != 'c' and eleccion != 'd' and eleccion != 'e':
            print("Elección no válida.")
            print("")
            eleccion = input("Seleccione una opción: ")
            
        match eleccion:
            case 'a':
                x = "si"
                while x == "si":  
                    verlos = input("Desea ver los locales ya cargados? Si/No: ").lower()
                    while verlos != 'si' and verlos != 'no':
                        verlos = input("Respuesta inválida, intente de nuevo: ").lower()
                    if verlos == "si":
                        if c == 0:
                            print("Todavía no hay locales cargados...")
                        else:
                            separacion()
                            print("Todos los locales: ")
                            for l in range(c):
                                print(locales[l])
                        separacion()
                    auxN = False
                    while auxN == False:
                        nombre = input("Ingrese el nombre del nuevo local: ")
                        auxN = True
                        for i in range(c):
                            if nombre == locales[i][1]:
                                auxN = False

                    ubicacion = input("Ingrese la ubicación: ")
                    print('''
                        a- Indumentaria.
                        b- Perfumería.
                        c- Gastronomía.
                        ''')
                    rubro = input("Seleccione a que rubro pertenece el local: ").lower()
                    while rubro != 'a' and rubro != 'b' and rubro != 'c':
                        print('Selección no válida.')
                        rubro = input("Seleccione a que rubro pertenece el local: ")                  
                    match rubro:
                        case "a":
                            rubro = "Indumentaria"
                        case "b":
                            rubro = "Perfumería"
                        case "c":
                            rubro = "Gastronomía"
                    
                    au = False
                    while au == False:
                        codD = input("Código de dueño de local: ")
                        try:
                            codD = int(codD)
                        except:
                            pass
                        if codD in duenos and codD != 0:
                            au = True

                    
                    locales[c] = [c+1, nombre, ubicacion, rubro, codD, "A"] 
                    separacion()
                    maxMinLocales(c)
                    c = c + 1
                    locales = ordenadoC(locales, c, 1, 6) 
                    x = input("Si desea seguir cargando locales, escriba 'si': ").lower()
                    while x != 'si' and x != 'no':
                        x = input("Respuesta inválida, intente de nuevo: ").lower()
                        
                print("Redirigiendo al menu principal...")
                menuPrincipalAdmin()
            case 'b':
                x = "si"
                while x == "si":
                    verlos = input("Desea ver los locales ya cargados? Si/No: ").lower()
                    while verlos != 'si' and verlos != 'no':
                        verlos = input("Respuesta inválida, intente de nuevo: ").lower()
                    if verlos == "si":
                        print("Todos los locales: ")
                        for i in range(c): 
                            print(locales[i])
                    
                    m = 0
                    cod = int(input("Código de negocio a modificar: "))
                    enc = buscarLocalD(locales, c, cod)
                    while enc == False:
                        cod = int(input("Código de negocio a modificar: "))
                    if locales[m][5] == "A":
                        modificacion(locales, m)
                    else:
                        print("Desea activar el estado del local? ")
                        el = input("-> ")
                        if el == "si":
                            locales[m][5] = "A"                    
                    locales = ordenadoD(locales, c, 1, 6) 
                    maxMinLocales(c)
                    x = input("Si desea seguir modificando locales, escriba 'si': ").lower()
                print("Redirigiendo al menu principal...")
                menuPrincipalAdmin()
            case 'c': 
                x = "si"
                while x == "si":
                    verlos = input("Desea ver los locales ya cargados? Si/No: ").lower()
                    while verlos != 'si' and verlos != 'no':
                        verlos = input("Respuesta inválida, intente de nuevo: ").lower()
                    locales = ordenadoD(locales, c, 1, 6) 
                    if verlos == "si":
                        print("Todos los locales: ")
                        for l in range(c):
                            print(locales[l])
                    m = 0
                    cod = int(input("Código de negocio a dar de baja: "))
                    enc = buscarLocalD(locales, c, cod)
                    while enc == False:
                        cod = int(input("Código de negocio a dar de baja: "))
                    if locales[m][5] == "A":
                        print("Desea confirmar eliminar el local: ")
                        print(locales[m])
                        elec = input("->  ").lower()
                        if elec == "si":
                            locales[m][5] = "B"
                    else: 
                        print("El local numero:",str(locales[m][0]), locales[m][1],"ya está dado de baja.")
            
                    x = input("Si desea seguir eliminando locales, escriba 'si': ").lower()
                print("Redirigiendo al menu principal...")
                menuPrincipalAdmin()
            case 'd': 
                verlos = input("Desea ver los locales ya cargados? Si/No: ").lower()
                while verlos != 'si' and verlos != 'no':
                    verlos = input("Respuesta inválida, intente de nuevo: ").lower()                
                locales = ordenadoC(locales, c, 1, 6) 
                if verlos == "si":
                    print("Todos los locales: ")
                    for l in range(c):
                        print(locales[l])
                a = 0
                for i in range(10):
                    print("+-+-+-+-+-+")
                    print("|"+str(locales[a][0])+"|"+str(locales[a+1][0])+"|"+str(locales[a+2][0])+"|"+str(locales[a+3][0])+"|"+str(locales[a+4][0])+"|")
                    a = a + 5
                menuPrincipalAdmin()
            case 'e':
                print("Volviendo... ")
                menuPrincipalAdmin()
                           
# Procedure que permite al admin administrar novedades, en construcción.
def gestionDeNovedades():
    print('''
        Opciones de gestion de novedades: 
        
          a- Crear novedades.
          b- Modificar novedades.
          c- Eliminar novedades.
          d- Ver reporte de novedades.
          e- Volver''')
    separacion()
    eleccion = input('Seleccione una opción: ')
    separacion()
    while eleccion != 'a' and eleccion != 'b' and eleccion != 'c' and eleccion != 'd' and eleccion != 'e':
            print("Elección no válida.")
            eleccion = input('Seleccione una opción: ')
            separacion()
    match eleccion:    
        case 'a':
            print('En construcción...')
            gestionDeNovedades()
        case 'b':
            print("En construcción...")
            gestionDeNovedades()
        case 'c':
            print("En construcción...")
            gestionDeNovedades()
        case 'd':
            print("En construcción...")
            gestionDeNovedades()
        case 'e':
            print("Volviedo al menú de administradores...")
            menuPrincipalAdmin()    

# Menu Principal donde un dueño de local puede hacer lo que quiera, todavía en construcción.
def menuPrincipalDue():
    print('''Menu principal para dueños: 
          
        1- Gestión de Descuentos.
          a) Crear descuento para mi local
          b) Modificar descuento de mi local
          c) Eliminar descuento de mi local
          d) Volver
        2- Aceptar / Rechazar pedido de descuento.
        3- Reporte de uso de descuentos.
        0- Salir.
    ''')
    separacion()
    eleccion = input("Seleccione una número: ")
    while eleccion != '1' and eleccion != '2' and eleccion != '3' and eleccion != '0':
        print("Elección no válida.")
        eleccion = input("Seleccione una opción: ")
    match eleccion:
        case '0':
            print("Saliendo.")
            separacion()
        case '1':
            print("En construcción...")
            separacion()
            menuPrincipalDue()
        case '2':
            print("En construcción...")
            separacion()
            menuPrincipalDue()
        case '3':
            print("En construcción...")
            separacion()
            menuPrincipalDue()

# Menu Principal donde un cliente puede hacer lo que quiera, todavía en construcción.
def menuPrincipalCli():
    separacion()
    print('''Menu principal para cliente:
          
        1- Registrarme.
        2- Buscar descuentos en locales.
        3- Solicitar descuento.
        4- Ver novedades.
        0- Salir.
    ''')
    separacion()
    eleccion = input("Seleccione una número: ")
    while eleccion != '1' and eleccion != '2' and eleccion != '3' and eleccion != '4' and eleccion != '0':
        print("Elección no válida.")
        eleccion = input("Seleccione una opción: ")
    match eleccion:
        case '0':
            print("Saliendo.")
        case '1':
            print("En construcción...")
            menuPrincipalCli()
        case '2':
            print("En construcción...")
            menuPrincipalCli()
        case '3':
            print("En construcción...")
            menuPrincipalCli()
        case '4':
            print("En construcción...")
            menuPrincipalCli()
    
# Listado decreciente de los rubros más frecuentes. 
def maxMinLocales(x):
    ind = 0
    perf = 0
    com = 0
    for i in range(x+1):
        match locales[i][3]:
            case "Indumentaria":
                ind = ind + 1
            case "Perfumería":
                perf = perf + 1
            case "Gastronomía":
                com = com + 1
    r = [[1, ind], [2, perf], [3, com]]
    r = ordenadoD(r, 3, 1, 2)
    for i in range(x+1):
        print(str(i+1)+"-", str(locales[i]))
    separacion()
    for i in range(len(r)):
        match r[i][0]:
            case 1:
                print("Indumentaria: ", ind)
            case 2:
                print("Perfumería: ", perf)
            case 3:
                print("Gastronomía: ", com)
                
    separacion()

# Respuesta ante ingreso de datos de usuario.
def validacion():
    separacion()
    global tdc, codU
    usuario_ingresado = input("Usuario: ") 
    contrasena_ingresada = input('Contraseña: ')
    auxU = False
    auxC = False
    aux = False
   
    for user in USUARIOS:
        if user[1] == usuario_ingresado:
            auxU = True
        if user[2] == contrasena_ingresada:
            auxC = True
        if user[1] == usuario_ingresado and user[2] == contrasena_ingresada:
            tdc = user[3]
            codU = user[0] 
            return True
            
    if auxU == False and auxC == True:
        print("Usuario o contraseña incorrecto... Intente de nuevo.")
    elif auxU == True and auxC == False:
        print("Contraseña incorrecta... Intente de nuevo.")
    if auxU == False and auxC == False:
        print("Usuario o contraseña incorrecto... Intente de nuevo.")
        
    if aux == False: return False 
    
validado = validacion()

# Validación de datos de usuario con variables auxiliares.
while intentos < 4:
    if validado:
        aux = 1
        intentos = 5
    elif intentos < 3 and aux == 0:    
        intentos = intentos + 1
        validado = validacion()
    elif intentos == 3 and aux == 0:
        print("Fuera de intentos!")
        intentos = intentos + 1
        separacion()        

# Una vez validado el ingreso, se redirige al usuario al menú correspondiente.
if aux == 1 and intentos == 5:
    print("Ingresando a sistema "+tdc+"!")
    print("Bienvenido!")
    match tdc:
        case "administrador":
            menuPrincipalAdmin()
        case "cliente":
            menuPrincipalCli()
        case "dueño":
            menuPrincipalDue()
    separacion()