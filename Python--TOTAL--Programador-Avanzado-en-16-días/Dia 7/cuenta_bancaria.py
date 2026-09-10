class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance=0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return (
            f"Cliente: {self.nombre} {self.apellido}\n"
            f"Número de cuenta: {self.numero_cuenta}\n"
            f"Balance: ${self.balance}"
        )

    def depositar(self, monto):
        self.balance += monto

    def retirar(self, monto):
        if monto <= self.balance:
            self.balance -= monto
        else:
            print("Error: fondos insuficientes.")


contador_cuenta = 100000


def crear_cliente():
    global contador_cuenta
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    numero_cuenta = contador_cuenta
    contador_cuenta += 1
    return Cliente(nombre, apellido, numero_cuenta, 0)


def inicio():
    cliente = crear_cliente()

    while True:
        print("\n" + str(cliente))
        print("\n¿Qué desea hacer?")
        print("1. Depositar")
        print("2. Retirar")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            monto = float(input("Ingrese el monto a depositar: "))
            cliente.depositar(monto)
        elif opcion == "2":
            monto = float(input("Ingrese el monto a retirar: "))
            cliente.retirar(monto)
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")

        print(f"Balance actualizado: ${cliente.balance}")


inicio()