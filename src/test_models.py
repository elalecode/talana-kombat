import unittest
from src.models import Character

class TestCharacter(unittest.TestCase):

    player1 = Character(
        ["D","DSD","S","DSD","SD"],
        ["K","P","","K","P"],
        "Tonyn",
        "DSDP",
        3,
        "SDK",
        2
    )
    player2 = Character(
        ["SA","SA","SA","ASA","SA"],
        ["K","","K","P","P"],
        "Arnaldor",
        "ASAP",
        2,
        "SAK",
        3
    )

    def test_get_action(self):
        self.assertEqual(self.player1.get_action(1), "DSDP")
        self.assertEqual(self.player2.get_action(4), "SAP")

    def test_get_action_without_punch(self):
        self.assertEqual(self.player1.get_action(2), "S")
        self.assertEqual(self.player2.get_action(1), "SA")

    def test_get_action_empty_and_out_range(self):
        self.assertEqual(self.player1.get_action(5), "")
        self.assertEqual(self.player2.get_action(5), "")

    def test_find_combo_taladoken(self):
        attack_player1 = "AADSDP"
        attack_player2 = "WASAP"
        self.assertEqual(self.player1.find_combo(attack_player1, self.player2), ["AA", "usa un Taladoken"])
        self.assertEqual(self.player2.find_combo(attack_player2, self.player1), ["W", "usa un Taladoken"])

    def test_find_combo_remuyuken(self):
        attack_player1 = "AADSDK"
        attack_player2 = "WASAK"
        self.assertEqual(self.player1.find_combo(attack_player1, self.player2), ["AAD", "conecta un Remuyuken"])
        self.assertEqual(self.player2.find_combo(attack_player2, self.player1), ["WA", "conecta un Remuyuken"])


if __name__ == "__main__":
    unittest.main()
