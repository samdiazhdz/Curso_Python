print("Bienvenido al conversor de millas a kilometros")

print("Escribe un numero en millas")
millas = input() #? Regresa datos String

print("Tipo de datos de millas", type(millas))

#* Convertimos de String a numero
millas = float(millas)

print("Tipo de datos de millas", type(millas))

# ! 1 milla = 1.609 km
kilometros = millas * 1.609
print("Millas ingresadas:", millas)
print("Kilometros:", kilometros)