class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.next = None

    def agregar(self, valor):
        if self.next:
            self.next.agregar(valor)
        else:
            self.next = Nodo(valor)

    def listar(self):
        if self.next:
            seguiente = self.next.listar()
        else:
            return self.valor

        return f"{self.valor} {seguiente}"


lista = Nodo(5)

lista.agregar(3)
lista.agregar(4)
lista.agregar(8)
lista.agregar(2)

res = lista.listar()

print(res)