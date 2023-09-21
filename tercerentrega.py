import os
import pickle
import os.path
import io

segundoaux = 0

class Usuario():
    def __init__(self):
        self.codigo = 0
        self.usuario = ''
        self.clave = ''
        self.tipo = ''

class Local():
    def __init__(self):
        self.id = 0
        self.codigo = 0
        self.nombre = ''
        self.ubicacion = ''
        self.rubro = ''
        
auf = r"C:\Users\tomas\OneDrive\Desktop\UTN\Algoritmos\proyecto-ayed-2023-git\USUARIOS.dat"
alf = r"C:\Users\tomas\OneDrive\Desktop\UTN\Algoritmos\proyecto-ayed-2023-git\LOCALES.dat"


if not os.path.exists(auf):
    aul = open(auf, 'w+b')
else:
    aul = open(auf, 'r+b')

if not os.path.exists(alf):
    all = open(alf, 'w+b')
else:
    all = open(alf, 'r+b')

def primerMenu():
    print('------------------------------------------------------------------------------')
    global segundoaux
    eleccion = -1
    while eleccion != 3 and segundoaux == 0:
        print('''
        1- Ingresar como usuario registrado.
        2- Registrarse como cliente.
        3- Salir.
            ''')
        eleccion = input("Seleccione una número: ")
        while valEntero(eleccion, 1, 5):
            print("Elección no válida.")
            eleccion = input("Seleccione una opción: ")
        eleccion = int(eleccion)
        match eleccion:
            case 1:
                ingreso()
            case 2:
                registro()
            case 4:
                mostrarLocales()
            case 5:
                mostrarUs()

def mostrarUs():
    print('----------------------------------------------------------------------')
    tamArc = os.path.getsize(auf)
    aul.seek(0)
    while aul.tell() < tamArc:
        reg = pickle.load(aul)
        print(reg.codigo)
        print(reg.usuario)
        print(reg.clave)
        print(reg.tipo)
        print('-------------------------------')
    print('----------------------------------------------------------------------')
       
def mostrarLocales():
    if os.path.getsize(alf) > 0:
        ordenarLocales()
        print('---------------------------------------------------------------------------------------------')
        all.seek(0)
        encabezado = ''
        encabezado += '{:<10}'.format('Id')
        encabezado += '{:<20}'.format('Nombre')
        encabezado += '{:<20}'.format('Ubicación')
        encabezado += '{:<17}'.format('Rubro')
        encabezado += '{:<15}'.format('Código de dueño')
        print(encabezado)
        print('-----------------------------------------------------------------------------------')
        while all.tell() < os.path.getsize(alf):    
            reg = pickle.load(all)
            salida = ''
            salida += '{:<10}'.format(str(reg.id).strip())
            salida += '{:<20}'.format(reg.nombre.strip())
            salida += '{:<20}'.format(reg.ubicacion.strip())
            salida += '{:<17}'.format(reg.rubro.strip())
            salida += '{:<15}'.format(str(reg.codigo).strip())
            print(salida)
            
        print('---------------------------------------------------------------------------------------------')
    else:
        print('---------------------------------------------------------------------')
        print('Todavía no hay locales cargados: ')
        print('----------------------------------------------------------------------')
        
def registro():
    U = Usuario()
    ingresarDatos(U)
    a, b = busqCli(U.usuario, U.clave)
    print(a)
    while a == 'T' or a == 'TT': 
        print('Usuario existente con los datos ingresados, intente de nuevo: ')
        mostrarUs()
        ingresarDatos(U)
        a, b = busqCli(U.usuario, U.clave)
        print(a, b)
    U.codigo = sacarUCod(aul)
    U.tipo = 'Cliente'
    aul.seek(os.path.getsize(auf))
    formateoU(U)
    pickle.dump(U, aul)
    aul.flush()
    os.system("cls")
    # mostrarUs()
  
def ingreso():
    global segundoaux
    
    usuario = input('Ingrese mail de usuario: ')
    while len(usuario) > 100:
        print('Debe de ser un usuario de máximo 100 caracteres. Ingrese de nuevo: ')
        usuario = input('>>  ')
    clave = input('Ingrese clave de usuario: ')
    while len(clave) > 8:
        print('Debe de ser una clave de máximo 8 caracteres. Ingrese de nuevo: ')
        clave = input('>>  ')
    
    usuario = usuario.ljust(100, ' ')
    clave = clave.ljust(8, ' ')

    auxxx = 1
    tipo = 'Nada'
    encontro, tipo = busqCli(usuario, clave)

    while auxxx < 3:
        match encontro:
            case 'T':
                print('Ingreso exitoso.')
                auxxx = 4
            case 'TT': 
                auxxx = auxxx + 1
                clave = input('Clave de usuario incorrecta, intente de nuevo: ')
                while len(clave) > 8:
                    print('Debe de ser una clave de máximo 8 caracteres. Ingrese de nuevo: ')
                    clave = input('>>  ')
            case 'F':
                auxxx = auxxx + 1
                print('Mail y clave de usuario incorrectas: ')
                usuario = input('>>   ')
                while len(usuario) > 100:
                    print('Debe de ser un usuario de máximo 100 caracteres. Ingrese de nuevo: ')
                    usuario = input('>>  ')
                clave = input('>>   ')
                while len(clave) > 8:
                    print('Debe de ser una clave de máximo 8 caracteres. Ingrese de nuevo: ')
                    clave = input('>>  ')    
              
    if auxxx == 4:
        match tipo:
            # case 'Dueno':
            #     menuDue()
            case 'Administrador':
                menuAdmin()
            # case 'Cliente':
            #     menuCli()             
    elif auxxx == 3:
        segundoaux = 1
         
def crearLocal():
    print(os.path.getsize(alf))
    L = Local()
    ingresarDatosLocal(L)
    while busqL(L.nombre): 
        print('Local existente con ese nombre.')
        L.nombre = input('Ingrese nombre de local: ')
        while len(L.nombre) > 50:
            print('Debe de ser un nombre de local de máximo 50 caracteres. Ingrese de nuevo: ')
            L.nombre = input('>>  ')
    L.id = sacarUId(all)
    all.seek(os.path.getsize(alf))
    formateoL(L)
    pickle.dump(L, all)
    all.flush()
    ordenarLocales()
    mostrarLocales()

def sacarCant(fis, log):
    tamArc = os.path.getsize(fis)
    log.seek(0)
    pickle.load(log)
    tamReg = log.tell()
    cantR = tamArc // tamReg
    return tamArc, tamReg, cantR

def sacarUCod(x):
    x.seek(0)
    aux = True
    while True and aux == True:
        try:
            reg = pickle.load(x)
        except EOFError:
            aux = False
    return int(reg.codigo) + 1 

def sacarUId(x):
    x.seek(0)
    aux = True
    if os.path.getsize(alf) > 0:    
        while True and aux == True:
            try:
                reg = pickle.load(x)
            except EOFError:
                aux = False
        return int(reg.id) + 1 
    else: 
        return 1

def ingresarDatos(x):
    x.usuario = input('Ingrese mail de usuario: ')
    while len(x.usuario) > 100:
        print('Debe de ser un usuario de máximo 100 caracteres. Ingrese de nuevo: ')
        x.usuario = input('>>  ')

    x.clave = input('Ingrese clave de usuario: ')
    while len(x.clave) > 8:
        print('Debe de ser una clave de máximo 8 caracteres. Ingrese de nuevo: ')
        x.clave = input('>>  ')
        
    x.usuario = x.usuario.ljust(100, ' ')
    x.clave = x.clave.ljust(8, ' ')
    
def ingresarDatosLocal(x):
    x.nombre = input('Ingrese nombre de local: ').ljust(50, ' ')
    while len(x.nombre) > 50 or busqL(x.nombre):
        if len(x.nombre) > 50:
            print('Debe de ser un nombre de local de máximo 50 caracteres. Ingrese de nuevo: ')
        else:
            print('Nombre de local existente. Ingrese con otro nombre: ')
        x.nombre = input('>>  ').ljust(50, ' ')

    x.ubicacion = input('Ingrese ubicacion de local: ').ljust(50, ' ')
    while len(x.ubicacion) > 50:
        print('Debe de ser una ubicacion de local de máximo 50 caracteres. Ingrese de nuevo: ')
        x.ubicacion = input('>>  ').ljust(50, ' ')
    
    print('''
        a- Indumentaria.
        b- Perfumería.
        c- Gastronomía.
        ''')
    x.rubro = input('Ingrese rubro de local (a/b/c): ').lower()
    while x.rubro != 'a' and x.rubro != 'b' and x.rubro != 'c':
        print('Selección no válida.')
        x.rubro = input("Seleccione a que rubro pertenece el local: ").lower()                  
    match x.rubro:
        case "a":
            x.rubro = "Indumentaria"
        case "b":
            x.rubro = "Perfumería"
        case "c":
            x.rubro = "Gastronomía"
    
    x.codigo = input("Ingrese el código del dueño del local: ")
    while valEntero(x.codigo, 1, 100000) or busqD(x.codigo):
        x.codigo = input("Intente de nuevo: ")
          
    x.codigo = int(x.codigo)            
                
def busqCli(x,y):
    tamArc = os.path.getsize(auf)
    aul.seek(0)
    aux = 'F'
    z = ''
    while aul.tell() < tamArc and aux == 'F':
        reg = pickle.load(aul)
        if reg.usuario == x and reg.clave == y:
            ## agregar redireccion a ingreso
            z = reg.tipo
            aux = 'T'
        elif reg.usuario == x:
            print('Usuario existente con este usuario.')
            aux = 'TT'
    return aux, z

def busqD(x):
    tamArc = os.path.getsize(auf)
    aul.seek(0)
    aux = True
    try: 
        x = int(x)
        while aul.tell() < tamArc and aux == True:
            reg = pickle.load(aul)
            if reg.tipo == 'Dueno'.ljust(13, ' ') and int(reg.codigo) == x:
                aux = False   
    except:
        ...
    return aux

def busqL(x):
    tamArc = os.path.getsize(alf)
    all.seek(0)
    aux = False
    while all.tell() < tamArc and aux == False:
        reg = pickle.load(all)
        if reg.nombre == x:
            aux = True
    return aux

def gestionDeLocales():
        print('''
        Opciones de gestión de locales:
        
            a) Crear locales.
            b) Modificar local.
            c) Eliminar local.
            d) Mapa de locales.
            e) Volver.
        ''')
        eleccion = input("Seleccione una opción: ")
        while eleccion != 'a' and eleccion != 'b' and eleccion != 'c' and eleccion != 'd' and eleccion != 'e':
            print("Elección no válida.")
            print("")
            eleccion = input("Seleccione una opción: ")
        while eleccion != 'e':    
            match eleccion:
                case 'a':
                    x = 'si'
                    while x == 'si':
                        # mostrarLocales()
                        crearLocal()
                        x = input("Si desea seguir cargando locales, escriba 'si': ").lower()
                        while x != 'si' and x != 'no':
                            x = input("Respuesta inválida, intente de nuevo: ").lower()
                            
                    print("Redirigiendo al menu principal de administradores...")
                    
                case 'b':
                    mostrarLocales()

                case 'c': 
                    mostrarLocales()

                case 'd': 
                    ...
                case 'e':
                    print("Volviendo... ")
            if eleccion != 'e':
                print('''
                Opciones de gestión de locales:
        
                a) Crear locales.
                b) Modificar local.
                c) Eliminar local.
                d) Mapa de locales.
                e) Volver.
                ''')
                eleccion = input("Seleccione una número: ")
                while eleccion != 'a' and eleccion != 'b' and eleccion != 'c' and eleccion != 'd' and eleccion != 'e':
                    print("Elección no válida.")
                    eleccion = input("Seleccione una opción: ")

def menuAdmin():
        print('''Opciones de Menú principal de Administradores:

            1- Gestión de locales.
            2- Crear cuenta de dueños de locales.
            3- Aprobar/Denegar solicitudes de descuentos.
            4- Gestión de novedades.
            5- Reporte de utilización de descuentos.
            0- Salir.
        ''')
        eleccion = input("Seleccione una número: ")
        while valEntero(eleccion, 0, 5):
            print("Elección no válida.")
            eleccion = input("Seleccione una opción: ")
        eleccion = int(eleccion)
        while eleccion != 0:
            match eleccion:
                case 0:
                    print("Saliendo.")
                case 1:
                    print("Gestión de locales: ")
                    gestionDeLocales()
                # case '2':
                #     crearCuentasDueno()
                # case '3':
                #     solDesc()
                # case '4':
                #     gestionDeNovedades()
                # case '5':
                #     reporteDesc()


    #hacer hasta elec = 0

def formateoU(x):
    x.usuario = x.usuario.ljust(100, ' ')
    x.clave = x.clave.ljust(8, ' ')
    x.tipo = x.tipo.ljust(13, ' ')
    
def formateoL(x):
    x.nombre = x.nombre.ljust(50, ' ')
    x.ubicacion = x.ubicacion.ljust(50, ' ')
    x.rubro = x.rubro.ljust(12, ' ')
    
def valEntero(opc, desde, hasta): 
    try:
        int(opc)
        if int(opc) >= desde and int(opc) <= hasta:
            return False
        else:
            return True
    except:
        return True

def ordenarLocales():
    tamArc, tamReg, cantRegs = sacarCant(alf, all)
    for i in range(0, cantRegs-1):
        for j in range(i+1, cantRegs):
            all.seek(i*tamReg, 0)
            auxi = pickle.load(all)
            all.seek(j*tamReg, 0)
            auxj = pickle.load(all)
            if (auxi.nombre > auxj.nombre):
                all.seek(i*tamReg, 0)
                pickle.dump(auxj, all)
                all.seek(j*tamReg, 0)
                pickle.dump(auxi, all)
    # all.flush()

if os.path.getsize(auf) == 0:
    U = Usuario()
    U.codigo = 1
    U.usuario = '1'.ljust(100, ' ')
    U.clave = '1'.ljust(8, ' ')
    U.tipo = 'Administrador'
    aul.seek(0)
    pickle.dump(U, aul)
    print('--------------------------')
    aul.flush()
    
    U = Usuario()
    U.codigo = 2
    U.usuario = '2'.ljust(100, ' ')
    U.clave = '2'.ljust(8, ' ')
    U.tipo = 'Dueno'.ljust(13, ' ')
    pickle.dump(U, aul)
    print('--------------------------')
    aul.flush()

    # mostrarUs()

primerMenu()

print("Saliendo.........")
all.close()
aul.close()