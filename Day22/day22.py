import sys
from copy import copy


def player_turn(
    player_stats: list[int],
    player_effects: list[int],
    boss_stats: list[int],
    min_mana: int = 100000000,
    used_mana: int = 0,
    hard_mode: bool = False,
) -> int:
    if hard_mode:
        player_stats[0] -= 1

    if player_stats[0] <= 0:
        return 100000000

    if player_effects[0] == 1:
        player_stats[1] = 0
    if player_effects[0] > 0:
        player_effects[0] -= 1
    if player_effects[1] > 0:
        player_effects[1] -= 1
        boss_stats = [boss_stats[0] - 3, boss_stats[1]]
    if player_effects[2] > 0:
        player_stats[2] += 101
        player_effects[2] -= 1

    if boss_stats[0] <= 0:
        return min(min_mana, used_mana)

    if player_stats[2] < 53:
        return 100000000

    # Magic missile
    cost = 53
    if used_mana + cost > min_mana:
        return min_mana
    min_mana = min(
        min_mana,
        boss_turn(
            [player_stats[0], player_stats[1], player_stats[2] - cost],
            copy(player_effects),
            [boss_stats[0] - 4, boss_stats[1]],
            min_mana,
            used_mana + cost,
            hard_mode,
        ),
    )

    # Drain
    cost = 73
    if player_stats[2] < cost or used_mana + cost > min_mana:
        return min_mana
    min_mana = min(
        min_mana,
        boss_turn(
            [player_stats[0] + 2, player_stats[1], player_stats[2] - cost],
            copy(player_effects),
            [boss_stats[0] - 2, boss_stats[1]],
            min_mana,
            used_mana + cost,
            hard_mode,
        ),
    )

    # Shield
    cost = 113
    if player_stats[2] < cost or used_mana + cost > min_mana:
        return min_mana
    if player_effects[0] == 0:
        min_mana = min(
            min_mana,
            boss_turn(
                [player_stats[0], 7, player_stats[2] - cost],
                [6, player_effects[1], player_effects[2]],
                copy(boss_stats),
                min_mana,
                used_mana + cost,
                hard_mode,
            ),
        )

    # Poison
    cost = 173
    if player_stats[2] < cost or used_mana + cost > min_mana:
        return min_mana
    if player_effects[1] == 0:
        min_mana = min(
            min_mana,
            boss_turn(
                [player_stats[0], player_stats[1], player_stats[2] - cost],
                [player_effects[0], 6, player_effects[2]],
                copy(boss_stats),
                min_mana,
                used_mana + cost,
                hard_mode,
            ),
        )

    # Recharge
    cost = 229
    if player_stats[2] < cost or used_mana + cost > min_mana:
        return min_mana
    if player_effects[2] == 0:
        min_mana = min(
            min_mana,
            boss_turn(
                [player_stats[0], player_stats[1], player_stats[2] - cost],
                [player_effects[0], player_effects[1], 5],
                copy(boss_stats),
                min_mana,
                used_mana + cost,
                hard_mode,
            ),
        )
    return min_mana


def boss_turn(
    player_stats: list[int],
    player_effects: list[int],
    boss_stats: list[int],
    min_mana: int,
    used_mana: int = 0,
    hard_mode: bool = False,
) -> int:
    if player_effects[0] == 1:
        player_stats[1] = 0
    if player_effects[0] > 0:
        player_effects[0] -= 1
    if player_effects[1] > 0:
        boss_stats = [boss_stats[0] - 3, boss_stats[1]]
        player_effects[1] -= 1
    if player_effects[2] > 0:
        player_stats[2] += 101
        player_effects[2] -= 1

    if boss_stats[0] <= 0:
        return min(min_mana, used_mana)

    return min(
        min_mana,
        player_turn(
            [
                player_stats[0] - (boss_stats[1] - player_stats[1]),
                player_stats[1],
                player_stats[2],
            ],
            player_effects,
            boss_stats,
            min_mana,
            used_mana,
            hard_mode,
        ),
    )


if __name__ == "__main__":
    try:
        file_name = sys.argv[1]
    except IndexError:
        file_name = "input.txt"
    boss_stats = [
        line.split(" ") for line in open(file_name).read().strip().split("\n")
    ]
    boss_hp = int(boss_stats[0][-1])
    boss_damage = int(boss_stats[1][-1])
    player_hp = 50
    player_mana = 500

    min_mana = player_turn(
        [player_hp, 0, player_mana],
        [0, 0, 0],
        [boss_hp, boss_damage],
    )

    min_mana_hard = player_turn(
        [player_hp, 0, player_mana], [0, 0, 0], [boss_hp, boss_damage], hard_mode=True
    )

    print(f"The minimum mana we can spend to win is {min_mana}")
    print(f"In hard mode, it's {min_mana_hard}")
