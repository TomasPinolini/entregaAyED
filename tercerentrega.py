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
        self.estado = ''
        
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
    eleccionpm = -1
    while eleccionpm != 3 and segundoaux == 0:
        print('''
        1- Ingresar como usuario registrado.
        2- Registrarse como cliente.
        3- Salir.
            ''')
        eleccionpm = input("Seleccione una número: ")
        while valEntero(eleccionpm, 1, 6):
            print("Elección no válida.")
            eleccionpm = input("Seleccione una opción: ")
        eleccionpm = int(eleccionpm)
        match eleccionpm:
            case 1:
                ingreso()
            case 2:
                registro()
            case 4:
                mostrarLocales()
            case 5:
                mostrarUs()
            case 6:
                mapeoLocales()
                
def menuAdmin():
        eleccionma = eleccionMA()
        while eleccionma != 0:
            match eleccionma:
                case 0:
                    print("Saliendo.")
                    eleccionma = 0
                case 1:
                    print("Gestión de locales: ")
                    gestionDeLocales()                    
                case 2:
                    crearCuentaD()
                # case '3':
                #     solDesc()
                # case '4':
                #     gestionDeNovedades()
                # case '5':
                #     reporteDesc()
            
            if eleccionma != 0:
                eleccionma = eleccionMA()
 
def menuDue():
    eleccionD = eleccionDue()
    while eleccionD != 0:
        match eleccionD:
            case 0:
                 print('Saliendo...')
                 eleccionD = 0
            case 1:
                # crearDescuento()
            # case 2:
            #     reporteUsoDesc()    
            # case 3:
                #verNovedades()
        if eleccionD != 0:
            eleccionD = eleccionDue()
            
def menuC():
    eleccionC = eleccionCl()
    while eleccionC != 0:
        match eleccionC:
            case 0:
                 print('Saliendo...')
                 eleccionC = 0
            # case 1:
                # buscarDesc()
            # case 2:
            #     solicitarDesc()    
            # case 3:
                #verNovedades()
        if eleccionC != 0:
            eleccionC = eleccionCl()
    
      
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
  
def crearCuentaD():
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
    U.tipo = 'Dueno'
    aul.seek(os.path.getsize(auf))
    formateoU(U)
    pickle.dump(U, aul)
    aul.flush()
    os.system("cls")

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

    auxxx = 0
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
                    clave = input('>>  ').ljust(8, ' ')
                encontro, tipo = busqCli(usuario, clave)
            case 'F':
                auxxx = auxxx + 1
                print('Mail y clave de usuario incorrectas: ')
                usuario = input('>>   ').ljust(100, ' ')
                while len(usuario) > 100:
                    print('Debe de ser un usuario de máximo 100 caracteres. Ingrese de nuevo: ')
                    usuario = input('>>  ').ljust(100, ' ')
                clave = input('>>   ').ljust(8, ' ')
                while len(clave) > 8:
                    print('Debe de ser una clave de máximo 8 caracteres. Ingrese de nuevo: ')
                    clave = input('>>  ').ljust(8, ' ')    
                encontro, tipo = busqCli(usuario, clave)
        
    if auxxx == 4:
        match tipo:
            # case 'Dueno':
                # menuDue()
            case 'Administrador':
                menuAdmin()
            # case 'Cliente':
            #     menuCli()    
        
def mapeoLocales():
    tamArc, tamReg, cantR = sacarCant(alf, all)
    locales = [0]*50
    for i in range(50):
        all.seek(0)
        for i in range(cantR):
            reg = pickle.load(all)
            locales[i] = reg.id
    a = 0
    for i in range(10):
        print("+-+-+-+-+-+")
        print("|"+str(locales[a])+"|"+str(locales[a+1])+"|"+str(locales[a+2])+"|"+str(locales[a+3])+"|"+str(locales[a+4])+"|")
        a = a + 5     
    print("+-+-+-+-+-+")
            
def gestionDeLocales(): 
    elecciongdl = eleccionGDL() 
    while elecciongdl != 'e':  
        match elecciongdl:
            case 'a':
                x = 'si'
                while x == 'si':
                    crearLocal()
                    x = input("Si desea seguir cargando locales, escriba 'si': ").lower()
                    while x != 'si' and x != 'no':
                        x = input("Respuesta inválida, intente de nuevo: ").lower()
                print("Redirigiendo al menu principal de administradores...")
                elecciongdl = 'e'
            case 'b':
                modificarLocal()
                mostrarLocales()
            case 'c': 
                eliminarLocal()
                mostrarLocales()
            case 'd': 
                mapeoLocales()
            case 'e':
                print('Volviendo al menu principal de administradores...')
                elecciongdl = 'e'
        if elecciongdl != 'e':
            elecciongdl = eleccionGDL() 
                
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
        print('---------------------------------------------------------------------------------------------')
        all.seek(0)
        encabezado = ''
        encabezado += '{:<10}'.format('Id')
        encabezado += '{:<20}'.format('Nombre')
        encabezado += '{:<20}'.format('Ubicación')
        encabezado += '{:<17}'.format('Rubro')
        encabezado += '{:<10}'.format('Estado')
        encabezado += '{:<15}'.format('Código de dueño')
        print(encabezado)
        print('---------------------------------------------------------------------------------------------')
        while all.tell() < os.path.getsize(alf):    
            reg = pickle.load(all)
            print(all.tell())
            salida = ''
            salida += '{:<10}'.format(str(reg.id).strip())
            salida += '{:<20}'.format(reg.nombre.strip())
            salida += '{:<20}'.format(reg.ubicacion.strip())
            salida += '{:<17}'.format(reg.rubro.strip())
            salida += '{:<10}'.format(reg.estado.strip())
            salida += '{:<15}'.format(str(reg.codigo).strip())
            print(salida)
            
        print('---------------------------------------------------------------------------------------------')
    else:
        print('---------------------------------------------------------------------')
        print('Todavía no hay locales cargados: ')
        print('----------------------------------------------------------------------')
             
def crearLocal():
    L = Local()
    ingresarDatosLocal(L)
    L.id = sacarUId(all)
    L.estado = 'A'
    all.seek(os.path.getsize(alf))
    formateoL(L)
    pickle.dump(L, all)
    all.flush()
    ordenarLocales()
    mostrarLocales()

def modificarLocal():
    cod = input('Código del local a modificar: ')
    while busqLC(cod) == -1:
        cod = input('Intente de nuevo: ')
    tamArc, tamReg, cantR = sacarCant(alf, all)
    all.seek(busqLC(cod)-tamReg)
    reg = pickle.load(all)
    print('---------------------------------------------------------------------------------------------')
    all.seek(0)
    encabezado = ''
    encabezado += '{:<20}'.format('1- Nombre')
    encabezado += '{:<20}'.format('2- Ubicación')
    encabezado += '{:<17}'.format('3- Rubro')
    encabezado += '{:<15}'.format('4- Código de dueño')
    print(encabezado)
    print('-----------------------------------------------------------------------------------')
    salida = ''
    salida += '{:<20}'.format(reg.nombre.strip())
    salida += '{:<20}'.format(reg.ubicacion.strip())
    salida += '{:<17}'.format(reg.rubro.strip())
    salida += '{:<15}'.format(str(reg.codigo).strip())
    print(salida)
    print('-----------------------------------------------------------------------------------')
    campo = input('Seleccione campo a modificar: ')
    while valEntero(campo, 1, 5):
        campo = input('Campo inválido, intente de nuevo: ')
    campo = int(campo)
    match campo:
        case 1:
            print('Previo campo: '+reg.nombre)
            reg.nombre = input('>> ')
            
        case 2:
            print('Previo campo: '+reg.ubicacion)
            reg.ubicacion = input('>> ')         
        case 3:
            print('Previo campo: '+reg.rubro)
                
            print('''
            a- Indumentaria.
            b- Perfumería.
            c- Gastronomía.
            ''')
            rubro = input('Ingrese rubro de local (a/b/c): ').lower()
            while rubro != 'a' and rubro != 'b' and rubro != 'c':
                rubro = input('Selección no válida, intente de nuevo: ').lower()                  
            match rubro:
                case "a":
                    reg.rubro = "Indumentaria"
                case "b":
                    reg.rubro = "Perfumeria"
                case "c":
                    reg.rubro = "Gastronomia"
        case 4:
            print('Previo campo: '+reg.codigo)
            codigo = input('>> ')
            while valEntero(codigo, 1, 100000) or busqD(codigo):
                codigo = input("Intente de nuevo: ")
            reg.codigo = int(codigo)            

    all.seek(busqLC(cod)-tamReg)
    formateoL(reg)
    pickle.dump(reg, all)
    all.flush()
    ordenarLocales()
    mostrarLocales()
       
def eliminarLocal():
    cod = input('Código del local a eliminar: ')
    while busqLC(cod) == -1:
        cod = input('Intente de nuevo: ')
    tamArc, tamReg, cantR = sacarCant(alf, all)
    all.seek(busqLC(cod)-tamReg)
    reg = pickle.load(all)
    if reg.estado == 'B':
        print(reg.nombre.strip(), 'ya está dado de baja.')
    else:
        print('Desea confirmar la baja del local? ')
        print('---------------------------------------------------------------------------------------------')
        encabezado = ''
        encabezado += '{:<20}'.format('1- Nombre')
        encabezado += '{:<20}'.format('2- Ubicación')
        encabezado += '{:<17}'.format('3- Rubro')
        encabezado += '{:<15}'.format('4- Código de dueño')
        print(encabezado)
        print('-----------------------------------------------------------------------------------')
        salida = ''
        salida += '{:<20}'.format(reg.nombre.strip())
        salida += '{:<20}'.format(reg.ubicacion.strip())
        salida += '{:<17}'.format(reg.rubro.strip())
        salida += '{:<15}'.format(str(reg.codigo).strip())
        print(salida)
        conf = input('[S/N]? ').lower()
        while conf not in ['s', 'n']:
            conf = input('Respuesta inválida, intente de nuevo: ').lower()
        if conf == 's':
            reg.estado = 'B'       
        all.seek(busqLC(cod)-tamReg)
        formateoL(reg)
        pickle.dump(reg, all)
        all.flush()

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
    while len(x.nombre) > 50 or busqLN(x.nombre) != -1:
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
            x.rubro = "Perfumeria"
        case "c":
            x.rubro = "Gastronomia"
    
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

def busqLN(x):
    if os.path.getsize(alf) > 0:
        tamArc, tamReg, cantR = sacarCant(alf, all)
        all.seek(0)
        desde = 0
        hasta = cantR-1
        medio = (desde + hasta) // 2
        all.seek(medio*tamReg, 0)
        reg = pickle.load(all)
        while reg.nombre != x and desde < hasta:
            if x < reg.nombre:
                hasta = medio - 1
            else:
                desde = hasta + 1
            medio = (desde + hasta) // 2
            all.seek(medio*tamReg, 0)
            reg = pickle.load(all)
        if reg.nombre == x:
            return medio*tamReg
        else: return -1
    else: return -1   

def busqLC(x):
    try:
        aux = -1
        x = int(x)
        tamArc = os.path.getsize(alf)
        all.seek(0)
        while all.tell() < tamArc:
            reg = pickle.load(all)
            if reg.id == x:
                aux = all.tell() 
        return aux   
    except: 
       return aux

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
    if cantRegs > 1:
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
    all.flush()

def eleccionMA():
    print('''Opciones de Menú principal de Administradores:

        1- Gestión de locales.
        2- Crear cuenta de dueños de locales.
        3- Aprobar/Denegar solicitudes de descuentos.
        4- Gestión de novedades.
        5- Reporte de utilización de descuentos.
        0- Salir.
    ''')
    eleccionma = input("Seleccione una número: ")
    while valEntero(eleccionma, 0, 5):
        print("Elección no válida.")
        eleccionma = input("Seleccione una opción: ")
    return int(eleccionma)

def eleccionGDL():
    print('''
            Opciones de gestión de locales:
            
                a) Crear locales.
                b) Modificar local.
                c) Eliminar local.
                d) Mapa de locales.
                e) Volver.
            ''')
    elecciongdl = input('Seleccione una opción: ').strip()
    while elecciongdl not in ['a', 'b', 'c', 'd', 'e']:
        print("Elección no válida.")
        elecciongdl = input('Elección no válida, intente de nuevo: ').strip() 
    return elecciongdl

def eleccionDue():
    print('''
          1. Crear descuento.
          2. Reporte de uso de descuentos.
          3. Ver novedades.
          0. Salir
          ''')
    elecciond = input("Seleccione una número: ")
    while valEntero(elecciond, 0, 3):
        print("Elección no válida.")
        elecciond = input("Seleccione una opción: ")
    return int(elecciond)

def eleccionCl():
    print('''
          1. Buscar descuentos en local.
          2. Solicitar descuento.
          3. Ver novedades.
          0. Salir
          ''')
    eleccionC = input("Seleccione una número: ")
    while valEntero(eleccionC, 0, 3):
        print("Elección no válida.")
        eleccionC = input("Seleccione una opción: ")
    return int(eleccionC)

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


primerMenu()

print("Saliendo.........")
all.close()
aul.close()