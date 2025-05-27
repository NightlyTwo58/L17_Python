from plant import Plant

class ZeroException(Exception):
    pass

class Garden:
    # careful this class variable will get shared by all instances of this class
    # this variable is shared across all instances
    age = 0

    def __init__(self, width, height):
        # these variables are unique to each instance
        if width < 0 or height < 0:
            raise ZeroException
        else:
            self.width = width
            self.height = height
            self.plants = [Plant() for _ in range(width * height)]

    def age_up(self):
        self.age += 1
        for i, plant in enumerate(self.plants):
            plant.age_up()

    def reset(self):
        self.age = 0
        for i, plant in enumerate(self.plants):
            plant.reset()

class SquareGarden(Garden):
    def __init__(self, side_length):
        if side_length < 0:
            raise ZeroException
        else:
            self.width = side_length
            self.height = side_length
            self.plants = [Plant() for _ in range(side_length ** 2)]

    # parental init method inherited
    # def __init__(self, width, height):
    #     self.width = width
    #     self.height = height
    #     self.plants = [Plant() for _ in range(width * height)]