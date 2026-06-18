#funciones
#opcion 2
def buscar_mascota(lista_m, nombre_m):
    for x in range(lista_m):
        if nombre_m == lista_m[x]["nombre"]:
            return x 
    return -1
#validacion
def validar_nombre(name):
    return name.strip() != ""
def validar_especie(especie):
    especies_validas = ["perro", "gato", "ave"]
    return especie.strip().lower() in especies_validas
def validar_edad(edad):
    return edad.isdigit() and int(edad) > 0



def mostrar_menu():
    print("bienvenido al menu")
    print("1. agregar mascota")
    print("2. buscar mascota")
    print("3. eliminar mascota")
    print("4. marcar como vacunado")
    print("5. mostar mascotas")
    print("6. salir")

def ingresar_opcion():
    while True:
        try:
            opcion = int(input("selecione una opcion:"))
            if opcion < 1 or opcion > 6:
                print("debe selecionar una opcion del 1 al 6")
            else:
                break
        except ValueError:
            print("debe ingresar un numero")
    return opcion 
def agregar_mascota(lista):
    nombre = input("ingresar el nombre de la mascota")
    correcto = validar_nombre(nombre)
    if not correcto:
        print("el nombre puede estar vacio")
        return
    especie = input("ingrese la especie de la mascota")
    correcto = validar_especie(especie)
    if not correcto:
        print("la especie solo puede ser perro,gato,ave")
        return

    edad = input("ingrese la edad de la mascota")
    correcto = validar_edad(edad)
    if not correcto:
        print("la edad debe ser un numero entero o mayor a cero")
        return
    
    mascota = {
        "nombre": nombre.strip(),
        "especie": especie.strip(),
        "edad": int(edad),
        "vacunada": False
    } 
#opcion4
def actualizar_vacunas(lista_m):
    for m in lista_m:
        if m["edad"] >= 1:
            m["vacunada"] = True
        else:
            m["vacunada"] = False
            
#codigo principal

#declaro la lista de mascotas
lista_mascotas = []
op = 0
while op != 6:
    mostrar_menu()
    op = ingresar_opcion()

    if op == 1:
        agregar_mascota(lista_mascotas)
    elif op == 2:
        print("buscar mascota")
        nombre = input("ingrese el nombre de la mascota")
        posicion = buscar_mascota(lista_mascotas ,  nombre)
        if posicion != -1:
            print(f"la posicion encotrada es: {posicion + 1} ")
            m = lista_mascotas = {posicion}
            print(f"nombre mascota {m["nombre"]}")
            print(f"especie mascota{m["especie"]}")
            print(f"edad de mascota{m["edad"]}")
            print(f"vacunada{m["vacunada"]}")
        else:
            print("la mascota nose a encontrado")
    elif op == 3:
        print("eliminar mascota")
        nombre = input("ingrese el nombre de la mascota a eliminar ")
        posicion = buscar_mascota(lista_mascotas , nombre)
        if posicion != -1:
            lista_mascotas.pop(posicion)
            print("la mascota ha sido eliminada")
        else:
            print(f"la mascota {nombre} no se encuentra en la lista" )
            
    elif op == 4:
        actualizar_vacunas(lista_mascotas)
        print("vacunas actualizadas")
    elif op == 5:
        actualizar_vacunas(lista_mascotas)
        if len(lista_mascotas) == 0:
            print("no hay mascotas")
        else:
            print("lista de mascotas")
            for m in lista_mascotas:
                print(f"nombre mascota {m["nombre"]}")
                print(f"especie mascota{m["especie"]}")
                print(f"edad de mascota{m["edad"]}")
                print(f"vacunada{m["vacunada"]}")
                estado = "al dia" if m["vacunada"] else "pendiente"
                print(f"estado vacuna {estado}")
                
                
    elif op == 6:
        print("gracias por usar el sistema")
    




