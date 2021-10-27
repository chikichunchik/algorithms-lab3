from Solver.GeneticAlgorithm import GeneticAlgorithm
from Models.Backpack import Backpack
from Models.Population import Population
from Models.Item import Item
import random

items = []
for i in range(100):
    items.append(Item(random.randint(2, 20), random.randint(1, 10)))
backpacks = []
for i in range(100):
    item_bool = [False]*100
    item_bool[i] = True
    backpacks.append(Backpack([items, item_bool], 200))

population = Population(backpacks)

ga = GeneticAlgorithm(population, 10000, 0.1)
ga.solve()
print(ga.get_solution())