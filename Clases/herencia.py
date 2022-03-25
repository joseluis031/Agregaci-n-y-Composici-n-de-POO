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
        