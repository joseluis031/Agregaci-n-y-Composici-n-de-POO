edificios = []
persona = []
class NuevaYork:
    def __init__(self,ciudad,edificios,persona):
        self.ciudad = ciudad
        self.edificios = edificios
        self.persona = persona
    def Edificios(self):
        self.edificios.extend = (["A","B"])
    def Persona(self):
        self.persona.extend = (["señor Martín","señor Salim"])
class LosAngeles:
    def __init__(self,ciudad,edificios,persona):
        self.ciudad = ciudad
        self.edificios = edificios
        self.persona = persona
    def Edificios(self):
        self.edificios.append("C")
        print("En LosAngeles se encuentra el edificio C")
    def Persona(self):
        self.persona.append("señor Xing")

if __name__ == "__main__":  
    ciudad = str(input("en que ciudad quieres que se produzca la tragedia(NewYork o LosAngeles)?: "))
    if ciudad == "NewYork":
        from Clases.eldia2 import NuevaYork
        total = NuevaYork(ciudad, edificios, persona)
        print(total.Edificios)
        print(total.Persona)
    elif ciudad == "LosAngeles":
        from Clases.eldia2 import LosAngeles
        total1 = LosAngeles(ciudad,edificios,persona)
        print(total1.Edificios)
        print(total1.Persona)
    else:
        print("Esa ciudad no esta disponible")
        pass