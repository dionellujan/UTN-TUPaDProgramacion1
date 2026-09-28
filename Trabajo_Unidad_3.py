# ========== EJERCICIO NUMERO 1 ==========
print("========== EJERCICIO NUMERO 1 ==========")

nombre = input("Ingrese el nombre del cliente: ")

while nombre == "" or not nombre.isalpha():
    print("Error. Ingrese un nombre valido.")
    nombre = input("Ingrese el nombre del cliente: ")


cantidad_str = input("Ingrese la cantidad de productos: ")

while not cantidad_str.isdigit() or int(cantidad_str) <= 0:
    print("Error. Ingrese una cantidad mayor a 0.")
    cantidad_str = input("Ingrese la cantidad de productos: ")

cantidad = int(cantidad_str)


total_sin_descuentos = 0
total_con_descuentos = 0
ahorro_total = 0


for i in range(cantidad):

    precio_str = input("Producto " + str(i + 1) + " - Precio: ")

    while not precio_str.isdigit():
        print("Error. Ingrese un precio valido.")
        precio_str = input("Producto " + str(i + 1) + " - Precio: ")

    precio = int(precio_str)


    descuento = input("Descuento (S/N): ").lower()

    while descuento != "s" and descuento != "n":
        print("Error. Ingrese S o N.")
        descuento = input("Descuento (S/N): ").lower()


    total_sin_descuentos = total_sin_descuentos + precio

    if descuento == "s":
        descuento_aplicado = precio * 0.10
        precio_final = precio - descuento_aplicado

        total_con_descuentos = total_con_descuentos + precio_final
        ahorro_total = ahorro_total + descuento_aplicado

    else:
        total_con_descuentos = total_con_descuentos + precio


promedio = total_con_descuentos / cantidad


print()
print("Cliente:", nombre)
print("Total sin descuentos: $", total_sin_descuentos)
print(f"Total con descuentos: ${total_con_descuentos:.2f}")
print(f"Ahorro: ${ahorro_total:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")

cantidad = int(cantidad_str)

# ========== EJERCICIO NUMERO 2 ==========
print("========== EJERCICIO NUMERO 2 ==========")

usuario_correcto = "alumno"
clave_correcta = "python123"

intentos = 0
acceso = False

while intentos < 3:
    print("Intento", intentos + 1, "/3")

    usuario = input("Usuario: ")
    clave = input("Clave: ")

    if usuario == usuario_correcto and clave == clave_correcta:
        print("Acceso concedido.")
        acceso = True
        break
    else:
        print("Error: credenciales invalidas.")

    intentos = intentos + 1


if acceso == False:
    print("Cuenta bloqueada.")

else:
    opcion = ""

    while opcion != "4":

        print()
        print("1) Estado")
        print("2) Cambiar clave")
        print("3) Mensaje")
        print("4) Salir")

        opcion = input("Opcion: ")

        while not opcion.isdigit():
            print("Error: ingrese un numero valido.")
            opcion = input("Opcion: ")

        if int(opcion) < 1 or int(opcion) > 4:
            print("Error: opcion fuera de rango.")

        elif opcion == "1":
            print("Inscripto")

        elif opcion == "2":
            nueva_clave = input("Nueva clave: ")

            while len(nueva_clave) < 6:
                print("Error: minimo 6 caracteres.")
                nueva_clave = input("Nueva clave: ")

            confirmacion = input("Confirme la nueva clave: ")

            while nueva_clave != confirmacion:
                print("Error: las claves no coinciden.")
                confirmacion = input("Confirme la nueva clave: ")

            clave_correcta = nueva_clave
            print("Clave cambiada correctamente.")

        elif opcion == "3":
            print("Segui adelante, cada paso te acerca a tu objetivo.")

        elif opcion == "4":
            print("Sesion finalizada.")

# ========== EJERCICIO NUMERO 3 ==========
print("========== EJERCICIO NUMERO 3 ==========")

operador = input("Ingrese el nombre del operador: ")

while operador == "" or not operador.isalpha():
    print("Error. Ingrese un nombre valido.")
    operador = input("Ingrese el nombre del operador: ")


lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

opcion = ""

while opcion != "5":

    print()
    print("1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del dia")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")

    opcion = input("Opcion: ")

    while not opcion.isdigit():
        print("Error. Ingrese un numero valido.")
        opcion = input("Opcion: ")

    if int(opcion) < 1 or int(opcion) > 5:
        print("Error. Opcion fuera de rango.")

    elif opcion == "1":

        print()
        print("1. Lunes")
        print("2. Martes")

        dia = input("Elija el dia: ")

        while not dia.isdigit():
            print("Error. Ingrese un numero valido.")
            dia = input("Elija el dia: ")

        while int(dia) < 1 or int(dia) > 2:
            print("Error. Elija 1 para Lunes o 2 para Martes.")
            dia = input("Elija el dia: ")

        paciente = input("Ingrese el nombre del paciente: ")

        while paciente == "" or not paciente.isalpha():
            print("Error. Ingrese un nombre valido.")
            paciente = input("Ingrese el nombre del paciente: ")


        if dia == "1":

            if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                print("Error. El paciente ya tiene un turno ese dia.")

            elif lunes1 == "":
                lunes1 = paciente
                print("Turno reservado correctamente.")

            elif lunes2 == "":
                lunes2 = paciente
                print("Turno reservado correctamente.")

            elif lunes3 == "":
                lunes3 = paciente
                print("Turno reservado correctamente.")

            elif lunes4 == "":
                lunes4 = paciente
                print("Turno reservado correctamente.")

            else:
                print("No hay turnos disponibles para el Lunes.")


        elif dia == "2":

            if paciente == martes1 or paciente == martes2 or paciente == martes3:
                print("Error. El paciente ya tiene un turno ese dia.")

            elif martes1 == "":
                martes1 = paciente
                print("Turno reservado correctamente.")

            elif martes2 == "":
                martes2 = paciente
                print("Turno reservado correctamente.")

            elif martes3 == "":
                martes3 = paciente
                print("Turno reservado correctamente.")

            else:
                print("No hay turnos disponibles para el Martes.")


    elif opcion == "2":

        print()
        print("1. Lunes")
        print("2. Martes")

        dia = input("Elija el dia: ")

        while not dia.isdigit():
            print("Error. Ingrese un numero valido.")
            dia = input("Elija el dia: ")

        while int(dia) < 1 or int(dia) > 2:
            print("Error. Elija 1 para Lunes o 2 para Martes.")
            dia = input("Elija el dia: ")

        paciente = input("Ingrese el nombre del paciente: ")

        while paciente == "" or not paciente.isalpha():
            print("Error. Ingrese un nombre valido.")
            paciente = input("Ingrese el nombre del paciente: ")


        if dia == "1":

            if paciente == lunes1:
                lunes1 = ""
                print("Turno cancelado correctamente.")

            elif paciente == lunes2:
                lunes2 = ""
                print("Turno cancelado correctamente.")

            elif paciente == lunes3:
                lunes3 = ""
                print("Turno cancelado correctamente.")

            elif paciente == lunes4:
                lunes4 = ""
                print("Turno cancelado correctamente.")

            else:
                print("No se encontro un turno para ese paciente.")


        elif dia == "2":

            if paciente == martes1:
                martes1 = ""
                print("Turno cancelado correctamente.")

            elif paciente == martes2:
                martes2 = ""
                print("Turno cancelado correctamente.")

            elif paciente == martes3:
                martes3 = ""
                print("Turno cancelado correctamente.")

            else:
                print("No se encontro un turno para ese paciente.")


    elif opcion == "3":

        print()
        print("1. Lunes")
        print("2. Martes")

        dia = input("Elija el dia: ")

        while not dia.isdigit():
            print("Error. Ingrese un numero valido.")
            dia = input("Elija el dia: ")

        while int(dia) < 1 or int(dia) > 2:
            print("Error. Elija 1 para Lunes o 2 para Martes.")
            dia = input("Elija el dia: ")


        if dia == "1":

            print()
            print("Agenda del Lunes:")

            if lunes1 == "":
                print("Turno 1: (libre)")
            else:
                print("Turno 1:", lunes1)

            if lunes2 == "":
                print("Turno 2: (libre)")
            else:
                print("Turno 2:", lunes2)

            if lunes3 == "":
                print("Turno 3: (libre)")
            else:
                print("Turno 3:", lunes3)

            if lunes4 == "":
                print("Turno 4: (libre)")
            else:
                print("Turno 4:", lunes4)


        elif dia == "2":

            print()
            print("Agenda del Martes:")

            if martes1 == "":
                print("Turno 1: (libre)")
            else:
                print("Turno 1:", martes1)

            if martes2 == "":
                print("Turno 2: (libre)")
            else:
                print("Turno 2:", martes2)

            if martes3 == "":
                print("Turno 3: (libre)")
            else:
                print("Turno 3:", martes3)


    elif opcion == "4":

        lunes_ocupados = 0

        if lunes1 != "":
            lunes_ocupados = lunes_ocupados + 1

        if lunes2 != "":
            lunes_ocupados = lunes_ocupados + 1

        if lunes3 != "":
            lunes_ocupados = lunes_ocupados + 1

        if lunes4 != "":
            lunes_ocupados = lunes_ocupados + 1


        martes_ocupados = 0

        if martes1 != "":
            martes_ocupados = martes_ocupados + 1

        if martes2 != "":
            martes_ocupados = martes_ocupados + 1

        if martes3 != "":
            martes_ocupados = martes_ocupados + 1


        lunes_disponibles = 4 - lunes_ocupados
        martes_disponibles = 3 - martes_ocupados


        print()
        print("Resumen general:")
        print("Lunes - Ocupados:", lunes_ocupados)
        print("Lunes - Disponibles:", lunes_disponibles)
        print("Martes - Ocupados:", martes_ocupados)
        print("Martes - Disponibles:", martes_disponibles)


        if lunes_ocupados > martes_ocupados:
            print("Dia con mas turnos: Lunes")

        elif martes_ocupados > lunes_ocupados:
            print("Dia con mas turnos: Martes")

        else:
            print("Hay un empate entre Lunes y Martes.")


    elif opcion == "5":
        print("Sistema cerrado.")

print("Hasta luego,", operador)

# ========== EJERCICIO NUMERO 4 ==========
print("========== EJERCICIO NUMERO 4 ==========")   

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzar_seguidas = 0

nombre = input("Ingrese el nombre del agente: ")

while nombre == "" or not nombre.isalpha():
    print("Error. Ingrese un nombre valido.")
    nombre = input("Ingrese el nombre del agente: ")

print()
print("Bienvenido, agente", nombre)
print("Debes abrir las 3 cerraduras antes de quedarte sin energia o tiempo.")


opcion = ""

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and alarma == False:

    print()
    print("================================")
    print("Energia:", energia)
    print("Tiempo:", tiempo)
    print("Cerraduras abiertas:", cerraduras_abiertas, "/ 3")
    print("Codigo parcial:", codigo_parcial)
    print("================================")

    print("1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")

    opcion = input("Elija una opcion: ")

    while not opcion.isdigit():
        print("Error. Ingrese un numero valido.")
        opcion = input("Elija una opcion: ")

    while int(opcion) < 1 or int(opcion) > 3:
        print("Error. La opcion debe estar entre 1 y 3.")
        opcion = input("Elija una opcion: ")

        while not opcion.isdigit():
            print("Error. Ingrese un numero valido.")
            opcion = input("Elija una opcion: ")


    # OPCION 1: FORZAR CERRADURA
    if opcion == "1":

        energia = energia - 20
        tiempo = tiempo - 2
        forzar_seguidas = forzar_seguidas + 1

        print("Intentas forzar la cerradura...")

        if forzar_seguidas == 3:

            print("La cerradura se trabo.")
            print("ALARMA ACTIVADA.")

            alarma = True

        else:

            if energia < 40:

                print("La energia esta por debajo de 40.")
                print("Riesgo de alarma.")

                numero = input("Ingrese un numero del 1 al 3: ")

                while not numero.isdigit():
                    print("Error. Ingrese un numero valido.")
                    numero = input("Ingrese un numero del 1 al 3: ")

                while int(numero) < 1 or int(numero) > 3:
                    print("Error. El numero debe estar entre 1 y 3.")
                    numero = input("Ingrese un numero del 1 al 3: ")

                    while not numero.isdigit():
                        print("Error. Ingrese un numero valido.")
                        numero = input("Ingrese un numero del 1 al 3: ")

                if numero == "3":
                    alarma = True
                    print("ALARMA ACTIVADA.")

                else:
                    cerraduras_abiertas = cerraduras_abiertas + 1
                    print("Cerradura abierta.")

            else:
                cerraduras_abiertas = cerraduras_abiertas + 1
                print("Cerradura abierta.")


    # OPCION 2: HACKEAR PANEL
    elif opcion == "2":

        energia = energia - 10
        tiempo = tiempo - 3

        forzar_seguidas = 0

        print("Iniciando hackeo...")

        for i in range(4):
            codigo_parcial = codigo_parcial + "A"
            print("Paso", i + 1, "/ 4")
            print("Codigo parcial:", codigo_parcial)

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:

            cerraduras_abiertas = cerraduras_abiertas + 1
            print("El hackeo abrio una cerradura.")

        else:
            print("El hackeo no fue suficiente para abrir una cerradura.")


    # OPCION 3: DESCANSAR
    elif opcion == "3":

        forzar_seguidas = 0

        energia = energia + 15

        if energia > 100:
            energia = 100

        tiempo = tiempo - 1

        if alarma == True:
            energia = energia - 10
            print("La alarma esta activa. Perdes 10 de energia extra.")

        print("Descansaste.")
        print("Energia actual:", energia)


    # BLOQUEO POR ALARMA
    if alarma == True and tiempo <= 3 and cerraduras_abiertas < 3:
        print()
        print("================================")
        print("BLOQUEO DE SEGURIDAD")
        print("La alarma se activo con poco tiempo restante.")
        print("La boveda queda bloqueada.")
        print("DERROTA")
        print("================================")


# CONDICIONES FINALES

if cerraduras_abiertas == 3:
    print()
    print("================================")
    print("VICTORIA")
    print("Abriste las 3 cerraduras.")
    print("La boveda fue abierta.")
    print("================================")

elif alarma == True:
    if not (tiempo <= 3 and cerraduras_abiertas < 3):
        print()
        print("================================")
        print("DERROTA")
        print("La alarma fue activada.")
        print("================================")

elif energia <= 0 or tiempo <= 0:
    print()
    print("================================")
    print("DERROTA")
    print("Te quedaste sin energia o sin tiempo.")
    print("================================")

# ========== EJERCICIO NUMERO 5 ==========
print("========== EJERCICIO NUMERO 5 ==========")

print("--- BIENVENIDO A LA ARENA ---")

nombre = input("Nombre del Gladiador: ")

while nombre == "" or not nombre.isalpha():
    print("Error: Solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ")


vida_jugador = 100
vida_enemigo = 100
pociones = 3
ataque_pesado = 15
daño_enemigo = 12
turno_jugador = True


print()
print("=== INICIO DEL COMBATE ===")


while vida_jugador > 0 and vida_enemigo > 0:

    if turno_jugador == True:

        print()
        print(nombre, "(HP:", vida_jugador, ") vs Enemigo (HP:", vida_enemigo, ") | Pociones:", pociones)

        print("Elige accion:")
        print("1. Ataque Pesado")
        print("2. Rafaga Veloz")
        print("3. Curar")

        opcion = input("Opcion: ")

        while not opcion.isdigit():
            print("Error: Ingrese un numero valido.")
            opcion = input("Opcion: ")

        while int(opcion) < 1 or int(opcion) > 3:
            print("Error: La opcion debe ser 1, 2 o 3.")
            opcion = input("Opcion: ")

            while not opcion.isdigit():
                print("Error: Ingrese un numero valido.")
                opcion = input("Opcion: ")


        # ATAQUE PESADO

        if opcion == "1":

            if vida_enemigo < 20:
                daño = ataque_pesado * 1.5
                print("¡Golpe Critico!")
            else:
                daño = float(ataque_pesado)

            vida_enemigo = vida_enemigo - daño

            print("¡Atacaste al enemigo por", daño, "puntos de daño!")


        # RAFAGA VELOZ

        elif opcion == "2":

            print(">> ¡Inicias una rafaga de golpes!")

            for i in range(3):

                vida_enemigo = vida_enemigo - 5

                print("> Golpe conectado por 5 de daño")


        # CURAR

        elif opcion == "3":

            if pociones > 0:

                vida_jugador = vida_jugador + 30
                pociones = pociones - 1

                if vida_jugador > 100:
                    vida_jugador = 100

                print("¡Te curaste 30 puntos de vida!")

            else:

                print("¡No quedan pociones!")


        # CAMBIO DE TURNO

        turno_jugador = False


    # TURNO DEL ENEMIGO

    else:

        if vida_enemigo > 0:

            vida_jugador = vida_jugador - daño_enemigo

            print()
            print(">> ¡El enemigo contraataca por", daño_enemigo, "puntos!")

            if vida_jugador > 0:
                print(nombre, "ahora tiene", vida_jugador, "puntos de vida.")

        turno_jugador = True


# FIN DEL JUEGO

print()

if vida_jugador > 0:
    print("¡VICTORIA!", nombre, "ha ganado la batalla.")

else:
    print("DERROTA. Has caido en combate.")

