import numpy as np
from Models.Backpack import Backpack


class GeneticAlgorithm:
    def __init__(self, initial_population, iterations, mutation_chance):
        self.population = initial_population
        self.iterations = iterations
        self.mutation_chance = mutation_chance

    def solve(self):
        for i in range(self.iterations):
            parents = GeneticAlgorithm.get_parents(self.population)

            new_child = GeneticAlgorithm.get_child(*parents)

            if np.random.choice([True, False], p=[self.mutation_chance, 1 - self.mutation_chance]):
                new_child = GeneticAlgorithm.get_mutated(new_child)

            new_child = GeneticAlgorithm.local_upgrade(new_child)

            if new_child.worth > self.population.best_worth:
                self.population.best_worth = new_child.worth
                self.population.best_backpack = new_child

            self.population.add(new_child)

    def get_solution(self):
        return self.population.best_backpack

    @staticmethod
    def get_parents(population):
        total_population_worth = sum([x.worth for x in population.backpacks])
        return tuple(np.random.choice(population.backpacks, size=2, replace=False,
                                      p=[x.worth / total_population_worth for x in population.backpacks]))

    @staticmethod
    def get_child(parent1, parent2):
        point1 = np.random.choice(range(len(parent1.items[0]) - 2))
        point2 = np.random.choice(range(point1 + 1, len(parent1.items[0])))
        return Backpack([parent1.items[0], parent1.items[1][:point1] + parent2.items[1][point1:point2] + parent1.items[1][point2:]],
                        parent1.max_weight)

    @staticmethod
    def get_mutated(backpack):
        change_index = np.random.choice(len(backpack.items[0]))
        backpack.items[1][change_index] = False if backpack.items[1][change_index] else True
        backpack.recount()
        return backpack

    @staticmethod
    def local_upgrade(backpack):
        start_worth = backpack.worth
        start_backpack = backpack
        max_item_worth = max([backpack.items[0][x].worth for x in range(len(backpack.items[0])) if not backpack.items[1][x]])
        max_worth_item_index = [backpack.items[0][x].worth for x in range(len(backpack.items[0]))].index(max_item_worth)
        backpack.items[1][max_worth_item_index] = True
        backpack.recount()
        iterations = 0
        while backpack.worth == 0 and iterations < 100:
            min_item_worth = min(
                [backpack.items[0][x].worth for x in range(len(backpack.items[0])) if backpack.items[1][x]])
            min_worth_item_index = [backpack.items[0][x].worth for x in range(len(backpack.items[0]))].index(min_item_worth)
            backpack.items[1][min_worth_item_index] = False
            backpack.recount()
            iterations += 1

        if start_worth > backpack.worth:
            return start_backpack

        return backpack
