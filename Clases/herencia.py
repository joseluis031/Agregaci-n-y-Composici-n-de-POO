class Pared:
    def __init__(self,orientacion):
        self.orientacion = orientacion
        
class Ventana(Pared):
    def __init__(self,orientacion,superficie):
        self.superficie = superficie
        Pared.__init__(self,orientacion)
        
class Casa(Ventana):
    def __init__(self,orientacion,superficie,paredes):
        self.paredes = paredes
        Ventana.__init__(self,orientacion,superficie)


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