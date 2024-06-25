print("****************************************")
print("                 WELCOME")
print("             TO THE PETSHOP")
print("****************************************")

#Declaracion de variables
num_perros = 10
num_gatos = 8
num_pajaros = 25

#Suma de animales
animales_totales = num_pajaros + num_gatos + num_perros

#! Pedir Nombre y Apellido del usuario
print("Por favor ingresa tu nombre")
nombre = input()
print("Por favor escribe tu apellido")
apellido = input()

# * Concatenacion - Unirlos

nombre_completo = nombre + " " + apellido

print("Gracias por visitarnos", nombre_completo)

#Impresion de todo
print("Actualmente contamos con:")
print("Perros:", num_perros, "\nGatos:", num_gatos, "\nPajaros:", num_pajaros)
print("En total tenemos:", animales_totales, "animales")