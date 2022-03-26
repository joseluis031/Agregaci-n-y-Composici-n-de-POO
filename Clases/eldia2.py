class NuevaYork:
    def __init__(self,ciudad,edificios,persona):
        self.ciudad = ciudad
        self.edificios = edificios
        self.persona = persona
    def Edificios(self):
        self.edificios = ["A" , "B"]
    def Persona(self):
        self.persona = ["señor Martín","señor Salim"]
        
class LosAngeles:
    def __init__(self,ciudad,edificios,persona):
        self.ciudad = ciudad
        self.edificios = edificios
        self.persona = persona
    def Edificios(self):
        self.edificios = "C"
    def Persona(self):
        self.persona = ["señor Xing"]
