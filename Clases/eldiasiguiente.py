ciudad = str(input("en que ciudad quieres que se produzca la tragedia(NewYork o LosAngeles)?: "))
edificios = ["A" , "B" ,"C"]
edificios_destruidos = []
empleados = ["señor Martín","señor Salim","señor Xing"]
empleados_masacrados = []
class destruccion:
    def __init__(self,ciudad,edificios,empleados,edificios_destruidos,empleados_masacrados):
        self.ciudad = ciudad
        self.edificios = edificios
        self.empleados = empleados
        self.edificios_destruidos = edificios_destruidos
        self.empleados_masacrados = empleados_masacrados
    def eleccion(self):
        if self.ciudad == "NewYork":
            edificios_destruidos.extend([edificios[0],edificios[1]])
            empleados_masacrados.extend([empleados[0],empleados[1]])
            print("Se ha destruido la ciudad de NewYork y las consecuencias son brutales!!!: ")
            print("Se han destruido los edificios",self.edificios_destruidos, "y se ha acabado con la vida de los empresarios ",self.empleados_masacrados)
        elif self.ciudad == "LosAngeles":
            edificios_destruidos.append(edificios[2])
            empleados_masacrados.append(empleados[2])
            print("Se ha destruido la ciudad de LosAngeles y las consecuencias son brutales!!!: ")
            print("Se han destruido los edificios",self.edificios_destruidos, "y se ha acabado con la vida de los empresarios ",self.empleados_masacrados)
            
final = destruccion(ciudad,edificios,empleados,edificios_destruidos,empleados_masacrados)
print(final.eleccion())