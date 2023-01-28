from utils import *


class shoulder(Bone):
    def __init__(self, side):
        super().__init__(self.__class__.__name__.lower() + '.' + side)
        self.mass = 4

class upper_arm(Bone):
    def __init__(self, side):
        super().__init__(self.__class__.__name__.lower() + '.' + side)
        self.mass = 12

class foream(Bone):
    def __init__(self, side):
        super().__init__(self.__class__.__name__.lower() + '.' + side)
        self.mass = 6

class hand(Bone):
    def __init__(self, side):
        super().__init__(self.__class__.__name__.lower() + '.' + side)
        self.mass = 3
