import os
import pickle
import os.path
import io

segundoaux = 0

class Usuario():
    def __init__(self):
        self.codigo = 0
        self.usuario = ''.ljust(100, ' ')
        self.clave = ''.ljust(8, ' ')
        self.tipo = ''.ljust(13, ' ')

class Local():
    def __init__(self):
        self.codigo = 0
        self.nombre = ''.ljust(50, ' ')
        self.ubicacion = ''.ljust(50, ' ')
        self.rubro = ''.ljust(12, ' ')
        
auf = r"C:\Users\tomas\OneDrive\Desktop\UTN\Algoritmos\proyecto-ayed-2023-git\USUARIOS.dat"
alf = r"C:\Users\tomas\OneDrive\Desktop\UTN\Algoritmos\proyecto-ayed-2023-git\LOCALES.dat"


if os.path.exists(auf):
    aul = open(auf, 'r+b')
else:
    aul = open(auf, 'w+b')

def primerMenu():
    global segundoaux
    print('''
        1- Ingresar como usuario registrado.
        2- Registrarse como cliente.
        3- Salir.
        ''')
    eleccion = input("Seleccione una número: ")
    while eleccion != '3' and segundoaux == 0:
        while eleccion != '1' and eleccion != '2' and eleccion != '3':
            print("Elección no válida.")
            eleccion = input("Seleccione una opción: ")
        match eleccion:
            case '1':
                ingreso()
            case '2':
                registro()
            case '3':
                print("Saliendo...")
        if segundoaux == 0:
            print('''
                1- Ingresar como usuario registrado.
                2- Registrarse como cliente.
                3- Salir.
                ''')
            eleccion = input("Seleccione una número:  ")

def mostrarUs():
    aul.seek(0)
    while aul.tell() < os.path.getsize(auf):
        reg = pickle.load(aul)
        print(reg.codigo)
        print(reg.usuario)
        print(reg.clave)
        print(reg.tipo)
        print('-------------------------------')
        
def registro():
    U = Usuario()
    ingresarDatos(U)
    while busqCli(U.usuario, U.clave) == 'T' or busqCli(U.usuario, U.clave) == 'TT': 
        ingresarDatos(U)
    U.codigo = sacarUCod()
    U.tipo = 'Cliente'
    aul.seek(os.path.getsize(auf))
    pickle.dump(U, aul)
    print(os.path.getsize(auf))
    aul.flush()
    mostrarUs()


def sacarCant():
    tamArc = os.path.getsize(auf)
    aul.seek(0)
    pickle.load(aul)
    tamReg = aul.tell()
    iterador = tamArc // tamReg
    return iterador

def sacarUCod():
    aul.seek(0)
    aux = True
    while True and aux == True:
        try:
            reg = pickle.load(aul)
        except EOFError:
            aux = False
    return reg.codigo + 1 

def ingresarDatos(x):
    x.usuario = input('Ingrese mail de usuario: ')
    while len(x.usuario) > 100:
        print('Debe de ser un usuario de máximo 100 caracteres. Ingrese de nuevo: ')
        x.usuario = input('>>  ')

    x.clave = input('Ingrese clave de usuario: ')
    while len(x.clave) > 8:
        print('Debe de ser una clave de máximo 8 caracteres. Ingrese de nuevo: ')
        x.clave = input('>>  ')
    
                


def busqCli(x,y):
    global tipo
    tamArc = os.path.getsize(auf)
    aul.seek(0)
    aux = 'F'
    while aul.tell() < tamArc and aux == 'F':
        reg = pickle.load(aul)
        if reg.usuario == x and reg.clave == y:
            print('Usuario existente con este usuario y clave.')
            ## agregar redireccion a ingreso
            tipo = reg.tipo
            aux = 'T'
        elif reg.usuario == x:
            print('Usuario existente con este usuario.')
            aux = 'TT'
    return aux



if os.path.getsize(auf) == 0:
    U = Usuario()
    U.codigo = 1
    U.usuario = '1'
    U.clave = '1'
    U.tipo = 'Administrador'
    aul.seek(0)
    pickle.dump(U, aul)
    ptam = os.path.getsize(auf)
    print('--------------------------')
    aul.flush()
    
    U = Usuario()
    U.codigo = 2
    U.usuario = '2'
    U.clave = '2'
    U.tipo = 'Dueno'
    aul.seek(0)
    pickle.dump(U, aul)
    ptam = os.path.getsize(auf)
    print('--------------------------')
    aul.flush()
else:
    print(os.path.getsize(auf))
    print('--------------------------')
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
    
    auxxx = 1
    tipo = ''
    
    while auxxx < 3:
        match busqCli(usuario, clave):
            case 'T':
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
       
    
if segundoaux == 0:
    primerMenu()
print("Saliendo.........")