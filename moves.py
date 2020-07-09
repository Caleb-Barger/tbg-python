class Move:
    def __init__(self, name, atk, desc, lv_learned=0):
        self.name = name
        self.atk = atk
        self.desc = desc
        self.lv_learned = lv_learned

    def __str__(self):
        return f"{self.name}, Atk - {self.atk}, Desc - {self.desc}"

MAGE = "mage"
ROUGE = "rouge"
KNIGHT = "knight"
INITAL_MOVES = "inital_moves"
LEARNED_MOVES = "learned_moves"

# Move Params (Name, Dmg, Desc)

MAGE_INITAL_MOVES = [
    Move("Do a Funky Jig", 4, "Wow"),
    Move("Fireball", 5, "Wooosh"),
    Move("Summon Snake", 2, "fzzzz")
]

MAGE_LEARNED_MOVES = [
    Move("Mega Kick", 10, "POW", 5),
    Move("Growl", 11, "Grrrr", 8),
    Move("Shadowball", 15, "Death...", 10)
]

ROUGE_INITAL_MOVES = [
    Move("Pile Driver", 5, "Wow"),
    Move("Fireball", 3, "Wooosh"),
    Move("Iceball", 2, "fzzzz")
]

ROUGE_LEARNED_MOVES = [
    Move("Mega Kick", 10, "POW", 5),
    Move("Growl", 11, "Grrrr", 8),
    Move("Shadowball", 15, "Death...", 10)
]

KNIGHT_INITAL_MOVES = [
    Move("Pile Driver", 5, "Wow"),
    Move("Fireball", 3, "Wooosh"),
    Move("Iceball", 2, "fzzzz")
]

KNIGHT_LEARNED_MOVES = [
    Move("Mega Kick", 10, "POW", 5),
    Move("Growl", 11, "Grrrr", 8),
    Move("Shadowball", 15, "Death...", 10)
]

ALL_MOVES = {
    MAGE: {INITAL_MOVES: MAGE_INITAL_MOVES, LEARNED_MOVES: MAGE_LEARNED_MOVES},
    ROUGE: {INITAL_MOVES: ROUGE_INITAL_MOVES, LEARNED_MOVES: ROUGE_LEARNED_MOVES},
    KNIGHT: {INITAL_MOVES: KNIGHT_INITAL_MOVES, LEARNED_MOVES: KNIGHT_LEARNED_MOVES}
}
