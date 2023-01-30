from utils import *
from .leg import *

 
class Body(object):
    def __init__(self):
        self.thigh_L = Thigh('L')
        self.thigh_R = Thigh('R')