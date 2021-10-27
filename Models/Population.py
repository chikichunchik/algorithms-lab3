class Population:
    def __init__(self, backpacks):
        self.backpacks = backpacks
        self.best_worth = max([x.worth for x in self.backpacks])
        self.best_backpack = backpacks[[x.worth for x in self.backpacks].index(self.best_worth)]

    def add(self, backpack):
        self.backpacks.append(backpack)
        self.backpacks.pop([x.worth for x in self.backpacks].index(min([x.worth for x in self.backpacks])))