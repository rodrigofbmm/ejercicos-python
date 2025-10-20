from abc import ABC, abstractmethod

class Animal(ABC):
    def Animal(self, nombre: str):
        self.nombre = nombre

    @abstractmethod
    def hacer_sonido(self) -> str:
        pass


class Perro(Animal):
    def hacer_sonido(self) -> str:
        return " perro Guau"


class Gato(Animal):
    def hacer_sonido(self) -> str:
        return "gato Miau"


class Veterinario:
    def Veterinario(self, nombre: str, registro: str):
        self.nombre = nombre
        self.registro = registro

    def atender(self, animal: Animal) -> str:
        return f"El veterinario {self.nombre} atendió a {animal.nombre} ({animal.sonido()})"
