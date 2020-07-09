import random
from room import Room
import time


class MapGenerator:
    def __init__(self):
        self.map = []
        self._max_x, self._max_y = 9, 9
        self._min_x, self._min_y = 0, 0
        self._n, self._s, self._e, self._w = 'n', 's', 'e', 'w'
        self._possible_starts = [
            [self._min_x, self._min_y],
            [self._min_x, self._max_y],
            [self._max_x, self._min_y],
            [self._max_x, self._max_y]
        ]
        self._directions = [self._n, self._s, self._e, self._w]

    def _pick_start(self):
        return random.choice(self._possible_starts)

    def _pick_exit(self, start_room):
        exit_room_cords = [self._min_x, self._min_y]
        if start_room.cords[0] == self._min_x:
            exit_room_cords[0] = self._max_x
        if start_room.cords[1] == self._min_y:
            exit_room_cords[1] = self._max_y
        return exit_room_cords

    def _may_generate(self):
        role = random.randint(0, 1)
        if role == 0:
            return True
        else:
            return False

    def is_valid_direction(self, chosen_direction, current_cords):
        if chosen_direction == self._n:
            if current_cords[1] + 1 > self._max_y:
                return False
            return True
        elif chosen_direction == self._s:
            if current_cords[1] - 1 < self._min_y:
                return False
            return True
        elif chosen_direction == self._e:
            if current_cords[0] + 1 > self._max_x:
                return True
            return False
        elif chosen_direction == self._w:
            if current_cords[0] - 1 < self._min_x:
                return False
            return True

    def _update_cords(self, chosen_direction, current_cords):
        if chosen_direction == self._n:
            current_cords[1] += 1
        elif chosen_direction == self._s:
            current_cords[1] -= 1
        elif chosen_direction == self._e:
            current_cords[0] += 1
        elif chosen_direction == self._w:
            current_cords[0] -= 1
        return current_cords

    def _link_rooms(self, old_room, new_room, chosen_direction):
        if chosen_direction == self._n:
            new_room.s_to = old_room
            old_room.n_to = new_room
        elif chosen_direction == self._s:
            new_room.n_to = old_room
            old_room.s_to = new_room
        elif chosen_direction == self._e:
            new_room.w_to = old_room
            old_room.e_to = new_room
        elif chosen_direction == self._w:
            new_room.e_to = old_room
            old_room.w_to = new_room

    def _is_at_exit(self, current_cords, exit_room_cords):
        if current_cords == exit_room_cords:
            return True
        return False

    def _is_empty(self, a_list):
        if a_list == []:
            return True
        return False

    def generate_map(self):
        start_room = Room(self._pick_start())
        exit_room = Room(self._pick_exit(start_room))
        prev_cords = []
        current_room = start_room
        self.map.append(current_room)

        while not self._is_at_exit(current_room.cords, exit_room.cords):
            generation_canditates = []
            for d in self._directions:
                if self._may_generate():
                    generation_canditates.append(d)

            if self._is_empty(generation_canditates):
                continue

            chosen_direction = random.choice(generation_canditates)

            if current_room.cords in prev_cords:
                continue

            if self.is_valid_direction(chosen_direction, current_room.cords):
                current_room.cords = self._update_cords(
                    chosen_direction, current_room.cords)

                new_room = Room(current_room.cords)
                self._link_rooms(current_room, new_room, chosen_direction)

                self.map.append(new_room)

                current_room = new_room

                prev_cords.append(current_room.cords)
