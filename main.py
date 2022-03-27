if __name__ == "__main__":  
    ciudad = str(input("en que ciudad quieres que se produzca la tragedia(NewYork o LosAngeles)?: "))
    edificios = []
    persona = []
    
    if ciudad == "NewYork":
        from Clases.eldia2 import NuevaYork
        total = NuevaYork(ciudad, edificios, persona)
        print(total.Edificios())
        print(total.Persona())
    elif ciudad == "LosAngeles":
        from Clases.eldia2 import LosAngeles
        total1 = LosAngeles(ciudad,edificios,persona)
        print(total1.Edificios())
        print(total1.Persona())
    else:
        print("Esa ciudad no esta disponible")
        pass