class Email:
    __idCuenta = ''
    __dominio = ''
    __tipoDominio = ''
    __password = ''


    def __init__(self, idc='', dominio='', tipodom='', pw=''):
        self.__idCuenta = idc
        self.__dominio = dominio
        self.__tipoDominio = tipodom
        self.__password = pw
        

    def getDominio(self):
        return self.__dominio

    def retornaEmail(self):
       mail = self.__idCuenta + "@" + self.__dominio + "." + self.__tipoDominio
       return mail 

    def modificarPassword(self, passwordvieja):
        if (passwordvieja == self.__password):
            self._passsowrd = input("Ingrese una nueva contraseña: ")
            print("La contraseña se cambió exitosamente.")
            return self._passsowrd

        


