import random

class Plant:
    def __init__(self):
        self.age = 0
        self.status = True

    def age_up(self):
        if random.randint(0, 1) == 1:
            self.age += 1
            self.status = True
        else:
            self.age = 0
            self.status = False

    def reset(self):
        self.__init__()

    def __str__(self):
        return 'Age: ' + str(self.age) + ', Alive: ' + str(self.status)