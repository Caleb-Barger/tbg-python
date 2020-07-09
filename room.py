class Room:
    def __init__(self, cords):
        self.cords = cords
        self.n_to, self.s_to, self.e_to, self.w_to = None, None, None, None

    def __str__(self):
        return f"Room @ Position - {self.cords}\nN - {self.n_to}\nS - {self.s_to}\nE  - {self.e_to}\nW - {self.w_to}"
