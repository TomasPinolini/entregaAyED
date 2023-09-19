def ingreso():
    U = Usuario()
    U.usuario = input('Ingrese mail de usuario: ')
    U.clave = input('Ingrese clave de usuario: ')
    
    if busqueda(aul, U.usuario, U.clave):
        tipo = busquedaTipo(aul, U.usuario)
        match tipo:
            case 'Administrador':
                menuAdmin()
            case 'DuenoLocal':
                menuDue()
            case 'Cliente':
                menuCli()
    
def menuAdmin():
    print('menu')
    elec = input()
    match elec:
        case 1:
            gestionDeLocales()
        case 2:
            crearCuentasDueno()
        case 3:
            solDesc()
        case 4:
            gestionNovedades()
        case 5:
            reporteDesc()
        case 0:
            print('Saliendo...')
    #hacer hasta elec = 0

def menuDue():
    print('menu')
    elec = input()
    match elec:
        case 1:
            crearDesc()
        case 2:
            rDesc()
        case 3:
            verNov()
        case 0:
            print('Saliendo...')

def menuCli():
    print('menu')
    elec = input()
    match elec:
        case 1:
            buscarDesc()
        case 2:
            solDesc()
        case 3:
            verNovv()
        case 0:
            print('Saliendo...')
