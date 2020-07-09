import random, sys
from moves import ALL_MOVES
from character import Character
from party_constructor import PartyConstructor
from map_generator import MapGenerator

def main():

    map_gen = MapGenerator()
    map_gen.generate_map()
    # party = PartyConstructor(ALL_MOVES)

    # i = 0
    # while i < 3:
    #     party.build_character(Character)
    #     i += 1

if __name__ == "__main__":
    main()


# Game mechanics:
    # Characters have unique move sets determined by the class chosen
    # Characters may use each move based off of some arb move usage currency
    
