
#  Este es un comentario y estes no se ejecutan.
# if True:
#     print("Hola mundo")
#     # End: sintaxis

# Start:
# Variables
# x = 10  # Guarda el numero entero 10 en la variable x
# tasa_interes = 3.14
# usuario_actual = "Ana"
# usuario_activo = True

# Constantes
# MAX_INTENTOS_JUGADOR = 3 #ESTE VALOR NO DEBE CAMBIAR NUNCA




# PRINT (STDOUT)
# nombre = "Ana"
# otro_nombre= "Pedro"
# print("!Hola, " + nombre + "!" ) #Imprime : !Hola Ana
# print("!Hola, " ,  nombre + "!" ) #Imprime : !Hola Ana
# print(f"!Hola, " + {nombre}  y {otro_nombre} "!" ) #Imprime : !Hola Ana y pedro




# Tipos de datos basivos
# int: numeros enteros (-2,0,5)
# float: numeros decimales (3.14, -0.5)
# str: texto entre comillas ("Hola", 'Hola')
# bool: verdadero o falso (True, False)

# print(type(x))
# print(type(tasa_interes))
# print(type(usuario_actual))
# print(type(usuario_activo))

# Tipo dinámico
# numero = 10  #Python infiere que 'numero' es un entero.
# print(type(numero))
# nombre = "Jose"  # Aqui tienes que 'nombre' es una cadema.
# print(type(nombre))

#declaracion y asignacion de variables
# mensaje = ""
# End: Variables, constantes y tipos de datos

# Start: Operadores aritméticos
# Operadores aritmeticos
# a = 10
# b = 3
# print(a + b) # Suma 13
# print(a - b) # resta 7
# print(a * b) # multiplicacion 30
# print(a / b) # division 3.3333...
# print(a //b) # Division entera  3
# print(a % b) # Modulo (resto de la division )  1
# print(a ++ b) # Potencia  1000 (10**3)

# Operadores de comparación
# x = 5
# y = 10
# print(x == y) # ¿Son iguales?  False
# print(x != y) # ¿Son diferentes?  True
# print(x > y) # ¿x es mayor que y ? False
# print(x < y) # ¿x es menor que y ? True
# print(x >= y) # ¿x es mayor o igual que y? False
# print(x <= y) # ¿x es menor o igual que y? True

# Operadores Lógicos
# edad = 20
# es_estudiante = True
# print((edad > 18) and es_estudiante ) #True (Ambas condiciones son cierta)
# print((edad > 18) and not es_estudiante ) #True (Ambas condiciones son cierta)
# print((edad < 18) or es_estudiante) # True (Al menos una es cierta)
# print((edad < 18) or not es_estudiante) # True (Al menos una es cierta)
# print(not es_estudiante) # False ( invierte el valor)

# Operadores de asignación
# x = 10 # Asignación simple
# print(x)
# x += 5 # Suma y asigna (x = x + 5)
# print(x)
# x -= 3 # Resta y asigna (x = - 3)
# print(x)
# x *= 2 # Multiplica y asigna (x = x * 2)
# print(x)
# x /= 4 # Divide y asigna (x = x / 4)

#Otros ejemplos :
# a,b, c = 5, 10, 15 #Asignación múltiple (asigna 5 a 'a', 10 a 'b' y 15 a 'c' ).
# print (a ,b ,c)
# p= q= r= 0 #Asignación del mismo valor a multiples variables (asigna 0 a 'p', 'q' y 'r').
# print(p, q, r)
# # Start: Intercambio directo
# x, y = 10, 20
# print(x, y)
# x, y = y, x
# print(x, y)
# #End: Intercambio directo

# Start: Input (stdin)

# nombre = input("Cuál es tu nombre? ")
# print("Hola,", nombre + "!")

# dato_1= float(input("Dame el dato 1: "))
# dato_2= float(input("Dame el dato 2: "))
# print(f"La suma de los dos numeros es: {dato_1 + dato_2}")
# End: Input

#Star: Conversion de tipos de datos básicos
# a = 5 #int
# b = 2.0 #Float
# c = a + b #Float
# print(type(a), type(b), type(c))
## Conversion explicita
# Conversion a entero
# num_str= "20"
# print(type(num_str))

# num_int= int(num_str)  # num_int será 20
# print(type(num_int))

# # Conversión a cadena
# num = 10
# print(type(num))
# num_float= float(num)   # num_float sera 10.0
# print(type(num_float))

# int()
# float()
# str()
# print(bool(0))

#End: Conversion de tipos de datos básicos

# End operadores aritméticos