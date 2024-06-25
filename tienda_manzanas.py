#-----------------------------------------------------------------------------------
# !Programa que representa a una tienda de manzanas que interactua con el usuario
#-----------------------------------------------------------------------------------

#* 1.- Mensaje de bienvenida
print("****************************************")
print("                  WELCOME")
print("             TO THE APPLESHOP")
print("****************************************")

#* 2.- Ingresar nombre del usuario
print("Por favor ingrese su nombre")
nombre = input()
print("Por favor ingrese su apellido")
apellido = input()

nombre_completo = nombre + " " + apellido

print("Bienvenido", nombre_completo)
#* 3.- Imprimir mensaje de nuestro stack de manzanas y precio unitario
#? Declaramos las variables para las manzanas (cantidad y precio).
manzanas_disponibles = 20
precio_manzana = 5
print("Tenemos en existencia", manzanas_disponibles, "manzanas a", precio_manzana, "pesos cada una.")
#* 4.- Preguntar cuantas manzanas quiere comprar el usuario
print("¿Cuantas manzanas desea comprar?")
#* 5.- Ingresar el numero de manzanas que el usuario desea
compra = input()
#?Convertimos el valor de compra - Str -> Int
compra = int(compra)

#? Ingresamos una condicional para en caso de que el numero sea mayor a 20 manzanas
#? mande un mensaje de error, lo mismo para el caso de que pida 0 manzanas.

if(compra > 20):
    print("No tenemos la cantidad de manzanas deseadas")
elif(compra == 0):
    # TODO: En caso de que la cantidad sea 0, se da un mensaje de despedida
    print("Muchas gracias por su preferencia, vuelva pronto.")
else:
    #* 6.- Imprimir un mensaje de cuantas manzanas compro y el total de compra
    precio_total = compra * precio_manzana #! Precio total de las manzanas compradas
    print("Su compra fue de", compra, "manzanas, el precio total fue de", precio_total, "pesos")
    #* 7.- Imprimir un mensaje donde nos muestre las manzanas restantes en existencia
    manzanas_disponibles = manzanas_disponibles - compra
    print("Tenemos en existencia", manzanas_disponibles, "manzanas a", precio_manzana, "pesos a cada una.")
    #* 8.- Imprimir mensaje de despedida del usuario
    print("Gracias por su compra, vuelva pronto.")