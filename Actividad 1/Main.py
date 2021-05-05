from Manejador import Manejador
from Email import Email
import csv

def imprimir():
    print('')
    print("---------- MENU --------")
    print("Opciones disponibles:")
    print("1. Ingresar datos para crear un Email")
    print("2. Cambiar contraseña ")
    print("3. Crear objeto a partir de un email")
    print("4. Contar cuantos email coinciden con el dominio")
    print("0. Salir")
    print()

def menu():
    band = True
    while band:
        imprimir()
        opcion=int(input("Ingrese Opcion: "))
        if opcion == 1:
            nombre = input("Ingrese Nombre: ")
            idCuenta = input("Ingrese idCuenta: ")
            dominio = input("Ingrese Dominio: ")
            tipoDominio = input("Ingrese tipo de Dominio: ")
            password = input("Ingrese contraseña: ")
            mail = Email(idCuenta, dominio, tipoDominio, password)

            print("Estimado {} te enviaremos tus mensajes a la dirección {}".format(nombre, mail.retornaEmail()))
        
        elif opcion == 2:
            print('')
            print("Se cambiará su contraseña actual. ")
            print('')
            password = input("Ingrese su contraseña: ")
            print("\nLa contraseña nueva es: {}".format(mail.modificarPassword(password)))

        elif opcion == 3:
            print('')
            print("Se creará un objeto de clase Email.")
            mail = input("Ingrese un mail: ")
            correo = Manejador(mail)
            objetonuevo = correo.crearObjeto()
            if isinstance(objetonuevo, Email):
            #if type(objetonuevo) == Email:
                print("El objeto creado es: ", mail)
                print("El identificador del objeto creado es: ", objetonuevo)
                print('')
                
        elif opcion == 4:
            print('')
            archivo = open('email.csv')
            dominio = input("Ingrese un dominio: ")
            cont = 0
            reader = csv.reader(archivo, delimiter = ';')
            for fila in reader:
                if fila[1] == dominio:
                    cont+=1
                 
            print("La cantidad de mails con el dominio ingresado es: {}".format(cont))
        
        elif opcion == 0:
            band = False
            print("Programa finalizado")
        else:
            print("Ingreso mal la opción.")
            print('')
            archivo.close()


if __name__ == '__main__':

    menu()
