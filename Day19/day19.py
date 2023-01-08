import sys


def detect_substring(small_string: str, big_string: str) -> list[int]:
    len_small = len(small_string)
    positions = []
    for index in range(len(big_string) - len_small + 1):
        substring = big_string[index : (index + len_small)]
        if substring == small_string:
            positions.append(index)
    return positions


def substitute_string(
    small_string: str, big_string: str, substitute_string: str, index: int
) -> str:
    return (
        big_string[:index]
        + substitute_string
        + big_string[(index + len(small_string)) :]
    )


def parse_substitutions(reactions: str):
    split_reactions = reactions.split("\n")
    substitutions = dict()
    for reaction in split_reactions:
        reaction = reaction.split(" => ")
        try:
            substitutions[reaction[0]].append(reaction[1])
        except KeyError:
            substitutions[reaction[0]] = [reaction[1]]
    return substitutions


def find_all_molecules(molecule: str, substitutions: dict) -> set:
    transformed_molecules = set()
    for to_change in substitutions:
        indices = detect_substring(to_change, molecule)
        if not indices:
            continue
        for substitute_molecule in substitutions[to_change]:
            for index in indices:
                transformed_molecules.add(
                    substitute_string(to_change, molecule, substitute_molecule, index)
                )
    return transformed_molecules


def number_steps(molecule: str, len_e: int) -> int:
    number_atoms = sum([char.isupper() for char in molecule])
    number_ar = molecule.count("Ar")
    number_rn = molecule.count("Rn")
    number_y = molecule.count("Y")
    return number_atoms - number_ar - number_rn - 2 * number_y - (len_e - 1)


if __name__ == "__main__":
    try:
        file_name = sys.argv[1]
    except IndexError:
        file_name = "input.txt"
    reactions, molecule = open(file_name).read().split("\n\n")
    substitutions = parse_substitutions(reactions)
    valid_molecules = find_all_molecules(molecule, substitutions)
    print(f"There are {len(valid_molecules)} possible molecules after the reaction.")

    len_e = len(substitutions["e"][0])
    steps_to_synthesize = number_steps(molecule, len_e)
    print(f"It takes {steps_to_synthesize} steps to synthesize the molecule.")
