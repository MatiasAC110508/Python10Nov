"""24. Escuela “Aprende con Funciones” -- Promedio de notas
Como profesor, quiero crear una función promedioNotas() que reciba tres notas y calcule el promedio.
Si el promedio es mayor o igual a 3.0, mostrar “Aprobado”; si no, “Reprobado”."""

print("--APRENDE CON FUNCIONES--\n")

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
            
promedionotas()