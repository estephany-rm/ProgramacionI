from abc import ABC, abstractmethod
import random
from vista import Vista

class Pokemon(ABC):
    def __init__(self, nombre: str, tipo: str, vida: int, ataque: int, defensa: int):
        self.__nombre = nombre
        self.__tipo = tipo
        self.__vida = vida
        self.__vida_max = vida
        self.__ataque = ataque
        self.__defensa = defensa

    def get_nombre(self):
        return self.__nombre

    def get_tipo(self):
        return self.__tipo

    def get_vida(self):
        return self.__vida

    def get_vida_max(self):
        return self.__vida_max

    def set_vida(self, newVida):
        self.__vida = max(0, newVida)

    def get_ataque(self):
        return self.__ataque

    def get_defensa(self):
        return self.__defensa

    def esta_vivo(self):
        return self.__vida > 0

    def mostrar_vida(self, largo: int = 20):
        vida_actual = self.get_vida()
        vida_max = self.get_vida_max()
        proporcion = vida_actual / vida_max if vida_max > 0 else 0
        barras = int(proporcion * largo)
        return f"[{'█'*barras}{' '*(largo-barras)}] {vida_actual}/{vida_max} HP"

    @abstractmethod
    def atacar(self, enemigo, movimiento):
        pass


class Movimiento:
    def __init__(self, nombre: str, tipo: str, poder: int):
        self.__nombre = nombre
        self.__tipo = tipo
        self.__poder = poder

    def get_nombre(self):
        return self.__nombre

    def get_tipo(self):
        return self.__tipo

    def get_poder(self):
        return self.__poder


class PokemonFuego(Pokemon):
    def __init__(self, nombre: str, vida: int, ataque: int, defensa: int):
        super().__init__(nombre, "Fuego", vida, ataque, defensa)
        self.movimientos = [
            Movimiento("Llamarada", "Fuego", 40),
            Movimiento("Arañazo", "Normal", 20)
        ]

    def atacar(self, enemigo, movimiento):
        base = movimiento.get_poder() + self.get_ataque() - enemigo.get_defensa()
        if movimiento.get_tipo() == "Fuego" and enemigo.get_tipo() == "Planta":
            base *= 2
        elif movimiento.get_tipo() == "Fuego" and enemigo.get_tipo() == "Agua":
            base *= 0.5
        enemigo.set_vida(enemigo.get_vida() - max(1, int(base)))
        return f"{self.get_nombre()} usa {movimiento.get_nombre()} contra {enemigo.get_nombre()}"


class PokemonAgua(Pokemon):
    def __init__(self, nombre: str, vida: int, ataque: int, defensa: int):
        super().__init__(nombre, "Agua", vida, ataque, defensa)
        self.movimientos = [
            Movimiento("Pistola Agua", "Agua", 35),
            Movimiento("Placaje", "Normal", 20)
        ]

    def atacar(self, enemigo, movimiento):
        base = movimiento.get_poder() + self.get_ataque() - enemigo.get_defensa()
        if movimiento.get_tipo() == "Agua" and enemigo.get_tipo() == "Fuego":
            base *= 2
        elif movimiento.get_tipo() == "Agua" and enemigo.get_tipo() == "Planta":
            base *= 0.5
        enemigo.set_vida(enemigo.get_vida() - max(1, int(base)))
        return f"{self.get_nombre()} usa {movimiento.get_nombre()} contra {enemigo.get_nombre()}"


class PokemonPlanta(Pokemon):
    def __init__(self, nombre: str, vida: int, ataque: int, defensa: int):
        super().__init__(nombre, "Planta", vida, ataque, defensa)
        self.movimientos = [
            Movimiento("Látigo Cepa", "Planta", 35),
            Movimiento("Placaje", "Normal", 20)
        ]

    def atacar(self, enemigo, movimiento):
        base = movimiento.get_poder() + self.get_ataque() - enemigo.get_defensa()
        if movimiento.get_tipo() == "Planta" and enemigo.get_tipo() == "Agua":
            base *= 2
        elif movimiento.get_tipo() == "Planta" and enemigo.get_tipo() == "Fuego":
            base *= 0.5
        enemigo.set_vida(enemigo.get_vida() - max(1, int(base)))
        return f"{self.get_nombre()} usa {movimiento.get_nombre()} contra {enemigo.get_nombre()}"


class Batalla:
    def __init__(self, jugador, maquina,vista):
        self._jugador = jugador
        self._maquina = maquina
        self._vista = vista

    def turno_jugador(self):
        print(f"\n{self._jugador.get_nombre()}: {self._jugador.mostrar_vida()}")
        print(f"{self._maquina.get_nombre()}: {self._maquina.mostrar_vida()}")

        print("\nElige un movimiento:")
        for i, mov in enumerate(self._jugador.movimientos, 1):
            print(f"{i}. {mov.get_nombre()} ({mov.get_tipo()}, Poder: {mov.get_poder()})")
        
        eleccion = self._vista.pedir_opcion("\nMovimiento: ", len(self._jugador.movimientos))
        movimiento = self._jugador.movimientos[eleccion]
        return self._jugador.atacar(self._maquina, movimiento)

    def turno_maquina(self):
        print(f"\n{self._jugador.get_nombre()}: {self._jugador.mostrar_vida()}")
        print(f"{self._maquina.get_nombre()}: {self._maquina.mostrar_vida()}")
        movimiento = random.choice(self._maquina.movimientos)
        return self._maquina.atacar(self._jugador, movimiento)

    def esta_activa(self):
        return self._jugador.esta_vivo() and self._maquina.esta_vivo()

    def get_ganador(self):
        if self._jugador.esta_vivo():
            return self._jugador
        elif self._maquina.esta_vivo():
            return self._maquina
        return None


class Entrenador:
    def __init__(self, nombre: str):
        self.__nombre = nombre
        self.__equipo = []

    def get_nombre(self):
        return self.__nombre

    def get_equipo(self):
        return self.__equipo

    def agregar_pokemon(self, pokemon):
        self.__equipo.append(pokemon)

    def mostrar_equipo(self):
        print(f"\n{self.get_nombre()}, estos son tus Pokémon disponibles:")
        vivos = [p for p in self.__equipo if p.esta_vivo()]
        for i, poke in enumerate(vivos, 1):
            print(f"{i}. {poke.get_nombre()} ({poke.get_tipo()}) - {poke.mostrar_vida()}")

    def elegir_pokemon(self, indice: int):
        vivos = [p for p in self.__equipo if p.esta_vivo()]
        if 0 <= indice < len(vivos):
            return vivos[indice]
        return None

    def tiene_pokemon_vivos(self):
        return any(p.esta_vivo() for p in self.__equipo)

