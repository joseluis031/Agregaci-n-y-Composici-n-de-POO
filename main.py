if __name__ == "__main__":  
    main = int(input("Que ejercicio deseas realizar(1,2 o 3):"))
    if main == 1:
        ciudad = str(input("En que ciudad quieres que se produzca la tragedia(NewYork o LosAngeles)?: "))
        edificios = []
        persona = []
        
        if ciudad == "NewYork":
            from Clases.eldia2 import NuevaYork
            total = NuevaYork(ciudad, edificios, persona)
            print(total.Edificios())
            print(total.Persona())
            print("Ha habido fuertes consecuencias...:")
            del total
            #print(total.Edificios()) ya me dice que no esta definido porque he utilizado el destructor
        elif ciudad == "LosAngeles":
            from Clases.eldia2 import LosAngeles
            total1 = LosAngeles(ciudad,edificios,persona)
            print(total1.Edificios())
            print(total1.Persona())
            print("Ha habido fuertes consecuencias...:")
            del total1
            #print(total1.Edificios()) ya me dice que no esta definido porque he utilizado el destructor
        else:
            print("Esa ciudad no esta disponible")
            pass
    elif main == 2:
        from Clases.inmortal import *
          
        yin = Yin() 
        yang = Yang() 
        yin.yang = yang 
        
        print(yang)  
        print(yang is yin.yang)  
        del(yang) 
        print("?")
    elif main ==3:
        from Clases.herencia import *
        casa = Casa([pared_norte, pared_oeste, pared_sur, pared_cortina]) 
        print(casa.superficie_acristalada())