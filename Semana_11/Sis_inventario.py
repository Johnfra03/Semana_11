import json


class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def actualizar_cantidad(self, cantidad):
        self.cantidad = cantidad

    def actualizar_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"


class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar(self, producto):
        self.productos[producto.id] = producto

    def eliminar(self, id):
        if id in self.productos:
            del self.productos[id]

    def actualizar(self, id, cantidad=None, precio=None):
        if id in self.productos:
            if cantidad is not None:
                self.productos[id].actualizar_cantidad(cantidad)
            if precio is not None:
                self.productos[id].actualizar_precio(precio)

    def buscar(self, nombre):
        return [p for p in self.productos.values() if p.nombre.lower() == nombre.lower()]

    def mostrar(self):
        for producto in self.productos.values():
            print(producto)

    def guardar(self, archivo):
        with open(archivo, 'w') as f:
            json.dump({id: vars(prod) for id, prod in self.productos.items()}, f)

    def cargar(self, archivo):
        try:
            with open(archivo, 'r') as f:
                datos = json.load(f)
                self.productos = {id: Producto(**prod) for id, prod in datos.items()}
        except FileNotFoundError:
            pass


def menu():
    inventario = Inventario()
    inventario.cargar("inventario.json")

    while True:
        print("\n--- Sistema de Gestión de Inventario ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar inventario")
        print("6. Guardar y salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar(Producto(id, nombre, cantidad, precio))
        elif opcion == "2":
            id = input("ID del producto a eliminar: ")
            inventario.eliminar(id)
        elif opcion == "3":
            id = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar vacío para no cambiar): ")
            precio = input("Nuevo precio (dejar vacío para no cambiar): ")
            inventario.actualizar(id, int(cantidad) if cantidad else None, float(precio) if precio else None)
        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ")
            resultados = inventario.buscar(nombre)
            for res in resultados:
                print(res)
        elif opcion == "5":
            inventario.mostrar()
        elif opcion == "6":
            inventario.guardar("inventario.json")
            print("Inventario guardado. Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    menu()
