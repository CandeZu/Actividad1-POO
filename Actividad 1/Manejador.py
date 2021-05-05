from Email import Email

class Manejador:
    __email = ''
    
    def __init__(self, mail=''):
        self.__email = mail
    
    def crearObjeto(self):
        if (self.__email.find("@")!=-1) & (self.__email.find(".")!=-1):
            idCuenta= self.__email[:self.__email.find("@")]
            dominio= self.__email[self.__email.find("@") + 1 : self.__email.find(".")]
            tipoDominio= self.__email[self.__email.find(".") + 1 :]
            password = input("Ingrese la contraseña: ")
            nuevoemail = Email(idCuenta, dominio, tipoDominio, password)
            print('IdCuenta: ',idCuenta)
            print('Dominio: ', dominio)
            print('Tipo de dominio: ',tipoDominio)
            print('Contraseña: ',password)
            return(nuevoemail)
        else:
            print('ERROR')


