class Backpack:
    def __init__(self, items, max_weight):
        self.max_weight = max_weight
        self.items = items
        self.worth = sum([items[0][x].worth*int(items[1][x]) for x in range(len(items[0]))])
        self.weight = sum([items[0][x].weight*int(items[1][x]) for x in range(len(items[0]))])
        if self.weight > max_weight:
            self.worth = 0

    def __str__(self):
        return 'weight = ' + str(self.weight) + '\nworth = ' + str(self.worth) + \
            '\nItems = ' + str(self.items[1])

    def recount(self):
        self.worth = sum([self.items[0][x].worth * int(self.items[1][x]) for x in range(len(self.items[0]))])
        self.weight = sum([self.items[0][x].weight * int(self.items[1][x]) for x in range(len(self.items[0]))])
        if self.weight > self.max_weight:
            self.worth = 0