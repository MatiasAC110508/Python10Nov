"""23. Banco “LoopBank”-- Simulación de intereses
Como analista financiero, quiero una función calcularInteres() que reciba un monto
y una tasa (porcentaje) y retorne el valor final después de aplicar el interés una vez.
El programa principal debe pedir los datos y mostrar el resultado."""

print("--LOOPBANK--\n")

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
            
calcularinteres()