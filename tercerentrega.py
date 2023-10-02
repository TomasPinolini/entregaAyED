import os
import pickle
import os.path
import io
import datetime

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
        
class Promocion():
    def __init__(self):
        self.id = 0
        self.desc = ''
        self.desde = ''
        self.hasta = ''
        self.diadesemana = ''
        self.estado = ''
        self.codD = 0
        self.codLocal = 0

class UsoPromo():
    def __init__(self):
        self.codCli = 0
        self.codPromo = 0
        self.hoy = ''

class reporteUso():
    def __init__(self):
        self.id = 0
        self.desc = ''
        self.desde = ''
        self.hasta = ''
        self.diadesemana =''
        self.estado = ''
        self.cantUsos = 0

auf = r"C:\Users\tomas\OneDrive\Desktop\UTN\Algoritmos\proyecto-ayed-2023-git\USUARIOS.dat"
alf = r"C:\Users\tomas\OneDrive\Desktop\UTN\Algoritmos\proyecto-ayed-2023-git\LOCALES.dat"
apf = r"C:\Users\tomas\OneDrive\Desktop\UTN\Algoritmos\proyecto-ayed-2023-git\PROMOCIONES.dat"
aupf = r"C:\Users\tomas\OneDrive\Desktop\UTN\Algoritmos\proyecto-ayed-2023-git\USO.dat"
aruf = r"C:\Users\tomas\OneDrive\Desktop\UTN\Algoritmos\proyecto-ayed-2023-git\REPORTEUSO.dat"


if not os.path.exists(aupf):
    aupl = open(aupf, 'w+b')
else:
    aupl = open(aupf, 'r+b')

if not os.path.exists(alf):
    all = open(alf, 'w+b')
else:
    all = open(alf, 'r+b')

if not os.path.exists(apf):
    apl = open(apf, 'w+b')
else:
    apl = open(apf, 'r+b')

if not os.path.exists(auf):
    aul = open(auf, 'w+b')
else:
    aul = open(auf, 'r+b')

if not os.path.exists(aruf):
    arul = open(aruf, 'w+b')
else:
    arul = open(aruf, 'r+b')

def primerMenu():
    print('------------------------------------------------------------------------------')
    eleccionpm = -1
    while eleccionpm != 3:
        print('''
        1- Ingresar como usuario registrado.
        2- Registrarse como cliente.
        3- Salir.
            ''')
        eleccionpm = input("Seleccione una número: ")
        while valEntero(eleccionpm, 1, 14):
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
                mostrarPromos()
            case 7: 
                mostrarUsos()
                
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
            case 3:
                aprobarDenegarD()
            case 4:
                print('Chapin!')
                # gestionDeNovedades()
            case 5:
                x = reporteDesc()
        
        if eleccionma != 0:
            eleccionma = eleccionMA()
 
def menuDue(idd):
    eleccionD = eleccionDue()
    while eleccionD != 0:
        match eleccionD:
            case 0:
                 print('Saliendo...')
                 eleccionD = 0
            case 1:
                x = 'S'
                while x == 'S':
                    crearPromocion(idd)
                    mostrarPromos()
                    x = input('Desea añadir otra promoción al listado? [S/N] >> ').upper()
                    while x not in ['S', 'N']:
                        x = input('Respuesta inválida, [S/N] >>').upper()
                print("Redirigiendo al menu principal de dueños...")
                eleccionD = 0
            case 2:
                reporteUsoDesc(idd)    
            case 3:
                print('Chapin!')
                #verNovedades()
        if eleccionD != 0:
            eleccionD = eleccionDue()
            
def menuC(x):
    eleccionC = eleccionCl()
    while eleccionC != 0:
        match eleccionC:
            case 0:
                 print('Saliendo...')
                 eleccionC = 0
            case 1:
                buscarDesc()
            case 2:
                solicitarDesc(x)    
            case 3:
                print("Chapín!")
                #verNovedades()
        if eleccionC != 0:
            eleccionC = eleccionCl()
    
def registro():
    U = Usuario()
    ingresarDatos(U)
    a, b, cod = busqCli(U.usuario, U.clave, auf, aul)
    print(a)
    while a == 'T' or a == 'TT': 
        print('Usuario existente con los datos ingresados, intente de nuevo: ')
        mostrarUs()
        ingresarDatos(U)
        a, b, c = busqCli(U.usuario, U.clave, auf, aul)
        print(a, b)
    U.codigo = sacarUCod(aul)
    U.tipo = 'Cliente'
    aul.seek(os.path.getsize(auf))
    formateoU(U)
    pickle.dump(U, aul)
    aul.flush()
    os.system("cls")
  
def crearCuentaD():
    U = Usuario()
    ingresarDatos(U)
    a, b, c = busqCli(U.usuario, U.clave, auf, aul)
    print(a)
    while a == 'T' or a == 'TT': 
        print('Usuario existente con los datos ingresados, intente de nuevo: ')
        mostrarUs()
        ingresarDatos(U)
        a, b, c = busqCli(U.usuario, U.clave, aul, auf)
        print(a, b)
    U.codigo = sacarUCod(aul)
    U.tipo = 'Dueno'
    aul.seek(os.path.getsize(auf))
    formateoU(U)
    pickle.dump(U, aul)
    aul.flush()
    os.system("cls")

def aprobarDenegarD():
    mostrarPromosPend()
    tamArc, tamReg, cantR = sacarCant(apf, apl)
    cod = input('Código de promoción >> ')
    while valEntero(cod, 0, 100000):
        cod = input('Código inválida, intente de nuevo: ')
    cod = int(cod)
    if busqIDP(cod) != -1:
        apl.seek(busqIDP(cod))
        reg = pickle.load(apl)
        if reg.estado.strip() == 'Pendiente':
            estado = input('Aprobado/Rechazado? (1/2) >> ')
            while valEntero(estado, 1, 2):
                estado = input('Respuesta inválida, intente de nuevo: ')
            estado = int(estado)
            match estado:
                case 1:
                    estado = 'Aprobada'
                case 2: 
                    estado = 'Rechazada'
            reg.estado = estado.ljust(9, ' ')
            apl.seek(-tamReg, 1)
            pickle.dump(reg, apl)
            apl.flush()
        else: print('Promoción ya evaluada: '+reg.estado.strip())
    else:
        print('No existe promoción con el código emitido.')
    
def reporteDesc():
    print('Desde: ')
    desde = validarFecha()
    print('Hasta: ')
    hasta = validarFecha()   
    while desde > hasta:
        print('Fechas inválidas:')
        print('Desde: ')
        desde = validarFecha()
        print('Hasta: ')
        hasta = validarFecha()  
    
    if os.path.getsize(apf) > 0:
        print('------------------------------------------------------------------------------------------------')
        apl.seek(0)
        encabezado = ''
        encabezado += '{:<7}'.format('Id')
        encabezado += '{:<35}'.format('Descripción')
        encabezado += '{:<15}'.format('Desde')
        encabezado += '{:<15}'.format('Hasta')
        encabezado += '{:<12}'.format('Estado')
        print(encabezado)
        print('-----------------------------------------------------------------------------------------------')
        while apl.tell() < os.path.getsize(apf):    
            reg = pickle.load(apl)
            anodesde, mesdesde, diadesde = reg.desde.split('-')
            anohasta, meshasta, diahasta = reg.hasta.split('-')
            anodesde, mesdesde, diadesde, anohasta, meshasta, diahasta = int(anodesde), int(mesdesde), int(diadesde), int(anohasta), int(meshasta), int(diahasta)
            regdesde = datetime.date(anodesde, mesdesde, diadesde)
            reghasta = datetime.date(anohasta, meshasta, diahasta)
            if reg.estado.strip() == 'Aprobada' and desde >= regdesde and hasta <= reghasta:
                salida = ''
                salida += '{:<7}'.format(str(reg.id).strip())
                salida += '{:<35}'.format(reg.desc.strip())
                salida += '{:<15}'.format(reg.desde.strip())
                salida += '{:<15}'.format(reg.hasta.strip())
                salida += '{:<12}'.format(reg.estado.strip())
                print(salida)
                print('-----------------------------------------------------------------------------------------------')
    else:
        print('---------------------------------------------------------------------')
        print('No hay promociones aprobadas ')
        print('----------------------------------------------------------------------') 

def ingreso():  
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
    encontro, tipo, id = busqCli(usuario, clave, auf, aul)

    while auxxx < 3 and not encontro:
        auxxx += 1
        print('Datos no compatible: ')
        usuario = input('>>   ').ljust(100, ' ')
        clave = input('>>   ').ljust(8, ' ')
        while len(usuario) > 100:
            print('Debe de ser un usuario de máximo 100 caracteres. Ingrese de nuevo: ')
            usuario = input('>>  ').ljust(100, ' ')
        while len(clave) > 8:
            print('Debe de ser una clave de máximo 8 caracteres. Ingrese de nuevo: ')
            clave = input('>>  ').ljust(8, ' ')    
        encontro, tipo, id = busqCli(usuario, clave, auf, aul)
                  
    if encontro:
        match tipo.strip():
            case 'Dueno':
                menuDue(id)
            case 'Administrador':
                menuAdmin()
            case 'Cliente':
                menuC(id)    
        
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
                x = 'S'
                while x == 'S':
                    crearLocal()
                    x = input("Si desea seguir cargando locales? [S/N] >> ").upper()
                    while x not in ['S', 'N']:
                        x = input("Respuesta inválida [S/N] ").upper()
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
        print('Todavía no hay locales cargados ')
        print('----------------------------------------------------------------------')
            
def mostrarPromos():
    if os.path.getsize(apf) > 0:
        print('-------------------------------------------------------------------------------------------------------------------------')
        apl.seek(0)
        encabezado = ''
        encabezado += '{:<7}'.format('Id')
        encabezado += '{:<35}'.format('Descripción')
        encabezado += '{:<15}'.format('Desde')
        encabezado += '{:<15}'.format('Hasta')
        encabezado += '{:<12}'.format('Estado')
        encabezado += '{:<18}'.format('Código de dueño')
        encabezado += '{:<15}'.format('Código de local')
        print(encabezado)
        print('------------------------------------------------------------------------------------------------------------------------')
        while apl.tell() < os.path.getsize(apf):    
            reg = pickle.load(apl)
            salida = ''
            salida += '{:<7}'.format(str(reg.id).strip())
            salida += '{:<35}'.format(reg.desc.strip())
            salida += '{:<15}'.format(reg.desde.strip())
            salida += '{:<15}'.format(reg.hasta.strip())
            salida += '{:<12}'.format(reg.estado.strip())
            salida += '{:<18}'.format(str(reg.codD))
            salida += '{:<15}'.format(str(reg.codLocal))
            print(salida)
            
        print('------------------------------------------------------------------------------------------------------------------------')
    else:
        print('-------------------------------------------------')
        print('Todavía no hay promociones cargadas ')
        print('-------------------------------------------------')
 
def mostrarPromosPend():
    if os.path.getsize(apf) > 0:
        print('------------------------------------------------------------------------------------------------')
        apl.seek(0)
        encabezado = ''
        encabezado += '{:<10}'.format('Id')
        encabezado += '{:<35}'.format('Descripción')
        encabezado += '{:<20}'.format('Desde')
        encabezado += '{:<20}'.format('Hasta')
        print(encabezado)
        print('-----------------------------------------------------------------------------------------------')
        while apl.tell() < os.path.getsize(apf):    
            reg = pickle.load(apl)
            if reg.estado == 'Pendiente'.strip():
                salida = ''
                salida += '{:<10}'.format(str(reg.id).strip())
                salida += '{:<35}'.format(reg.desc.strip())
                salida += '{:<20}'.format(reg.desde.strip())
                salida += '{:<20}'.format(reg.hasta.strip())
                print(salida)
                print('-----------------------------------------------------------------------------------------------')
    else:
        print('---------------------------------------------------------------------')
        print('No hay promociones pendietes ')
        print('----------------------------------------------------------------------') 

def mostrarUsos():
    if os.path.getsize(aupf) > 0:
        print('--------------------------------------------------------')
        aupl.seek(0)
        encabezado = ''
        encabezado += '{:<20}'.format('Código Cliente')
        encabezado += '{:<20}'.format('Codigo Promoción')
        encabezado += '{:<25}'.format('Día')
        print(encabezado)
        print('--------------------------------------------------------')
        while aupl.tell() < os.path.getsize(aupf):    
            reg = pickle.load(aupl)
            salida = ''
            salida += '{:<20}'.format(reg.codCli)
            salida += '{:<20}'.format(reg.codPromo)
            salida += '{:<25}'.format(reg.hoy.strip())
            print(salida)
            
        print('--------------------------------------------------------')
    else:
        print('---------------------------------------------------------------------')
        print('Todavía no hay promociones utilizadas ')
        print('----------------------------------------------------------------------')    

def crearLocal():
    L = Local()
    ingresarDatosLocal(L)
    L.id = sacarUIdL()
    L.estado = 'A'
    all.seek(os.path.getsize(alf))
    formateoL(L)
    pickle.dump(L, all)
    all.flush()
    ordenarLocales()
    mostrarLocales()

def crearPromocion(idd):
    P = Promocion()
    ingresarDatosPromo(P,idd)
    P.id = sacarUIdP()
    P.estado = 'Pendiente'
    P.codD = idd
    apl.seek(os.path.getsize(apf))
    formateoP(P)
    print(P.codLocal)
    pickle.dump(P, apl)
    apl.flush()

def reporteUsoDesc(idd):
    aupl.seek(0)
    print('Desde: ')
    desde = validarFecha()
    print('Hasta: ')
    hasta = validarFecha()   
    while desde > hasta:
        print('Fechas inválidas:')
        print('Desde: ')
        desde = validarFecha()
        print('Hasta: ')
        hasta = validarFecha()
        
    if os.path.getsize(apf) > 0:
        all.seek(0)
        while all.tell() < os.path.getsize(alf):
            local = pickle.load(all)
            if local.codigo == idd:
                print()
                print(local.nombre.capitalize().strip()+':') 
                print('------------------------------------------------------------------')
                encabezado = ''
                encabezado += '{:<7}'.format('Id')
                encabezado += '{:<35}'.format('Descripción')
                encabezado += '{:<7}'.format('Cantidad Uso')
                print(encabezado)
                print('-----------------------------------------------------------------')  
                apl.seek(0)         
                while apl.tell() < os.path.getsize(apf):    
                    promo = pickle.load(apl)
                    anodesde, mesdesde, diadesde = promo.desde.split('-')
                    anohasta, meshasta, diahasta = promo.hasta.split('-')
                    anodesde, mesdesde, diadesde, anohasta, meshasta, diahasta = int(anodesde), int(mesdesde), int(diadesde), int(anohasta), int(meshasta), int(diahasta)
                    promodesde = datetime.date(anodesde, mesdesde, diadesde)
                    promohasta = datetime.date(anohasta, meshasta, diahasta)
                    codigoL = int(promo.codLocal)
                    if promo.estado.strip() == 'Aprobada' and desde >= promodesde and hasta <= promohasta and local.id == codigoL:
                        cantUsos = 0
                        aupl.seek(0)
                        salida = ''
                        salida += '{:<7}'.format(str(promo.id).strip())
                        salida += '{:<35}'.format(promo.desc.strip())
                        while aupl.tell() < os.path.getsize(aupf): 
                            uso = pickle.load(aupl)
                            if uso.codPromo == promo.id:
                                cantUsos += 1
                        salida += '{:<7}'.format(cantUsos)
                        print(salida)
                        print('-----------------------------------------------------------------')
    else:
        print('---------------------------------------------------------------------')
        print('No hay promociones aprobadas ')
        print('---------------------------------------------------------------------')   
               
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
    if os.path.getsize(fis) > 0:
        tamArc = os.path.getsize(fis)
        log.seek(0)
        pickle.load(log)
        tamReg = log.tell()
        cantR = tamArc // tamReg
        return tamArc, tamReg, cantR
    return 0,0,0

def sacarUCod(x):
    x.seek(0)
    aux = True
    while True and aux == True:
        try:
            reg = pickle.load(x)
        except EOFError:
            aux = False
    return int(reg.codigo) + 1 

def sacarUIdL():
    if os.path.getsize(alf)>0:
        all.seek(0)
        comp = 0
        tArc = os.path.getsize(alf)
        while all.tell() < tArc:
            reg = pickle.load(all)
            if reg.id > comp:
                comp = reg.id
        return comp + 1
    else:
        return 1

def sacarUIdP():
    if os.path.getsize(apf)>0:
        apl.seek(0)
        comp = 0
        tArc = os.path.getsize(apf)
        while apl.tell() < tArc:
            reg = pickle.load(apl)
            if reg.id > comp:
                comp = reg.id
        return comp + 1
    else:
        return 1

def sacarLocales(idd):
    tamArc, tamReg, cantR = sacarCant(alf, all)
    all.seek(0)
    r = ''
    while all.tell() < tamArc:
        local = pickle.load(all)
        if local.codigo == idd:
            if len(r) > 0:
                r = r + ',' + str(local.id)
            else: r = str(local.id)
    return r

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
       
def ingresarDatosPromo(x, y):
    x.desc = input('Ingrese la descripción de la promoción a agregar: ')
    print('Desde: ')
    desde = validarFecha()
    print('Hasta: ')
    hasta = validarFecha()   
    while desde > hasta or desde < datetime.date.today():
        print('Fechas inválidas:')
        print('Desde: ')
        desde = validarFecha()
        print('Hasta: ')
        hasta = validarFecha()    
    x.desde = str(desde)
    x.hasta = str(hasta)
    
    dias = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    for i in dias:
        msj = str(i)+ '? 0: No, 1: Si >> '
        conf = input(str(msj))
        while valEntero(conf, 0, 1):
            msjj = 'Respeusta inválida, '+msj
            conf = input(msjj)
        conf = int(conf)
        x.diadesemana += str(conf)
    
    x.codLocal = input('Código del local al que será aplicada la promoción: ')
    while valLC(x.codLocal, y) == -1:
        x.codLocal = input('Código del local inexistente, intente de nuevo: ')
    
def busqCli(x,y, fis, log):
    tamArc = os.path.getsize(fis)
    log.seek(0)
    aux = False
    z = ''
    cod = 0
    while log.tell() < tamArc and aux == False:
        reg = pickle.load(log)
        if reg.usuario == x and reg.clave == y:
            z = reg.tipo
            aux = True
            cod = reg.codigo
        elif reg.usuario == x:
            print('Usuario existente con este usuario.')
    return aux, z, cod

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
                desde = medio + 1
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

def valLC(cod, idd):
    try:
        aux = -1
        idd = int(idd)
        cod = int(cod)
        tamArc = os.path.getsize(alf)
        all.seek(0)
        while all.tell() < tamArc:
            local = pickle.load(all)
            if local.codigo == idd and cod == local.id:
                aux = cod
        return aux   
    except: 
       return aux

def busqPC(x):
    try:
        aux = -1
        x = int(x)
        tamArc = os.path.getsize(apf)
        apl.seek(0)
        while apl.tell() < tamArc:
            reg = pickle.load(apl)
            if reg.id == x:
                aux = apl.tell() 
        return aux   
    except: 
       return aux

def busqIDP(x):
    try:
        aux = -1
        tamArc, tamReg, cantR = sacarCant(apf, apl)
        apl.seek(0)
        while apl.tell() < tamArc:
            reg = pickle.load(apl)
            if reg.id == x:
                aux = apl.tell() - tamReg
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
    
def formateoP(x):
    x.desc = x.desc.ljust(50, ' ')
    x.desde = x.desde.ljust(10, ' ')
    x.hasta = x.hasta.ljust(10, ' ')
    x.diadesemana = x.diadesemana.ljust(7, ' ')
    x.estado = x.estado.ljust(9, ' ')
           
def valEntero(opc, desde, hasta): 
    try:
        int(opc)
        if int(opc) >= desde and int(opc) <= hasta:
            return False
        else:
            return True
    except:
        return True

def validarFecha():
    ano = input('Año: ')
    while valEntero(ano, 0, 2100):
        ano = input('Inválido, intente de nuevo: ')
    ano = int(ano)
    mes = input('Mes: ')
    while valEntero(mes, 1, 12):
        mes = input('Inválido, intente de nuevo: ')
    mes = int(mes)
    dia = input('Día: ')
    while valEntero(dia, 1, 31):
        dia = input('Inválido, intente de nuevo: ')
    dia = int(dia)
    
    return datetime.date(ano, mes, dia)

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

def buscarDesc():
    mostrarLocales()
    cod = input('Código del local donde se usó la promoción: ')
    while busqLC(cod) == -1 and valEntero(cod, 0, 1000):
        cod = input('Promoción con tal código inexistente, intente de nuevo: ')
    cod = int(cod)
    fecha = validarFecha()
    while fecha < datetime.date.today():
        print('Debe ser la fecha de hoy o posterior.')
        fecha = validarFecha()
    wd = fecha.weekday()
    tamArc, tamReg, cantR = sacarCant(apf, apl)
    tamArcL, tamRegL, cantRL = sacarCant(alf, all)
    all.seek(cod*tamRegL-tamRegL)
    local = pickle.load(all)
    duenoLocal = local.codigo
    apl.seek(0)
    encabezado = ''
    encabezado += '{:<10}'.format('Id')
    encabezado += '{:<35}'.format('Descripción')
    encabezado += '{:<20}'.format('Desde')
    encabezado += '{:<20}'.format('Hasta')
    print(encabezado)
    print('-----------------------------------------------------------------------------------------------')
    while apl.tell() < tamArc:
        promo = pickle.load(apl)
        if promo.diadesemana[wd] == '1' and promo.estado.strip() == 'Aprobada' and promo.codD == duenoLocal:
            salida = ''
            salida += '{:<10}'.format(str(promo.id).strip())
            salida += '{:<35}'.format(promo.desc.strip())
            salida += '{:<20}'.format(promo.desde.strip())
            salida += '{:<20}'.format(promo.hasta.strip())
            print(salida)
    
def solicitarDesc(p):
    mostrarPromos()
    cod = input('Código de la promoción a utilizar: ')
    while busqPC(cod) == -1:
        cod = input('Promoción con tal código inexistente, intente de nuevo: ')
    cod = int(cod)
    tamArc, tamReg, cantR = sacarCant(apf, apl)
    apl.seek(cod*tamReg-tamReg)
    promo = pickle.load(apl)
    anodesde, mesdesde, diadesde = promo.desde.split('-')
    anohasta, meshasta, diahasta = promo.hasta.split('-')
    anodesde, mesdesde, diadesde, anohasta, meshasta, diahasta = int(anodesde), int(mesdesde), int(diadesde), int(anohasta), int(meshasta), int(diahasta)
    regdesde = datetime.date(anodesde, mesdesde, diadesde)
    reghasta = datetime.date(anohasta, meshasta, diahasta)
    hoy = datetime.date(2023, 12, 4)
    if hoy >= regdesde and hoy <= reghasta and promo.estado.strip() == 'Aprobada':
        Up = UsoPromo()
        Up.codCli = p
        Up.codPromo = promo.id
        Up.hoy = str(hoy).ljust(10, ' ')
        aupl.seek(os.path.getsize(aupf))
        pickle.dump(Up, aupl)
        aupl.flush()

        print("Promoción '"+promo.desc.strip()+"' utilizada.")
    elif hoy < regdesde or hoy > reghasta:
        print('Promoción no disponible el día de hoy, disponible del '+str(regdesde)+' al '+str(reghasta)+'.')
    elif promo.estado.strip() != 'Aprobada': 
        print('Promoción no aprobada en el momento.')
        
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
    
    U = Usuario()
    U.codigo = 3
    U.usuario = '3'.ljust(100, ' ')
    U.clave = '3'.ljust(8, ' ')
    U.tipo = 'Dueno'.ljust(13, ' ')
    pickle.dump(U, aul)
    print('--------------------------')
    aul.flush()


primerMenu()

print("Saliendo.........")
all.close()
aul.close()
apl.close()
aupl.close()
arul.close()