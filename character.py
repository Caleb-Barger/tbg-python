class Character:
    def __init__(self, name, base_stats, move_set, learned_moves):
        self.name = name
        self.max_hp, self.base_atk, self.base_defend = base_stats
        self.hp = self.max_hp
        self.move_set = move_set
        self.learned_moves = learned_moves
        self.is_alive = True
        self.xp = 0
        self.lv = 0
        self.xp_to_lv_up = 100  # <--- Another magic number
        self._lvs_to_learn_move = [m.lv_learned for m in learned_moves]

    def _should_learn_new_move(self):
        if self.lv in self._lvs_to_learn_move:
            return True
        return False

    def _which_move_to_learn(self):
        for m in self.learned_moves:
            if m.lv_learned == self.lv:
                return m

    def _learn_new_move(self):
        new_move = self._which_move_to_learn()
        self.move_set.append(new_move)

    def _lv_up(self):
        # MAGIC NUMBERS FIX THIS
        self.base_atk += 1
        self.base_defend += 1
        self.max_hp += 1

        if self._should_learn_new_move():
            self._learn_new_move()

    def _did_lv_up(self):
        while self.xp >= self.xp_to_lv_up:
            self.xp = self.xp - self.xp_to_lv_up
            self.xp_to_lv_up += 10  # <--- ANOTHER MAGIC NUMBER
            self.lv += 1
            self._lv_up()

    def _check_is_dead(self):
        if self.hp <= 0:
            self.is_alive = False
            self.hp = 0

    def gain_xp(self, xp_amt):
        self.xp += xp_amt
        self._did_lv_up()

    def take_dmg(self, dmg_amt):
        if not dmg_amt - self.base_defend < 0:
            self.hp -= dmg_amt - self.base_defend
            self._check_is_dead()

    def print_moves(self):
        print("\nMOVES:")
        for m in self.move_set:
            print(m)

    def __str__(self):
        return f"""\n{self.name.upper()}:\nAlive - {self.is_alive}\nMax HP - {self.max_hp}\nCurrent HP - {self.hp}\nBase Atk - {self.base_atk}\nBase Defend - {self.base_defend}\nLV - {self.lv}\nXP - {self.xp}\nXP to nxt LV - {self.xp_to_lv_up - self.xp}"""
