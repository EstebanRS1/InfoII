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
            return self.__listaAnimales[id].verFechaI()
        return None
    
    def verAn(self,c):
        return self.__listaAnimales[c]
    
    def verListadoAnimales(self):
        return self.__listaAnimales
    

    def eliminarAnimal(self, id):
        if id in self.__listaAnimales:
            del self.__listaAnimales[id]
            return True #eliminado con exito
        return False

#Validaciones
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
            corral=input("Ingrese el corral de confinamiento (Número de fila y columna): ")
            habitat=input("Ingrese la Naturaleza de habitat (Terrestre, Acuático, Híbrido).: ").upper()
            peligro=input("¿Es una especie que representa peligro? (Sí/No): ").upper()
            tipo=validar("\nIngrese el tipo de animal \n1.Bovino. \n2.Cabra. \n3.Pollo \n4.Otro \n: ")
            
            mas = Animales()
            mas.asignarCorral(corral)
            mas.asignarId(id)
            mas.asignarHabitat(habitat)
            mas.asignarPeligro(peligro)
            mi_sistema.ingresarAnimal(mas)
            
            masB=Bovino()
            masC=Cabras()
            if tipo == 1:
                nombre=input("Ingrese el nombre del animal: ")
                edad=validar("Ingrese la edad del animal: ")
                sexo=input("Ingrese el sexo del animal(Macho o Hembra): ").upper()
                temperamento=input("Ingrese el temperamento del animal(Agresivo o Calmado): ").upper()
                masB.asignarNombre(nombre)
                masB.asignarEdad(edad)
                masB.asignarSexo(sexo)
                masB.asignarTemperamento(temperamento)   
                mi_sistema.ingresarAnimal(masB)
                print("Mascota ingresada con exito")

            elif tipo == 2:
                sexo=input("Ingrese el sexo del animal(Macho o Hembra): ").upper()
                estudio=input("¿Se encuentra bajo estudio? (Sí/No): ").upper()
                masC.asignarSexo(sexo)
                masC.asignarEstudio(estudio)
                mi_sistema.ingresarAnimal(masC)
                print("Mascota ingresada con exito")
            
            elif tipo == 3:
                fechaE=input("Ingrese la fecha de ingreso del animal: ")
                alimento=input("Ingrese el alimento que se le está suministrando: ")
                color=input("Ingrese el color del animal: ")
                masP=Pollos()
                masP.asignarFechaE(fechaE)
                masP.asignarAlimento(alimento)
                masP.asignarColor(color)
                mi_sistema.ingresarAnimal(masP)
                print("Mascota ingresada con exito")
            
            elif tipo == 4:
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
                print("Opción no válida, intente nuevamente")


        else:
            print(f"Ya existe un Animal con el numero de ID {id}. Intente nuevamente") 


    elif menu==2:
        #print(mi_sistema.verAnimales())
        # Idd1= validar(" Ingrese el identificador del Animal: ")
        # if mi_sistema.verificarExiste(Idd1):
        #     p = mi_sistema.verAn(Idd1)
        cv =len(mi_sistema.verListadoAnimales())
        print(cv)
        #     print(f"El Animal {p.verId()} tiene {cv} visitas")
        # else:
        #     print("El Animal no existe en el sistema, intente nuevamente")
        # numero=mi_sistema.verNumeroAnimales()
        # print("El número de Animales en el sistema es: " + str(numero))

    elif menu==3:
        q = validar("Ingrese el ID de la mascota: ")
        ann=mi_sistema.verListadoAnimales()
        print(ann)
        
    elif menu==4:
        q = validar("Ingrese el ID del Animal: ")
        resultado_operacion = mi_sistema.eliminarAnimal(q) 
        if resultado_operacion == True:
            print("Animal eliminado del sistema con exito")
        else:
            print("No se ha podido eliminar el Animal, intente nuevamente")

    elif menu==5:
        print("Usted ha salido del sistema de servicio del laboratorio")
        break

    else:
        print("Usted ingresó una opción no válida, intentelo nuevamente...")