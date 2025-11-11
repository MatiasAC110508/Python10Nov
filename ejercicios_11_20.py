#11

""" total = 0
for mes in range(1, 7):
    ahorro = int(input(f"Ingrese ahorro del mes {mes}: "))
    total += ahorro
    if total > 1000000:
        print("¡Meta alcanzada!")
print(f"Total acumulado: {total}") """

#12

""" rep = int(input("Ingrese número de repeticiones: "))
for i in range(1, rep + 1):
    print(f"Repetición {i} completada")
    if i % 3 == 0:
        print("¡Excelente ritmo!") """
        
#13

""" vehiculos = 0
while vehiculos < 20:
    vehiculos += 1
    if vehiculos % 2 == 0:
        print("Vehículo par registrado")
    if vehiculos == 20:
        print("Capacidad completa") """

#14

""" total = 0
while True:
    venta = float(input("Ingrese monto de venta (0 para terminar): "))
    if venta == 0:
        break
    if venta > 100000:
        print("Venta destacada")
    total += venta
print(f"Total vendido: {total}") """

#15

""" n = int(input("Ingrese cantidad de ejercicios: "))
for i in range(1, n + 1):
    if i % 5 == 0:
        print(f"Ejercicio {i} completado ¡Gran avance!")
    else:
        print(f"Ejercicio {i} completado") """

#16

""" total = 0
while total < 100:
    venta = int(input("Ingrese litros vendidos: "))
    total += venta
    if total < 100:
        print("Sigue vendiendo")
    else:
        print("Meta diaria alcanzada") """
        
#17

""" for i in range(1, 13):
    print(f"Producción {i}")
    if i == 6:
        print("Mitad de la producción completada")
    if i == 12:
        print("¡Día finalizado!") """
        
#18

""" palabra = input("Ingrese una palabra: ")
for i in range(1, 6):
    if i % 2 == 0:
        print(palabra.upper())
    else:
        print(palabra.lower()) """
        
# 19

""" clientes = 0
while clientes <= 15:
    clientes += 1
    if clientes % 5 == 0:
        print("Pausa para limpieza")
print("Turno finalizado") """

#20

""" intentos = 0
clave = "1234"
while intentos < 3:
    entrada = input("Ingrese contraseña: ")
    if entrada == clave:
        print("Acceso permitido")
        break
    intentos += 1
if intentos == 3:
    print("Acceso denegado") """




