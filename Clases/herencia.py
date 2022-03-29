class Pared:
    def __init__(self,orientacion,ventanas):
        self.orientacion = orientacion
        self.ventanas = ventanas
class Ventana(Pared):
    def __init__(self,orientacion,ventanas,superficie,pared):
        self.superficie = superficie
        self.pared = pared
        Pared.__init__(self,orientacion,ventanas)
        
class Casa(Ventana):
    def __init__(self,orientacion,superficie,paredes):
        self.paredes = paredes
        Ventana.__init__(self,orientacion,superficie)
    def cristal(self):
        self.superficie = 0
        for ventana in self.ventanas:
            self.superficie += ventana.superficie()
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