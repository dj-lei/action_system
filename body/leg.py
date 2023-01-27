from utils import *
from func.friction import Friction


class Thigh(Bone):
    def __init__(self, side):
        super().__init__(self.__class__.__name__.lower() + '.' + side)
        self.shin =  Shin(side)

    def func_switch(self, func, x, y, z, frame_id, *args):
        if func == 'motion':
            # motion
            self.rotation_euler_X(x)
            self.rotation_euler_Y(y)
            self.rotation_euler_Z(z)
            self.keyframe_insert(frame_id)
        elif func  == 'centrifugal':
            # Maximize strength
            pass
        elif func  == 'support':
            # do nothing keep motionless
            self.rotation_euler_X(x)
            self.rotation_euler_Y(y)
            self.rotation_euler_Z(z)
            self.keyframe_insert(frame_id)
        elif func  == 'inaction':
            # do nothing keep parent
            pass

class Shin(Bone):
    def __init__(self, side):
        super().__init__(self.__class__.__name__.lower() + '.' + side)
        self.foot = Foot()

    def func_switch(self, func, x, y, z, frame_id, *args):
        if func == 'motion':
            # motion
            self.rotation_euler_X(x)
            self.rotation_euler_Y(y)
            self.rotation_euler_Z(z)
            self.keyframe_insert(frame_id)
        elif func  == 'centrifugal':
            # Maximize strength
            pass
        elif func  == 'support':
            # do nothing keep motionless
            self.rotation_euler_X(x)
            self.rotation_euler_Y(y)
            self.rotation_euler_Z(z)
            self.keyframe_insert(frame_id)
        elif func  == 'inaction':
            # do nothing keep parent
            pass

class Foot(Bone):
    def __init__(self):
        self.toe = Toe()
        self.heel = Heel()

class Toe(Bone):
    def __init__(self):
        self.friction = Friction()

    def func_switch(self, func):
        if func == 'friction':
            # 1.keep motionless
            # 2.let root bone move
            pass
        elif func == 'inaction':
            # do nothing
            pass

class Heel(Bone):
    def __init__(self):
        self.subscribes = [] 