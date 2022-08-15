"""Talana Kombat models."""

import json
from jsonschema import validate


class Character:
    """Character model."""

    MAX_ATTACKS = 5
    moves: list = []
    punches: list = []
    name: str = ""
    taladoken: str
    taladoken_attack: int
    remuyuken: str
    remuyuken_attack: int
    punch: str = "P"
    punch_attack: int = 1
    kick: str = "K"
    kick_attack: int = 1

    def __init__(self, moves: list, punches: list, name: str, taladoken: str, taladoken_attack: int, remuyuken: str , remuyuken_attack: int) -> None:
        self._energy: int = 6
        self.moves = moves
        self.punches = punches
        self.name = name
        self.taladoken = taladoken
        self.taladoken_attack = taladoken_attack
        self.remuyuken = remuyuken
        self.remuyuken_attack = remuyuken_attack

    def get_name(self) -> str:
        return self.name

    def get_energy(self) -> int:
        return self._energy

    def set_energy(self, x) -> None:
        self._energy = x

    def attack(self, round: int, opponent) -> None:
        attack = self.get_action(round)
        moves, combo_str = self.find_combo(attack, opponent)
        moves, hit_str = self.find_hit(moves, opponent)

        moves_str = ""
        if len(moves) > 1:
            moves_str = "se mueve"
        else:
            if moves == "W":
                moves_str = f"{moves_str} salta"
            if moves == "S":
                moves_str = f"{moves_str} se agacha"

            if moves == "A":
                if self.name == "Arnaldor":
                    moves_str = f"{moves_str} retrocede"
                else:
                    moves_str = f"{moves_str} avanza"

            if moves == "D":
                if self.name == "Tonyn":
                    moves_str = f"{moves_str} avanza"
                else:
                    moves_str = f"{moves_str} retrocede"            

        story = f"{self.name}"
        if len(moves_str):
            story = f"{story} {moves_str}"
        if len(hit_str):
            story = f"{story} y {hit_str}"
        if len(combo_str):
            story = f"{story} {combo_str}"
        print(story)

    def find_hit(self, moves, opponent) -> list:
        if len(moves):
            if moves[-1] == self.punch:
                return [moves.replace(self.punch, ""), self.hit_with_punch(opponent)]
            if moves[-1] == self.kick:
                return [moves.replace(self.kick, ""), self.hit_with_kick(opponent)]
        return [moves, ""]

    def find_combo(self, attack: str, opponent) -> list:
        if attack.find(self.taladoken) >= 0:
            return [attack.replace(self.taladoken, ""), self.hit_with_taladoken(opponent)]

        elif attack.find(self.remuyuken) >= 0:
            return [attack.replace(self.remuyuken, ""), self.hit_with_remuyuken(opponent)]
        return [attack, ""]

    def count_combos(self) -> int:
        count = 0
        count_combos = 0
        while count < len(self.moves):
            action = self.get_action(count)
            if action.find(self.taladoken) >= 0 or action.find(self.remuyuken) >= 0:
                count_combos += 1
            count += 1
        return count_combos

    def count_moves(self) -> int:
        count = 0
        count_moves = 0
        while count < len(self.moves):
            count_moves += len(self.moves[count])
            count += 1
        return count_moves

    def count_punches(self) -> int:
        count = 0
        count_punches = 0
        while count < len(self.moves):
            count_punches += len(self.punches[count])
            count += 1
        return count_punches

    def get_action(self, index) -> str:
        punch = ""
        moves = ""
        try:
            punch = self.punches[index]
        except:
            pass
        
        try:
            moves = self.moves[index]
        except:
            pass
        return f"{moves}{punch}"

    def hit_with_taladoken(self, opponent) -> str:
        opponent.set_energy(opponent._energy - self.taladoken_attack)
        return "usa un Taladoken"
    
    def hit_with_remuyuken(self, opponent) -> str:
        opponent.set_energy(opponent._energy - self.remuyuken_attack)
        return "conecta un Remuyuken"

    def hit_with_punch(self, opponent) -> str:
        opponent.set_energy(opponent._energy - self.punch_attack)
        return f"le da un puñetazo al pobre {opponent.get_name()}"

    def hit_with_kick(self, opponent) -> str:
        opponent.set_energy(opponent._energy - self.kick_attack)
        return "da una patada"


class Bootstrap:
    rounds: int = 5
    count_rounds: int = 0
    player1: Character
    player2: Character
    fighting = False

    JSON_SCHEMA: dict = {
        "type" : "object",
        "properties" : {
            "player1" : {
                "type" : "object",
                "properties": {
                    "movimientos": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    },
                    "golpes": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    }
                }
            },
            "player2" : {
                "type" : "object",
                "properties": {
                    "movimientos": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    },
                    "golpes": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    }
                }
            },
        },
    }

    def __init__(self):
        data = self.get_params()
        self.player1 = Character(data["player1"]["movimientos"], data["player1"]["golpes"], "Tonyn", "DSDP", 3, "SDK", 2)
        self.player2 = Character(data["player2"]["movimientos"], data["player2"]["golpes"], "Arnaldor", "ASAP", 2, "SAK", 3)

    def who_start(self) -> Character:
        """Search who start."""
        player1_combos = self.player1.count_combos()
        player1_moves = self.player1.count_moves()
        player1_punches = self.player1.count_punches()

        player2_combos = self.player2.count_combos()
        player2_moves = self.player2.count_moves()
        player2_punches = self.player2.count_punches()

        if (player1_combos > player2_combos
            or player1_moves > player2_moves
            or player1_punches > player2_punches):
            return self.player2
        
        return self.player1

    def start_kombat(self):
        self.fighting = True
        first = self.who_start()
        second = self.player1 if first is not self.player1 else self.player2
        players = [first, second]
        count_rounds = 0

        print("----------------TALAN KOMBAT--------------")
        while self.fighting:
            print()
            players[0].attack(count_rounds, players[1])
            if self.verify_winner():
                break
            players[1].attack(count_rounds, players[0])
            if self.verify_winner():
                break
            count_rounds += 1

    def verify_winner(self):
        if self.player1.get_energy() <= 0 or self.player2.get_energy() <= 0:
            if self.player1.get_energy() == self.player2.get_energy():
                print("Empate")
            elif self.player1.get_energy() > self.player2.get_energy():
                print(f"{self.player1.name} Gana la pelea y aun le queda {self.player1.get_energy()} de energía")
            else:
                print(f"{self.player2.name} Gana la pelea y aun le queda {self.player2.get_energy()} de energía")
            return True
        return False

    def get_params(self):
        validated = False
        while not validated:
            print("Ingresa los valores del juego en formato JSON.")
            string = input()
            json_data = json.loads(string)
            try:
                validated = validate(instance=json_data, schema=self.JSON_SCHEMA)
            except:
                print("El formato del JSON no es el correcto, vuelve a intentar.")
            return json_data


