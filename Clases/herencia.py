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