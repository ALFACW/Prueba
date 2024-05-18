def sueldo_bruto(valorHora, sueldoBase, horasExtras, fonasa, afp):
    valorHoraExtras = valorHora * 1.5
    sueldoBruto = sueldoBase + (horasExtras * valorHoraExtras)
    descuentoFonasa = sueldoBruto * fonasa
    descuentoAFP = sueldoBruto * afp
    sueldoLiquido = sueldoBruto - descuentoFonasa - descuentoAFP
    
    sueldoLiquido = round(sueldoLiquido)
    descuentoFonasa = round(descuentoFonasa)
    descuentoAFP = round(descuentoAFP)
    
    return sueldoLiquido, descuentoFonasa, descuentoAFP,sueldoBruto

valorHora = 3500
afp = 0.07
fonasa = 0.1

while True:
    nombreTrabajador = input("Ingrese el nombre del trabajador: ")
    if not nombreTrabajador:
        print("Debe ingresar un nombre")
    elif len(nombreTrabajador) > 30:
        print("El nombre debe tener como máximo 30 caracteres")
    else:
        break

while True:
        horas = int(input("Ingrese el total de horas trabajadas: "))
        if horas < 0:
            print("El número de horas trabajadas debe ser positivo")
        else:
            horasExtras = max(0, horas - 180)
            break
        print("Por favor, ingrese un número válido de horas")

while True:
        sueldoBase = int(input("Ingrese el sueldo base del trabajador: "))
        if sueldoBase < 0:
            print("El sueldo base no puede ser negativo")
        else:
            break
        print("Por favor, ingrese un sueldo base válido")

sueldoLiquido, descuentoFonasa, descuentoAFP, sueldoBruto = sueldo_bruto(valorHora, sueldoBase, horasExtras, fonasa, afp)

print("\nLiquidaciones")
print("Nombre del Trabajador:", nombreTrabajador)
print("Sueldo Base: $", sueldoBase)
print("Horas Totales Trabajadas:", horas)
print("Horas Extras Trabajadas:", horasExtras)
print("Sueldo Bruto: $", sueldoBruto)
print("Descuento Fonasa: $", descuentoFonasa)
print("Descuento AFP: $", descuentoAFP)
print("Total a pagar: $", sueldoLiquido)

with open(f"liquidacion_{nombreTrabajador}.txt", "w") as archivo:
    archivo.write("Liquidaciones de Sueldo:\n")
    archivo.write(f"Nombre del Trabajador: {nombreTrabajador}\n")
    archivo.write(f"Sueldo Base: $ {sueldoBase}\n")
    archivo.write(f"Horas Totales Trabajadas: {horas}\n")
    archivo.write(f"Horas Extras Trabajadas: {horasExtras}\n")
    archivo.write(f"Sueldo Bruto: $ {sueldoBruto}")
    archivo.write(f"Descuento Fonasa: $ {descuentoFonasa}\n")
    archivo.write(f"Descuento AFP: $ {descuentoAFP}\n")
    archivo.write(f"Total a pagar: $ {sueldoLiquido}\n")
  