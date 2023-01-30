from utils import *
from func.friction import Friction


class Thigh(Bone):
    def __init__(self, side):
        super().__init__(self.__class__.__name__.lower() + '.' + side)
        self.mass = 25
        self.shin =  Shin(side)

    def estimate(self, *args):
        self.rotation_x, self.vcx, frame_id = self.formula('x', args[0], args[3])
        self.rotation_euler_X(self.rotation_x)
        self.keyframe_x += frame_id

        self.keyframe_insert(frame_id)

    def formula(self, coordinate, torque, duration):
        # force_rate = fragment.torque_x / (fragment.torque_x + fragment.torque_y)

        vc = getattr(self, "vc"+coordinate)
        if duration == -1: # until touch the ground
            cur_rotation = getattr(self, "rotation_"+coordinate)
            a = (torque - self.gravity * self.mass) / self.mass
            if a != 0:
                duration = pow((cur_rotation * 2 * a + vc * vc) / (a * a), 0.5)
                vt = 0
            else:
                duration = cur_rotation / vc
                vt = 0
            rotation = -1 * cur_rotation
        elif duration == -2: # on the ground
            a = torque / self.mass
            if a != 0:
                vt = vc + a * duration
                rotation = (vt * vt - vc * vc) / (2 * a)
            else:
                vt = vc
                rotation = vt * duration
        else:
            a = (torque - self.gravity * self.mass) / self.mass
            if a != 0:
                vt = vc + a * duration
                rotation = (vt * vt - vc * vc) / (2 * a)
            else:
                vt = vc
                rotation = vt * duration

        # a = (fragment.torque_y - (1 - force_rate) * self.gravity * self.mass) / self.mass
        # if a != 0:
        #     vt = a * fragment.duration
        #     self.rotation_y = (vt * vt - self.vcy * self.vcy) / (2 * a)
        #     self.vcy = vt

        # a = fragment.torque_z / self.mass
        # if a != 0:
        #     vt = a * fragment.duration
        #     self.rotation_z = (vt * vt - self.vcz * self.vcz) / (2 * a)
        #     self.vcz = vt

        frame_id = self.current_frame + duration * self.fps

        return rotation, vt, frame_id

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
        self.mass = 15
        self.foot = Foot(side)

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
    def __init__(self, side):
        super().__init__(self.__class__.__name__.lower() + '.' + side)
        self.mass = 5
        self.toe = Toe(side)
        self.heel = Heel(side)

class Toe(Bone):
    def __init__(self, side):
        super().__init__(self.__class__.__name__.lower() + '.' + side)
        self.mass = 3
        # self.friction = Friction()

    def func_switch(self, func):
        if func == 'friction':
            # 1.keep motionless
            # 2.let root bone move
            pass
        elif func == 'inaction':
            # do nothing
            pass

class Heel(Bone):
    def __init__(self, side):
        super().__init__(self.__class__.__name__.lower() + '.' + side)
        self.mass = 2