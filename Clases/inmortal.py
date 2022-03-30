class Yin: pass 
class Yang: 
    def __del__(self): 
        print("Yang destruido") 
 

#Aparece despues porque utilizabamos 2 instancias Yang, y al final vemos Yang destruido porque al final del programa seguiamos manteniendo 1 de esas 2 instancias