
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
    def __init__(self,ciudad1,edificios1,persona1):
        self.ciudad1 = ciudad1
        self.edificios1 = edificios1
        self.persona1 = persona1
    def Edificios(self):
        self.edificios1 = "C"
    def Persona(self):
        self.persona1 = "señor Xing"


if __name__ == "__main__":
    ciudad = str(input("en que ciudad quieres que se produzca la tragedia(NewYork o LosAngeles)?: "))
    if ciudad == "NewYork":
        total = NuevaYork
        print(total.Edificios)
        print(total.Persona)
    elif ciudad == "LosAngeles":
        total1 = LosAngeles
        print(total1.Edificios)
        print(total1.Persona)
    else:
        print("Esa ciudad no esta disponible")
        pass