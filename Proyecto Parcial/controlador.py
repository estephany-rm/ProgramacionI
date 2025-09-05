from modelo import Entrenador, PokemonAgua, PokemonFuego, PokemonPlanta, Batalla
from vista import Vista
import random

class Controlador:
    def __init__(self):
        self.jugador = Entrenador("Jugador")
        self.maquina = Entrenador("Máquina")
        self.vista = Vista()

    def preparar_equipo(self):
        self.jugador.get_equipo().clear()
        self.maquina.get_equipo().clear()

        # Equipo del jugador
        self.jugador.agregar_pokemon(PokemonFuego("Charmander", 50, 15, 5))
        self.jugador.agregar_pokemon(PokemonPlanta("Bulbasaur", 55, 12, 6))
        self.jugador.agregar_pokemon(PokemonAgua("Squirtle", 52, 13, 7))

        # Equipo de la máquina
        self.maquina.agregar_pokemon(PokemonPlanta("Chikorita", 53, 12, 6))
        self.maquina.agregar_pokemon(PokemonFuego("Cyndaquil", 48, 14, 5))
        self.maquina.agregar_pokemon(PokemonAgua("Totodile", 54, 13, 7))

    def elegir_pokemon(self, entrenador, es_jugador=True):
        vivos = [p for p in entrenador.get_equipo() if p.esta_vivo()]
        if es_jugador:
            entrenador.mostrar_equipo()
            opcion = self.vista.pedir_opcion("Elige tu Pokémon: ", len(vivos))
            pokemon = vivos[opcion]
            self.vista.mostrar_mensaje(f"\nHas elegido a {pokemon.get_nombre()} ({pokemon.get_tipo()})", delay=1)
            return pokemon
        else:
            pokemon = random.choice(vivos)
            self.vista.mostrar_mensaje(f"🤖 La máquina elige a {pokemon.get_nombre()} ({pokemon.get_tipo()})", delay=1)
            return pokemon

    def jugar_partida(self):
        self.preparar_equipo()
        pokemon_jugador = self.elegir_pokemon(self.jugador, True)
        pokemon_maquina = self.elegir_pokemon(self.maquina, False)

        batalla = Batalla(pokemon_jugador, pokemon_maquina, self.vista)
        self.vista.mostrar_mensaje("\n🔥 ¡Comienza la batalla Pokémon! 🔥", delay=1.5)

        while batalla.esta_activa():
            self.vista.mostrar_mensaje("\n--- Nuevo Turno ---", delay=1)
            self.vista.mostrar_mensaje(batalla.turno_jugador(), delay=1.2)
            if not pokemon_maquina.esta_vivo():
                self.vista.mostrar_mensaje("\n🎉 ¡Has ganado la partida!", delay=2)
                return
            self.vista.mostrar_mensaje(batalla.turno_maquina(), delay=1.2)
            if not pokemon_jugador.esta_vivo():
                self.vista.mostrar_mensaje("\n💀 Has perdido la partida...", delay=2)
                return

    def iniciar(self):
        seguir = True
        self.vista.mostrar_mensaje("\n🎮 Bienvenido al simulador Pokémon 🎮", delay=1.5)
        while seguir:
            self.jugar_partida()
            opcion = input("\n¿Quieres jugar otra vez? (si/no): ").lower()
            if opcion != "si":
                seguir = False
                self.vista.mostrar_mensaje("\n👋 Gracias por jugar. ¡Hasta la próxima!", delay=1.5)

