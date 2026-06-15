#funciones
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
    

#codigo principal

#declaro la lista de mascotas
lista_mascotas = []
op = 0
while op != 6:
    mostrar_menu()
    op = ingresar_opcion()
