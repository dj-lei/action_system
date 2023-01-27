from utils import *
from .leg import *

 
class Body(object):
    def __init__(self):
        self.thigh_L = Thigh('L')
        self.thigh_R = Thigh('R')

    def walk(self):
        action_walk_right_leg = {
            'thigh': [
                ('support', 0, 0, 0, 0),
                ('motion', -0.3, 0, 0, 30),
                ('motion', 0.6, 0, 0, 90),
                ('motion', -0.6, 0, 0, 150),
                ('motion', 0.6, 0, 0, 210),
                ('support', -0.3, 0, 0, 240)
                ],
            'shin': [
                ('support', 0, 0, 0, 0),
                ('motion', 0.2, 0, 0, 30),
                ('motion', -0.2, 0, 0, 90),
                ('motion', 0.2, 0, 0, 150),
                ('motion', -0.2, 0, 0, 210),
                ('support', 0.2, 0, 0, 240)
            ],
            'foot': [(),()],
            'toe': [(),()],
            'heel': [(),()],
        }

        action_walk_left_leg = {
            'thigh': [
                ('support', 0, 0, 0, 0),
                ('motion', 0.3, 0, 0, 30),
                ('motion', -0.6, 0, 0, 90),
                ('motion', 0.6, 0, 0, 150),
                ('motion', -0.6, 0, 0, 210),
                ('support', 0.3, 0, 0, 240)
                ],
            'shin': [
                ('support', 0, 0, 0, 0),
                ('motion', 0.2, 0, 0, 30),
                ('motion', -0.2, 0, 0, 90),
                ('motion', 0.2, 0, 0, 150),
                ('motion', -0.2, 0, 0, 210),
                ('support', 0.2, 0, 0, 240)
            ],
            'foot': [(),()],
            'toe': [(),()],
            'heel': [(),()],
        }

        for func,x,y,z,frame_id in action_walk_right_leg['thigh']:
            self.thigh_R.func_switch(func,x,y,z,frame_id)

        for func,x,y,z,frame_id in action_walk_right_leg['thigh']:
            self.thigh_R.shin.func_switch(func,x,y,z,frame_id)

        for func,x,y,z,frame_id in action_walk_left_leg['thigh']:
            self.thigh_L.func_switch(func,x,y,z,frame_id)