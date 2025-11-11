"""22. Gimnasio “StrongFit” -- Cálculo de energía
Como entrenador, quiero una función calcularEnergia() que reciba un número de repeticiones y devuelva un mensaje:

    Si las repeticiones son menores de 5 → “Necesitas más esfuerzo”.
    Si son 5 o más → “¡Buen trabajo!”."""
    
print("--STRONGFIT--\n")

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
            
calcularenergia()