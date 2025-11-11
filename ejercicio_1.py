#21

""" print("--FUNCIONASHOP--\n")

def saludo():
    print("Bienvenido a Funcionashop.") """

#22

""" print("--STRONGFIT--\n")

def calcularenergia():
    while True:
        
        try:
            
            rep = int(input("Ingrese el número de repeticiones aquí: "))
    
            if rep >= 5:
                print("¡Buen trabajo!")
                break
            else:
                print("Necesitas más esfuerzo")
                break
                
        except ValueError:
            print("Porfavor ingrese solo números.\n")
            
calcularenergia() """

#23

""" print("--LOOPBANK--\n")

def calcularinteres():
    
    while True:
        
        try:
            
            monto = float(input("\nIngrese el monto aquí(SOLO NÚMEROS): "))
            tasa = float(input("\nIngrese el porcentaje de la tasa\nde interes aquí (SOLO NÚMEROS): "))
            monto_final = monto * (1 + (tasa / 100))
            
            print(f"\nEl monto final es ${monto_final:.2f}.")
            break
        
        except ValueError:
            print("Ingresa solo números.\n")
            
calcularinteres() """

#24

""" print("--APRENDE CON FUNCIONES--\n")

def promedionotas():
    
    while True:
        
        try:
            
            nota_1 = float(input("Ingrese aquí la nota #1: "))
            nota_2 = float(input("Ingrese aquí la nota #2: "))
            nota_3 = float(input("Ingrese aquí la nota #3: "))
            
            if nota_1 < 1.0 or nota_1 > 5.0:
                print("\nLas notas deben estar entre 1.0 y 5.0")               
            elif  nota_2 < 1.0 or nota_2 > 5.0:
                print("\nLas notas deben estar entre 1.0 y 5.0")
            elif  nota_3 < 1.0 or nota_3 > 5.0:
                print("\nLas notas deben estar entre 1.0 y 5.0")
            else:
          
                promedio = (nota_1 + nota_2 + nota_3) / 3
            
                if promedio >= 3.0:
                    print("\nAprobado.")
                    break
                else:
                    print("\nReprobado.")    
                    break
        except ValueError:
            print("Ingrese solo numeros decimales.\n")
            
promedionotas() """

#25

""" print("--BUENAFUNCIÓN--\n")

def verificarturno():
    while True:
        
        try:
            
            hora = float(input('Ingrese aqui la hora\n(de esta manera (00.00-23.59), sin "pm" o "am"): '))
            
            if hora > 23.59 or hora < 00.00:
                print("Porfavor ingrese un número entre 00.00 y 23.59.\n")
                
            if hora > 18.00:
                print("Turno de noche.")
                break
            elif hora <= 18.00 and hora >= 12.00:
                print("Turno de tarde.")
                break
            else:
                print("Turno mañana")
                break           
        
        except ValueError:
            print("Porfavor ingrese solo números decimales.\n")
            
verificarturno() """


