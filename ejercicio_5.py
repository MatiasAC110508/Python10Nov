"""25. Restaurante “BuenaFunción” -- Verificación de turno
Como gerente, quiero una función verificarTurno(hora) que determine:

    Si la hora es menor que 12 → “Turno de mañana”.
    Si está entre 12 y 18 → “Turno de tarde”.
    Si es mayor → “Turno de noche”.
    El programa principal debe pedir la hora e imprimir el resultado."""
    
print("--BUENAFUNCIÓN--\n")

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
            
verificarturno()
