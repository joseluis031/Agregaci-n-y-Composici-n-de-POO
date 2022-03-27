edificios = []
persona = []
class NuevaYork:
    def __init__(self,ciudad,edificios,persona):
        self.ciudad = ciudad
        self.edificios = edificios
        self.persona = persona
    def Edificios(self):
        self.edificios.extend(["A","B"])
        print("En NuevaYork se encuentran los edificios", self.edificios)
    def Persona(self):
        self.persona.extend(["señor Martín","señor Salim"])
        print("En NuevaYork se encuentran los empleados", self.persona)
class LosAngeles:
    def __init__(self,ciudad,edificios,persona):
        self.ciudad = ciudad
        self.edificios = edificios
        self.persona = persona
    def Edificios(self):
        self.edificios.append("C")
        print("En LosAngeles se encuentra el edificio",self.edificios)
    def __del__(self):
        print("El edificio",self.edificios,"ha sido derrumbado")
    def Persona(self):
        self.persona.append("señor Xing")
        print("En LosAngeles se encuentra el empleado", self.persona)

