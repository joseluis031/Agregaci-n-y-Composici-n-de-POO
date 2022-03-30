# Agregaci-n-y-Composici-n-de-POO
La dirección de este repositorio es la siguiente:[GitHub](https://github.com/joseluis031/Agregaci-n-y-Composici-n-de-POO.git)

## Ejercicio 1
--El código es el siguiente:
```
class NuevaYork:
    def __init__(self,ciudad,edificios,persona):
        self.ciudad = ciudad
        self.edificios = edificios
        self.persona = persona
    def __del__(self):
        print("Los edificios",self.edificios,"han sido derrumbados")
        print("Los empleados",self.persona,"han muerto")
    def Edificios(self):
        self.edificios.extend(["A","B"])
        print("En NuevaYork se encuentran los edificios")
        return self.edificios
    def Persona(self):
        self.persona.extend(["señor Martín","señor Salim"])
        print("En NuevaYork se encuentran los empleados")
        return self.persona
class LosAngeles:
    def __init__(self,ciudad,edificios,persona):
        self.ciudad = ciudad
        self.edificios = edificios
        self.persona = persona
    def __del__(self):
        print("El edificio",self.edificios,"ha sido derrumbado")
        print("El empleado",self.persona,"ha muerto")
    def Edificios(self):
        self.edificios.append("C")
        print("En LosAngeles se encuentra el edificio")
        return self.edificios
    def Persona(self):
        self.persona.append("señor Xing")
        print("En LosAngeles se encuentra el empleado")
        return self.persona
```

--Su UML es el siguiente:


![UML Dia siguiente](https://user-images.githubusercontent.com/91721888/160854625-4d57e50a-9028-4973-8b51-b917537f43a9.png)


## Ejercicio 2
```
class Yin: pass 
class Yang: 
    def __del__(self): 
        print("Yang destruido") 
 
yin = Yin() 
yang = Yang() 
yin.yang = yang 
 
print(yang)  
print(yang is yin.yang)  
del(yang) 
print("?") 
#Aparece despues porque utilizabamos 2 instancias Yang, y al final vemos Yang destruido porque al final del programa seguiamos manteniendo 1 de esas 2 instancias
```

--Su UML es el siguiente:


![UML Ying Yang](https://user-images.githubusercontent.com/91721888/160922140-2b7e80d6-1a57-4aee-9445-d99b99236e1f.png)

## Ejercicio 3

--Su codigo es el siguiente:
```
class Pared:
    def __init__(self,orientacion,):
        self.orientacion = orientacion
class Ventana:
    def __init__(self,superficie,pared):
        self.superficie = superficie
        self.pared = pared
        
        
class Casa:
    def __init__(self,paredes):
        self.paredes = paredes
        self.ventanas = []
    def superficie_acristalada(self):
        self.superficie = 0
        for ventana in self.paredes:
            self.superficie += ventana.superficie
            return self.superficie
        
        

# Instanciación de las paredes 
pared_norte = Pared("NORTE") 
pared_oeste = Pared("OESTE") 
pared_sur = Pared("SUR") 
pared_este = Pared("ESTE") 
# Instanciación de las ventanas 
ventana_norte = Ventana(pared_norte, 0.5) 
ventana_oeste = Ventana(pared_oeste, 1) 
ventana_sur = Ventana(pared_sur, 2) 
ventana_este = Ventana(pared_este, 1) 
# Instanciación de la casa con las 4 paredes 
casa = Casa([pared_norte, pared_oeste, pared_sur, pared_este]) 
print(casa.superficie_acristalada())   

class ParedCortina(Pared,Ventana):
    def __init__(self,orientacion,superficie,pared):
       Pared.__init__(self,orientacion)
       Ventana.__init__(self,pared,superficie)

pared_cortina = ParedCortina("Este", 10)
```

--Su UML es el siguiente:

![UML Herenciamult_paredcortina](https://user-images.githubusercontent.com/91721888/160937035-60460752-942d-4c65-997c-be0bf706cf4b.png)
