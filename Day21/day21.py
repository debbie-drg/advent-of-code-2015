import sys
from math import ceil
from itertools import combinations

WEAPONS = {  # Cost, Damage, Armor
    "Dagger": [8, 4, 0],
    "Shortsword": [10, 5, 0],
    "Warhammer": [25, 6, 0],
    "Longsword": [40, 7, 0],
    "Greataxe": [74, 8, 0],
}

ARMOR = {  # Cost, Damage, Armor
    "No armor": [0, 0, 0],
    "Leather": [13, 0, 1],
    "Chainmail": [31, 0, 2],
    "Splintmail": [53, 0, 3],
    "Bandedmail": [75, 0, 4],
    "Platemail": [102, 0, 5],
}

RINGS = {  # Cost, Damage, Armor
    "Damage +1": [25, 1, 0],
    "Damage +2": [50, 2, 0],
    "Damage +3": [100, 3, 0],
    "Defense +1": [20, 0, 1],
    "Defense +2": [40, 0, 2],
    "Defense +3": [80, 0, 3],
}


class Player:
    def __init__(self, hp: int):
        self.hp = hp
        self.damage = 0
        self.armor = 0

    def set_damage(self, damage: int):
        self.damage = damage

    def increase_damage(self, damage_increase: int):
        self.damage += damage_increase

    def decrease_damage(self, damage_decrease: int):
        self.damage -= damage_decrease

    def set_armor(self, armor: int):
        self.armor = armor

    def increase_armor(self, armor_increase: int):
        self.armor += armor_increase

    def decrease_armor(self, armor_decrease: int):
        self.armor -= armor_decrease

    def add_ring(self, ring_stats: list[int]):
        self.increase_damage(ring_stats[1])
        self.increase_armor(ring_stats[2])

    def remove_ring(self, ring_stats: list[int]):
        self.decrease_damage(ring_stats[1])
        self.decrease_armor(ring_stats[2])

    def turns_to_defeat(self, enemy):
        enemy_armor = enemy.armor
        enemy_hp = enemy.hp
        damage_per_turn = max(1, self.damage - enemy_armor)
        return ceil(enemy_hp // damage_per_turn)


class Boss(Player):
    def __init__(self, hp: int, damage: int, armor: int):
        self.hp = hp
        self.damage = damage
        self.armor = armor


def is_victorious(player: Player, boss: Boss) -> bool:
    return player.turns_to_defeat(boss) <= boss.turns_to_defeat(player)


def try_weapons(player: Player, boss: Boss, lose: bool = False) -> int:
    optimal_cost = 0 if lose else sys.maxsize

    for weapon in WEAPONS:
        weapon_stats = WEAPONS[weapon]
        player.set_damage(weapon_stats[1])
        next_cost = try_armor(player, boss, weapon_stats[0], lose)
        optimal_cost = max(optimal_cost, next_cost) if lose else min(optimal_cost, next_cost)

    return optimal_cost


def try_armor(player: Player, boss: Boss, cost: int, lose: bool = False) -> int:
    optimal_cost = 0 if lose else sys.maxsize

    for armor in ARMOR:
        armor_stats = ARMOR[armor]
        player.set_armor(armor_stats[2])
        next_cost = try_ring(player, boss, cost + armor_stats[0], lose)
        optimal_cost = max(optimal_cost, next_cost) if lose else min(optimal_cost, next_cost)

    return optimal_cost


def try_ring(player: Player, boss: Boss, cost: int, lose: bool = False) -> int:

    if is_victorious(player, boss) and not lose:
        return cost

    optimal_cost = 0 if lose else sys.maxsize

    ring_keys = list(RINGS.keys())

    for index_1 in range(len(ring_keys)):
        ring_1_stats = RINGS[ring_keys[index_1]]
        player.add_ring(ring_1_stats)

        victory = is_victorious(player, boss)

        if victory ^ lose:
            next_cost = cost + ring_1_stats[0]
            optimal_cost = max(optimal_cost, next_cost) if lose else min(optimal_cost, next_cost)
            if not lose:
                player.remove_ring(ring_1_stats)
                continue

        for index_2 in range(index_1 + 1, len(ring_keys)):
            ring_2_stats = RINGS[ring_keys[index_2]]
            player.add_ring(ring_2_stats)

            victory = is_victorious(player, boss)
            if victory ^ lose:
                next_cost = cost + ring_1_stats[0] + ring_2_stats[0]
                optimal_cost = max(optimal_cost, next_cost) if lose else min(optimal_cost, next_cost)


            player.remove_ring(ring_2_stats)

        player.remove_ring(ring_1_stats)

    return optimal_cost


def find_cheapest_victory(
    player_hp: int, boss_hp: int, boss_damage: int, boss_armor: int
) -> int:
    player = Player(player_hp)
    boss = Boss(boss_hp, boss_damage, boss_armor)
    return try_weapons(player, boss)


def find_most_expensive_loss(
    player_hp: int, boss_hp: int, boss_damage: int, boss_armor: int
) -> int:
    player = Player(player_hp)
    boss = Boss(boss_hp, boss_damage, boss_armor)
    return try_weapons(player, boss, True)


if __name__ == "__main__":
    try:
        file_name = sys.argv[1]
    except IndexError:
        file_name = "input.txt"
    player_hp = 100
    boss_stats = [line.split(" ") for line in open(file_name).read().strip().split("\n")]
    boss_hp = int(boss_stats[0][-1])
    boss_damage = int(boss_stats[1][-1])
    boss_armor = int(boss_stats[2][-1])

    cheapest_victory = find_cheapest_victory(player_hp, boss_hp, boss_damage, boss_armor)

    print(f"The least gold you can spend to defeat the boss is {cheapest_victory}.")

    most_expensive_loss = find_most_expensive_loss(player_hp, boss_hp, boss_damage, boss_armor)

    print(f"The most expensive loss costs {most_expensive_loss}.")