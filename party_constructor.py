class PartyConstructor:
    def __init__(self, all_moves):
        self._init_vars()
        self.all_moves = all_moves
        self.party = []
        self.class_choices = [self._mage, self._rouge, self._knight]
        self.gold = 0

    def _init_vars(self):
        self._mage = "mage"
        self._mage_hp = 100
        self._mage_base_atk = 4
        self._mage_base_defend = 4
        self._rouge = "rouge"
        self._rouge_hp = 80
        self._rouge_base_atk = 5
        self._rouge_base_defend = 3
        self._knight = "knight"
        self._knight_hp = 120
        self._knight_base_atk = 3
        self._knight_base_defend = 5
        self._inital_moves = "inital_moves"
        self._learned_moves = "learned_moves"

    def _name_select(self):
        return input("Character Name : ")

    def _class_select(self):
        print(self.class_choices)
        class_choice = None
        while class_choice not in self.class_choices:
            class_choice = input(f"Class : ").lower()
        return class_choice

    def _determine_move_set(self, class_choice):
        if class_choice == self._mage:
            return (self.all_moves[self._mage][self._inital_moves], self.all_moves[self._mage][self._learned_moves])
        elif class_choice == self._rouge:
            return (self.all_moves[self._rouge][self._inital_moves], self.all_moves[self._rouge][self._learned_moves])
        elif class_choice == self._knight:
            return (self.all_moves[self._knight][self._inital_moves], self.all_moves[self._knight][self._learned_moves])

    def _determine_stats(self, class_choice):
        if class_choice == self._mage:
            return (self._mage_hp, self._mage_base_atk, self._mage_base_defend)
        elif class_choice == self._rouge:
            return (self._rouge_hp, self._rouge_base_atk, self._rouge_base_defend)
        elif class_choice == self._knight:
            return (self._knight_hp, self._knight_base_atk, self._knight_base_defend)

    def build_character(self, Character):
        name = self._name_select()
        class_choice = self._class_select()
        inital_moves, learned_moves = self._determine_move_set(class_choice)
        inital_moves_copy = [m for m in inital_moves]
        learned_moves_copy = [m for m in learned_moves]
        new_character = Character(name, self._determine_stats(
            class_choice), inital_moves_copy, learned_moves_copy)

        self.party.append(new_character)

    def add_gold(self, gold):
        self.gold += gold