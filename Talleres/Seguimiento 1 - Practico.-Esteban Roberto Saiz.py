import datetime
class Animales:
    def __init__(self):
        self.__id=0
        self.__corral=""
        self.__habitat=""
        self.__peligro=""
    
    #Setters

    def asignarId(self,id):
        self.__id=id
    def asignarCorral(self,corral):
        self.__corral=corral
    def asignarHabitat(self,habitat):
        self.__habitat=habitat
    def asignarPeligro(self,peligro):
        self.__peligro=peligro
    
    #Getters

    def verId(self):
        return self.__id
    def verCorral(self):
        return self.__corral
    def verHabitat(self):
        return self.__habitat
    def verPeligro(self):  
        return self.__peligro


class Bovino(Animales):
    

    def __init__(self):
        super().__init__()  # llama al constructor de la clase padre
        self.__nombre=""
        self.__sexo=""
        self.__edad=0
        self.__temperamento=""

    #Setters
    def asignarNombre(self,nombre):
        self.__nombre=nombre
    def asignarSexo(self,sexo):
        self.__sexo=sexo
    def asignarEdad(self,edad):
        self.__edad=edad
    def asignarTemperamento(self,temperamento):
        self.__temperamento=temperamento

    #Getters
    def verNombre(self):
        return self.__nombre
    def verSexo(self):
        return self.__sexo
    def verEdad(self):
        return self.__edad
    def verTemperamento(self):
        return self.__temperamento

class Cabras(Animales):

    def __init__(self):
        super().__init__()  # llama al constructor de la clase padre
        self.__sexo=""
        self.__estudio=""

    #Setters
    def asignarSexo(self,sexo):
        self.__sexo=sexo  
    def asignarEstudio(self,estudio):
        self.__estudio=estudio

    #Getters
    def verSexo(self):
        return self.__sexo
    def verEstudio(self):
        return self.__estudio

class Pollos(Animales):
    def __init__(self):
        super().__init__()  # llama al constructor de la clase padre
        self.__fechaE=datetime.datetime.now().strftime("%x")
        self.__alimento=""
        self.__color=""

    #Setters
    def asignarFechaE(self,fechaE):
        self.__fechaE=fechaE
    def asignarAlimento(self,alimento):
        self.__alimento=alimento
    def asignarColor(self,color):
        self.__color=color

    #Getters
    def verFechaE(self):
        return self.__fechaE
    def verAlimento(self):
        return self.__alimento
    def verColor(self):
        return self.__color

class Otros(Animales):
    def __init__(self):
        super().__init__()  # llama al constructor de la clase padre
        self.__fechaI=datetime.datetime.now().strftime("%x")
        self.__motivo=""
        self.__fecharetiro=datetime.datetime.now().strftime("%x")

    #Setters
    def asignarFechaI(self,fechaI):
        self.__fechaI=fechaI
    def asignarMotivo(self,motivo):
        self.__motivo=motivo
    def asignarFechaRetiro(self,fecharetiro):
        self.__fecharetiro=fecharetiro
    
    #Getters
    def verFechaI(self):
        return self.__fechaI
    def verMotivo(self):
        return self.__motivo
    def verFechaRetiro(self):
        return self.__fecharetiro

class Sistema():
    def __init__(self):
        self.__listaAnimales={}#[id]=animal 
        # self.__lista_bovino=[]
        # self.__lista_cabras=[]
        # self.__lista_pollos=[]
        # self.__lista_otros=[]

    def verificarExiste(self,id):
        if id in self.__listaAnimales:
            return True
        #solo luego de haber recorrido todo el ciclo se retorna False
        return False
    
    def verNumeroAnimales(self):
        return len(self.__listaAnimales)
    
    def ingresarAnimal(self,animal):
        if self.verificarExiste(animal.verId()):
            return False
        else:
            self.__listaAnimales[animal.verId()] = animal
            return True
        
    def verFechaIngreso(self,id):
        #busco la mascota y devuelvo el atributo solicitado
        if id in self.__listaAnimales:
            return self.__listaAnimales[id].verId()
        return None
    
    def verAn(self,c):
        return self.__listaAnimales[c]
    
    # def verAnimales(self, id):
    #     for id, animal in self.__listaAnimales.items():
    #         print(f"ID: {id}")
    #         print(f"Tipo de animal: {type(animal).__name__}")
    #         print(f"Nombre: {id.verNombre()}" if isinstance(id, Bovino) else "")
    #         print(f"Sexo: {id.verSexo()}")
    #         print(f"Edad: {id.verEdad()}" if isinstance(id, Bovino) else "")
    #         print(f"Habitat: {id.verHabitat()}")
    #         print(f"Fecha de ingreso: {id.verFechaI()}")
    #         print()

    def eliminarAnimal(self, id):
        if id in self.__listaAnimales:
            del self.__listaAnimales[id]
            return True #eliminado con exito
        return False

def validar(msj):
    while True:
        try:
            valor = int(input(msj))
            break
        except ValueError:
            print("Error!, Ingrese un dato numérico...")
    return valor

def validarf(cc):
    while True:
        try:
            valor=float(input(cc))
            break
        except ValueError:
            print("Error, ingrese un valor valido")
    return valor


mi_sistema = Sistema()
while True:
    menu=int(input('''\nIngrese una opción: 
                    \n1- Ingresar un Animal
                    \n2- Ver número de Animales en el servicio 
                    \n3- Ver Animal por ID
                    \n4- Eliminar Animal 
                    \n5- Salir 
                    \nUsted ingresó la opción: ''' ))

    if menu == 1:
        
        id = validar(" Ingrese el identificador del Animal: ")
        if mi_sistema.verificarExiste(id) == False:
            corral=input("Ingrese el corral de confinamiento (Número de fila y columna): ")
            habitat=input("Ingrese la Naturaleza de habitat (Terrestre, Acuático, Híbrido).: ").upper()
            peligro=input("¿Es una especie que representa peligro? (Sí/No): ").upper()
            tipo=input("Ingrese el tipo de animal (Bovino, Cabra, Pollo, Otro): ").upper()
            
            mas = Animales()
            mas.asignarCorral(corral)
            mas.asignarId(id)
            mas.asignarHabitat(habitat)
            mas.asignarPeligro(peligro)
            mi_sistema.ingresarAnimal(mas)
            
            masB=Bovino()
            masC=Cabras()
            if tipo == "BOVINO":
                nombre=input("Ingrese el nombre del animal: ")
                edad=int(input("Ingrese la edad del animal: "))
                sexo=input("Ingrese el sexo del animal(Macho o Hembra): ").upper()
                temperamento=input("Ingrese el temperamento del animal(Agresivo o Calmado): ").upper()
                masB.asignarNombre(nombre)
                masB.asignarEdad(edad)
                masB.asignarSexo(sexo)
                masB.asignarTemperamento(temperamento)   
                mi_sistema.ingresarAnimal(masB)
                print("Mascota ingresada con exito")

            elif tipo == "CABRA":
                sexo=input("Ingrese el sexo del animal(Macho o Hembra): ").upper()
                estudio=input("¿Se encuentra bajo estudio? (Sí/No): ").upper()
                masC.asignarSexo(sexo)
                masC.asignarEstudio(estudio)
                mi_sistema.ingresarAnimal(masC)
                print("Mascota ingresada con exito")
            
            elif tipo == "POLLO":
                fechaE=input("Ingrese la fecha de ingreso del animal: ")
                alimento=input("Ingrese el alimento que se le está suministrando: ")
                color=input("Ingrese el color del animal: ")
                masP=Pollos()
                masP.asignarFechaE(fechaE)
                masP.asignarAlimento(alimento)
                masP.asignarColor(color)
                mi_sistema.ingresarAnimal(masP)
                print("Mascota ingresada con exito")
            
            elif tipo == "OTRO":
                fechaI=input("Ingrese la fecha de ingreso del animal: ")
                motivo=input("Ingrese el motivo de ingreso del animal: ")
                fecharetiro=input("Ingrese la fecha de retiro del animal: ")
                masO=Otros()
                masO.asignarFechaI(fechaI)
                masO.asignarMotivo(motivo)
                masO.asignarFechaRetiro(fecharetiro)
                mi_sistema.ingresarAnimal(masO)
                print("Mascota ingresada con exito")


        else:
            print("Ya existe un Animal con el numero de ID ingresado.") 


    elif menu==2:
        print(mi_sistema.verAnimales())
        # numero=mi_sistema.verNumeroAnimales()
        # print("El número de Animales en el sistema es: " + str(numero))

    elif menu==3:
        q = int(input("Ingrese el ID de la mascota: "))
        ann=mi_sistema.verAnimales(q)
        print(ann)
       


    elif menu==4:
        q = int(input("Ingrese el ID del Animal: "))
        resultado_operacion = mi_sistema.eliminarAnimal(q) 
        if resultado_operacion == True:
            print("Animal eliminado del sistema con exito")
        else:
            print("No se ha podido eliminar el Animal")

    elif menu==5:
        print("Usted ha salido del sistema de servicio del laboratorio")
        break

    else:
        print("Usted ingresó una opción no válida, intentelo nuevamente...")

 
    # elif menu == 2:
    #     print("Número total de pacientes: " + str(mi_sistema.verNumeroPacientes()))
    # elif menu == 3:
    #     mi_sistema.verDatosPacientes()
    # elif menu == 4:
    #     break
    # else: 
    #     print("Opción inválida")