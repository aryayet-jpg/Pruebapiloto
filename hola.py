#Esto no te va a andar nunca si no instalas phyton aca, a la izquierda en el lateral vas a ver unos cuadrados. Despues de la Lupa es el tercero
#Instalas la version mas reciente, tranqui lo hace el programa solo. Luego siempre recorda guardar los archivos ".py" ejemplo este archivo es "hola.py"
#Arriba a tu derecha tenes un PLAY. Le das click y te abre la consola
#En caso que no te aparezca el PLAY, tira la PC.. Na mentira. Arriba donde dice RUN haces click y pones el primer item. Start Debbung o algo asi y listo.
#Ok, empecemos..
"""
#Ejercicio 1:
#Para poder comentar en Phyton se utiliza el numeral, en algunos otros programas como JS o Java se utilizan las barras invertidas // .
#Input siempre devuelve un texto
#En este caso, si bien no esta declarado como VAR (Variable) se puede tomar "nombre_Usuario¨ como variable

#Le pedimos al usuario que escriba su nombre o cualquier cosa
nombreUsuario = input("¿Como te llamas? ")
#Tener en cuenta que el programa no te detecta faltas de ortografia
#Mostramos el saludo. "Print" siempre imprime (Muestra) en pantalla o consola , se utiliza para todos los programas
print(f"Hola mhgjhgjhgjhgmh{nombreUsuario}")
"""

#Que carajo es la F azul? Sin esa F no muestra nada, la F detecta lo que esta entre corchetes. Solo para eso
#Juga e intercambia las cosas para probarlo. Ejemplo, esto se utiliza en un programa cuando terminas de inscribirte 
#O algo que te dice "Hola Ariadna, gracias por inscribirte, pronto nos contactaremos" . El mensaje no tiene limites de caracteres

#######################################################################################
#Ejercicio 2
#Suma o resta

"""
#Pedimos el primer número al usuario
VariableA = float(input("Ingresá el primer número: "))
#Que es float ? Float se utiliza para los numeros con comas, enteras y racionales. Aca nos metemos en matematicas. 
#INT en minuscula, es otro atributo que podemos usar, pero este solo detecta numeros enteros. Es decir 2+2 , FLOAT te detecta 2,2+2,4 hace ese tipo de sumas o restas
#Seguimoos..
#Pedimos el segundo número al usuario. Siempre recorda escribir formal. Es lo que ve el cliente, lo que escribas entre # es para vos o para otro programador.
VariableB = float(input("Ingresá el segundo número: "))
#Calculamos la suma
resta = VariableA - VariableB
#Aca te calcula la suma, pero no vas a ver nada. Y aca entra el famoso PRINT otra vez para mostrar al usuario
#Mostramos el resultado
print(f"La suma es {resta}")
"""

#Una vez probado, borra el float y proba con INT en minuscula. Cambia un poco la visual
#Te dejo un "Bonus track de Tronco" gratis , mira esto

"""
try:
    #Pedimos el primer número
    numero1 = float(input("Ingresá el primer número: "))
    #Pedimos el segundo número
    numero2 = float(input("Ingresá el segundo número: "))
    #Calculamos la suma
    suma = numero1 + numero2
    #Mostramos el resultado
    print(f"La suma de {numero1} + {numero2} es {suma}")
except ValueError:
    print("⚠️ Error: Por favor, ingresá solo números.")
"""

#Que vemos aca ? Lo mismo pero con un condicional. Lo vas a ver todo el tiempo esto en programacion, ejemplo en un banco
#Suponete, vas a sacar plata o a transferir. En tu cuenta tenes 400 , queres trasnferir 200 listo, te hace la resta como aprendiste recien
#Pero que pasa si queres trasnferir 500 ? No te va a dejar, entonces aca entra el TRY y el EXCEPT. Donde TRY quiere decir "Primero hacemos esto" 
#Y sino, aparece EXCEPT (Estuve dos horas porque escribi ESPERT como el politico) . Ah eso, no detecta errores esto por ende que si tenes un error directamente
#El programa no se ejecuta pero no te dice donde esta el error. Imaginate que suceda eso con un programa de 500 lineas y solo te falte una coma o un punto.
#Hay que prestar atencion. Por eso los programadores laburan en un ambiente tranquilo sin presion. Bueno volvamos...
#EXCEPT se utiliza para el condicional, osea si pasa esto hace esto otro. En este caso te muestra en pantalla que ingreses solo los numeros
#Escribiendo EXIT salis de la consola

#######################################################################################
#Ejercicio 3
#Sabiendo esto, te dejo el ejercicio numero 3 para vos. Recorda que en programacion es copiar y pegar, pero tambien hay que saber QUE COPIAR Y QUE PEGAR.
#Crea un programa que pida el nombre, el apellido la edad y luego que lo muestre en una pantalla
"""
nombre = input ("Cual es tu nombre:") 
apellido = input ("Cual es tu apellido:")
edad = input ("Cual es tu edad:")
email = input ("Ingrese su email:")
print(f"Hola {nombre} {apellido} {edad}") 
""" 
    

#######################################################################################
#Ejercicio 4. Idem Ejercicio 3
"""
nombre = input ("Cual es tu nombre:")
numeroDeComision = input ("Ingrese su numero de comision:")
asignaturaDocente = input ("Cual es su asignatura docente:")
presentismo = input ("Estuvo presente")
print(f"{nombre}")
print(f"{numeroDeComision}")
print(f"{asignaturaDocente}")
print(F"{presentismo}")
"""

#######################################################################################
#Ejercicio 5, 
#Bien, aca tenemos matematicas pura. Como se calcula la superficie de un cuadrado ? Lado por lado. Es decir, aca tener que crear tu variable "lado"
#Empecemos,
#Algo que no te dije, con a tecla TAB (Arriba de la Mayuscula) te das los espacios que necesitas para programar. Todo en orden y por bloques tiene que estar

""""
#Creamos nuestra "Variable" lado.
#Pedir al usuario el valor del lado
lado = float(input("Ingresá el valor del lado del cuadrado (en metros): "))
# Calcular el área (lado x lado)
superficie = lado * lado
#En la multiplicacion se usa el asterisco. En la division la barra. Ojo con el % te rompe el programa. Me acaba de pasar
#Mostramos el resultado
print(f"La superficie del cuadrado es {superficie} m2")
#Recorda que lo que esta entre comillas con letras rojas lo podes cambiar a tu gusto. Es decir en vez que diga "La superficie del cuadrado es"
#Le podes poner directamente lo que quieras, "tu cuadrado tiene una superficie total de" y asi.
"""

#######################################################################################
#Ejercicio 6. Te lo dejo a vos, dato de la superficie de un Rectangulo no la se. Pero va a tener que ingresar dos numeros. Ejercicio 2 lo hiciste.
"""
base = float(input("Ingresa el valor de la base:"))
altura = float(input("Ingrese el valor de la altura:"))
superficie = base * altura
print(f"La superficie del rectangulo es {superficie}m2")
"""
"""
#######################################################################################
#Ejercicio 7. Dato de la superficie de un triangulo es BASE por ALTURA. Es decir va a tener que ingresar dos numeros. Ejercicio 2 lo hiciste.
base = float(input("Ingresa el valor de la base"))
altura = float(input("Ingresa el valor de la altura"))
superficie = base * altura
print(f"La superficie del rectangulo es {superficie}m2")
"""
#######################################################################################
#Ejercicio 8.
#Esto es mas de lo mismo, teniendo en cuenta que IVA es 21% . Es decir es el 0.21 de una multiplicacion. Es decir, como sacas el IVA ?
#Si un producto vale 500 pesos. El IVA es el 21% de ese producto, multiplicas 500X0,21 y al valor que te da. Se lo sumas a 500. Esto da 605
#En este caso le tenes que mostrar al usuario el valor del IVA , no tenes que sumar nada. Solo mostrar ese valor
#Vamos a hacerlo con el ejemplo de 500 pesos.
"""
producto = input("Ingrese el nombre del producto")
precio = float(input("Ingrese el valor del precio"))
iva = precio * 0.21
precioFinal = precio + iva
print(f"Su precio final es {precioFinal}") 
"""

#Aca yo te imprimi todo. Pero el ejercicio solo pide el IVA . Lo demas es al pedo, pero suma

#######################################################################################
#Ejercico 9
#Tengo que ser profe de programacion yo, que crack dios.
#Empecemos, el principio del ejercicio es todo tal cual veniamos aprendiendo. Tenes que ingresar el nombre de las materias con las notas
#Pero pensa, solo te voy a dar pistas. Es mas facil de lo que pensas
#Tenes que hacer que el usuario ingrese tres numeros. Numero 1, Numero 2 y Numero 3.
#Que calcule el promedio, como se calcula un promedio la suma de las notas. Divido 3.
#Tenes que lograr que el programa Sume los 3 numeros y luego los divida y muestre ese resultado final
#Pensalo, es facil.
"""
nombre = input ("Ingrese el nombre del alumno:")
apellido = input ("Ingrese el apellido del alumno:")
nota1 = float(input("Ingrese la nota de Literatura:"))
nota2 = float(input("Ingrese la nota de Quimica:"))
nota3 = float(input("Ingrese la nota de Historia:"))
promedio = (nota1 + nota2 + nota3) / 3
print("Resultado")
print(f"El alumno {nombre}{apellido}")
print(f"Notas:{nota1}{nota2}{nota3}")
print(f"Su promedio es de {promedio:}")
"""


"""
#Ingresar datos del alumno
nombre = input("Ingrese el nombre del alumno: ")
apellido = input("Ingrese el apellido del alumno: ")

#Ingresar las 3 notas
#Recorda que lo que esta entre comillas se puede cambiar. Ejemplo "Ingrese la nota de Matematicas"
nota1 = float(input("Ingresá la primera nota: "))
nota2 = float(input("Ingresá la segunda nota: "))
nota3 = float(input("Ingresá la tercera nota: "))

#Calcular promedio
promedio = (nota1 + nota2 + nota3) / 3

# Mostrar resultado
print("Resultado")
print(f"Alumno: {nombre} {apellido}")
print(f"Notas: {nota1}, {nota2}, {nota3}")
print(f"Promedio: {promedio:}")
#Tene en cuanta que las variables que vos nombras, como nota1, nombre, apellido . Pueden tener cualquier nombre, ejemplo JARRA
#Esto el usuario no lo ve. Solo lo ves vos. El tema esta que el dia de mañana cuando trabajes en una empresa, vos vas a hacer una parte del programa
#Y otra persona la va a seguir, por eso tiene que estar todo en orden y bien identificado que es cada cosa. Porque te va a pasar que te van a dar un codigo
#Y no vas a entender nada y tenes que decifrar que es cada cosa o que hace cada cosa, resta tiempo y el tiempo para una empresa que es? PLATA.
"""

#######################################################################################
#Ejercicio 10. Todo tuyo ...
#Practica sin miedo, juga y proba todo tipo de cosas. Es muy facil phyton y programar. Solo tenes que seguir una logica y luego reemplazar por los
#Atributos o variables que tengas, cada programa es unico y no existe un codigo exactamente igual. Yo lo puedo programar asi, quiza tu profe lo haga de otra manera
#Y va a andar y esta bien, lo ideal es tener un estilo propio. Te vas a cruzar con gente que es muy desprolija en su codigo, pero anda igual
#El usuario que ve? Que ande y que pueda utilizarlo. Pero para pasar de Junior a SemiSenior y ni hablar de Senior se destaca todo en la simpleza y limpieza
#De tu codigo.
#Un crack soy, lose. Me debes una cerveza Stella.


###########################################################
#Crea un programa que pida al usuario un numero, si coincide con el valor 18, mostrar el mensaje Usted tiene 18 años


#########################################################
#Determinar el tipo de mantenimiento recomendado para un vehiculo:
#Tipo de vehiculo: automovil, motocicleta, camion
#Kilometraje acumulado
#Peso (solo para camiones: liviano, mediano, pesado)

#Si el vehiculo es un automovil:
#Si el km es menor a 10.000km se recomienda mantenimiento basico
#Si el km esta entre 10,000km y 50,000km se recomienda mantenimiento preventivo
#Si supera los 50,000 km se recomienda mantenimiento general

#Si el vehiculo es una motocicleta
#Si el km es menor a 5,000km se recomienda cambio de aceite
#Si esta entre 5000 y 20000 km se recomienda ajuste general
#Si supera los 20000km se recomienda revision completa

#Si el vehiculo es un camion:
#Dependiendo de su peso (liviano, mediano, pesado)
#Liviano: requiere revision cada 15000km
#Mediano: requiere revision cada 10000km
#Pesado: requiere revision cada 5000km
 
#El programa debera mostrar un mensaje especifico si el camion supera los 100000 km indicando que ademas se requiere
#una revision urgente

tipodeVehiculo = input("Ingresa el tipo de vehiculo:")
kilometraje = float(input("Ingresa el kilometraje acumulado"))
if tipodeVehiculo == "auto":
    if kilometraje < 10000:
        print("Mantenimiento basico")
    elif 10000 >= kilometraje <= 50000:
        print("Mantenimiento preventivo")
    else:
        print("Mantenimiento general")

elif tipodeVehiculo == "motocicleta":
    if kilometraje < 5000:
        print("cambio de aceite")
    elif 5000 >= kilometraje <= 20000:
        print("ajuste general")
    else:
        print("revision completa")