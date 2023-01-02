import sys


class ReinderCompetition:
    def __init__(self, reinder_data: list[str]):
        self.reinders = [Reinder(line) for line in reinder_data]

    def race_winner(self, number_minutes: int):
        return max(
            [reinder.distance_travelled(number_minutes) for reinder in self.reinders]
        )
    
    def points(self, number_minutes: int):
        scores = [0] * len(self.reinders)
        for _ in range(number_minutes):
            current_distances = [reinder.travel_one_second() for reinder in self.reinders]
            max_distance = max(current_distances)
            winner_indices = [index for index in range(len(self.reinders)) if current_distances[index] == (max_distance)]
            for index in winner_indices:
                scores[index] += 1
        return scores


class Reinder:
    def __init__(self, reinder_data):
        self.speed = int(reinder_data[3])
        self.time_flying = int(reinder_data[6])
        self.time_resting = int(reinder_data[-2])

        self.flying = True
        self.time_flown = 0
        self.time_rested = 0
        self.travelled = 0

    def distance_travelled(self, number_minutes: int):
        number_loops, remaining_time = divmod(number_minutes, self.time_flying + self.time_resting)
        remaining_flying_time = min(remaining_time, self.time_flying)
        return (
            number_loops * self.time_flying * self.speed + remaining_flying_time * self.speed
        )
    
    def travel_one_second(self) -> int:
        if self.flying:
            self.time_flown += 1
            self.travelled += self.speed
            if self.time_flown == self.time_flying:
                self.flying = False
                self.time_flown = 0
        else:
            self.time_rested += 1
            if self.time_rested == self.time_resting:
                self.flying = True
                self.time_rested = 0
        return self.travelled



if __name__ == "__main__":
    try:
        file_name = sys.argv[1]
    except IndexError:
        file_name = "input.txt"
    reinder_data = [
        line.split(" ") for line in open(file_name).read().strip().split("\n")
    ]

    reinder_competition = ReinderCompetition(reinder_data)
    print(
        f"The winning reinder has travelled {reinder_competition.race_winner(2503)} km."
    )

    reinder_scores = reinder_competition.points(2503)
    print(f"The reinder with the highest scores has {max(reinder_scores)} points.")
