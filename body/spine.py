from utils import *

# spine0-1 waist
class spine0(Bone):
    def __init__(self):
        self.mass = 300

class spine1(Bone):
    def __init__(self):
        self.mass = 140

# spine2-4 chest
class spine2(Bone):
    def __init__(self):
        self.subscribes = 100

class spine3(Bone):
    def __init__(self):
        self.subscribes = 100

class spine4(Bone):
    def __init__(self):
        self.subscribes = 130

# spine5 head
class spine5(Bone):
    def __init__(self):
        self.mass = 80