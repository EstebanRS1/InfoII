import datetime
class Animales:
    def __init__(self):
        self.__id=0
        self.__corral=0
        self.__habitat=""
        self.__peligro=""
        self.__especie=0
    
    #Setters

    def asignarId(self,id):
        self.__id=id
    def asignarCorral(self,corral):
        self.__corral=corral
    def asignarHabitat(self,habitat):
        self.__habitat=habitat
    def asignarPeligro(self,peligro):
        self.__peligro=peligro
    def asignarEspecie(self,especie):
        self.__especie=especie
    #Getters

    def verId(self):
        return self.__id
    def verCorral(self):
        return self.__corral
    def verHabitat(self):
        return self.__habitat
    def verPeligro(self):  
        return self.__peligro
    def verEspecie(self):
        return self.__especie
    
    def mostrar_info(self):
        print(f"Id: {self.__id}")
        print(f"Corral: {self.__corral}")
        print(f"Habitat: {self.__habitat}")
        print(f"Esta en Peligro: {self.__peligro}")
        #print(f"Especie: {self.__especie}")


class Bovino(Animales):
    

    def __init__(self):
        super().__init__()  # llama al constructor de la clase padre
        self.__nombre=""
        self.__sexo=""
        self.__edad=0
        self.__temperamento=""
        self.__especie=0

    #Setters
    def asignarNombre(self,nombre):
        self.__nombre=nombre
    def asignarSexo(self,sexo):
        self.__sexo=sexo
    def asignarEdad(self,edad):
        self.__edad=edad
    def asignarTemperamento(self,temperamento):
        self.__temperamento=temperamento

    def asignarEspecie(self,especie):
        self.__especie=especie

    #Getters
    def verNombre(self):
        return self.__nombre
    def verSexo(self):
        return self.__sexo
    def verEdad(self):
        return self.__edad
    def verTemperamento(self):
        return self.__temperamento
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Nombre: {self.__nombre}")
        print(f"Sexo: {self.__sexo}")
        print(f"Edad: {self.__edad}")
        print(f"Temperamento: {self.__temperamento}")

class Cabras(Animales):

    def __init__(self):
        super().__init__()  # llama al constructor de la clase padre
        self.__sexo=""
        self.__estudio=""
        self.__especie=0

    #Setters
    def asignarSexo(self,sexo):
        self.__sexo=sexo  
    def asignarEstudio(self,estudio):
        self.__estudio=estudio
    def asignarEspecie(self,especie):
        self.__especie=especie
    
    #Getters
    def verSexo(self):
        return self.__sexo
    def verEstudio(self):
        return self.__estudio

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Sexo: {self.__sexo}")
        print(f"Estudio: {self.__estudio}")

class Pollos(Animales):
    def __init__(self):
        super().__init__()  # llama al constructor de la clase padre
        self.__fechaE=datetime.datetime.now().strftime("%x")
        self.__alimento=""
        self.__color=""
        self.__especie=0

    #Setters
    def asignarFechaE(self,fechaE):
        self.__fechaE=fechaE
    def asignarAlimento(self,alimento):
        self.__alimento=alimento
    def asignarColor(self,color):
        self.__color=color
    def asignarEspecie(self,especie):
        self.__especie=especie

    #Getters
    def verFechaE(self):
        return self.__fechaE
    def verAlimento(self):
        return self.__alimento
    def verColor(self):
        return self.__color
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Fecha de Entrada: {self.__fechaE}")
        print(f"Alimento: {self.__alimento}")
        print(f"Color: {self.__color}")

class Otros(Animales):
    def __init__(self):
        super().__init__()  # llama al constructor de la clase padre
        self.__fechaI=datetime.datetime.now().strftime("%x")
        self.__motivo=""
        self.__fecharetiro=datetime.datetime.now().strftime("%x")
        self.__especie=0

    #Setters
    def asignarFechaI(self,fechaI):
        self.__fechaI=fechaI
    def asignarMotivo(self,motivo):
        self.__motivo=motivo
    def asignarFechaRetiro(self,fecharetiro):
        self.__fecharetiro=fecharetiro
    def asignarEspecie(self,especie):
        self.__especie=especie

    #Getters
    def verFechaI(self):
        return self.__fechaI
    def verMotivo(self):
        return self.__motivo
    def verFechaRetiro(self):
        return self.__fecharetiro
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Fecha de Ingreso: {self.__fechaI}")
        print(f"Motivo: {self.__motivo}")
        print(f"Fecha de Retiro: {self.__fecharetiro}")


class Sistema():
    def __init__(self):
        self.__listaAnimales={}#[id]=animal 

    def verificarExiste(self,c):
        return c in self.__listaAnimales
     
    def agregarAn(self,p):
        self.__listaAnimales[p.verId()]=p

    def verNumeroAnimales(self):
        return len(self.__listaAnimales)
    
    def eliminarAn(self,c):
        del self.__listaAnimales[c]
        return True
    
    def verAn(self,c):
        return self.__listaAnimales[c]       
    
    def verListadoAnimales(self):
        return self.__listaAnimales
    

       

#Validaciones
def validar(msj):
    while True:
        try:
            valor = int(input(msj))
            break
        except ValueError:
            print("Error!, Ingrese un dato numérico...")
    return valor

def main():
    #Menu
    mi_sistema = Sistema()
    while True:
        menu=validar('''\nIngrese una opción: 
                        \n1- Ingresar un Animal
                        \n2- Ver número de Animales en el servicio 
                        \n3- Ver Animal por ID
                        \n4- Eliminar Animal 
                        \n5- Salir 
                        \nUsted ingresó la opción: ''' )

        if menu == 1:
            
            id = validar(" Ingrese el identificador del Animal: ")
            if mi_sistema.verificarExiste(id) == False:
                corral=validar("Ingrese el corral de confinamiento (Número de fila y columna): ")
                habitat=input("Ingrese la Naturaleza de habitat (Terrestre, Acuático, Híbrido).: ").upper()
                peligro=input("¿Es una especie que representa peligro? (Sí/No): ").upper()
                while True:
                    tipo=validar("\nIngrese el tipo de animal \n1.Bovino. \n2.Cabra. \n3.Pollo \n4.Otro \n: ")
                    
                
                    if tipo == 1:
                        nombre=input("Ingrese el nombre del animal: ")
                        edad=validar("Ingrese la edad del animal: ")
                        sexo=input("Ingrese el sexo del animal(Macho o Hembra): ").upper()
                        temperamento=input("Ingrese el temperamento del animal(Agresivo o Calmado): ").upper()
                        masB=Bovino()
                        masB.asignarCorral(corral)
                        masB.asignarId(id)
                        masB.asignarHabitat(habitat)
                        masB.asignarPeligro(peligro)
                        masB.asignarEspecie(tipo) 
                        masB.asignarNombre(nombre)
                        masB.asignarEdad(edad)
                        masB.asignarSexo(sexo)
                        masB.asignarTemperamento(temperamento)  
                        mi_sistema.agregarAn(masB)
                        print("Mascota ingresada con exito")
                        break
                    elif tipo == 2:
                        sexo=input("Ingrese el sexo del animal(Macho o Hembra): ").upper()
                        estudio=input("¿Se encuentra bajo estudio? (Sí/No): ").upper()
                        masC=Cabras()
                        masC.asignarSexo(sexo)
                        masC.asignarEstudio(estudio)
                        masC.asignarEspecie(tipo)
                        masC.asignarCorral(corral)
                        masC.asignarId(id)
                        masC.asignarHabitat(habitat)
                        masC.asignarPeligro(peligro)

                        mi_sistema.agregarAn(masC)
                        print("Mascota ingresada con exito")
                        break
                    elif tipo == 3:
                        fechaE=input("Ingrese la fecha de ingreso del animal: ")
                        alimento=input("Ingrese el alimento que se le está suministrando: ")
                        color=input("Ingrese el color del animal: ")
                        masP=Pollos()
                        masP.asignarFechaE(fechaE)
                        masP.asignarAlimento(alimento)
                        masP.asignarColor(color)
                        masP.asignarEspecie(tipo)
                        masP.asignarCorral(corral)
                        masP.asignarId(id)
                        masP.asignarHabitat(habitat)
                        masP.asignarPeligro(peligro)
                        mi_sistema.agregarAn(masP)
                        print("Mascota ingresada con exito")
                        break
                    elif tipo == 4:
                        fechaI=validar("Ingrese la fecha de ingreso del animal: ")
                        motivo=input("Ingrese el motivo de ingreso del animal: ")
                        fecharetiro=validar("Ingrese la fecha de retiro del animal: ")
                        masO=Otros()
                        masO.asignarFechaI(fechaI)
                        masO.asignarMotivo(motivo)
                        masO.asignarFechaRetiro(fecharetiro)
                        masO.asignarEspecie(tipo)

                        masO.asignarCorral(corral)
                        masO.asignarId(id)
                        masO.asignarHabitat(habitat)
                        masO.asignarPeligro(peligro)
                        mi_sistema.agregarAn(masO)
                        print("Mascota ingresada con exito")
                        break
                    else:
                        print("Opción no válida, intente nuevamente")
                        continue
            else:
                print(f"Ya existe un Animal con el numero de ID {id}. Intente nuevamente") 


        elif menu==2:
            
            cv =len(mi_sistema.verListadoAnimales())
            print(cv)
        

        elif menu==3:#Ver Animal por ID
            identificacion= validar("Ingrese el numero de Identificacion que desea ver: ")
            if mi_sistema.verificarExiste(identificacion):
                p = mi_sistema.verAn(identificacion)           
                p.mostrar_info()
                  
            else:
                print(f"\nEl Identificador: {identificacion} no existe en el sistema")

                
        elif menu==4:
            q = validar("Ingrese el ID del Animal: ")
            if mi_sistema.verificarExiste(q):
                mi_sistema.eliminarAn(q)
                print("Animal eliminado del sistema con exito")
            else:
                print(f"El Animal con ID: {q} no existe en el sistema")

        elif menu==5:
            print("Usted ha salido del sistema de servicio del laboratorio")
            break

        else:
            print("Usted ingresó una opción no válida, intentelo nuevamente...")
if __name__ == "__main__":
    main()