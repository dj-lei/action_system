import bpy
import math
from mathutils import Vector, Quaternion

rigify = 'metarig'

class Config(object):
    def __init__(self):
        self.gravity = 2000
        self.fps = 120
        self.current_frame = 0


class Bone(Config):
    def __init__(self, name):
        super().__init__()
#        self.rotation_mode = 'XYZ'
        self.bone = ''
        self.name = name
        self.mass = 0
        self.direction = 1

        self.vcx = 0
        self.vcy = 0
        self.vcz = 0

        self.rotation_x = 0
        self.rotation_y = 0
        self.rotation_z = 0

        self.keyframe_x = 0
        self.keyframe_y = 0
        self.keyframe_z = 0

        self.init()

    def init(self):
        self.bone = bpy.data.objects[rigify].pose.bones[self.name]
#        self.bone.rotation_mode = self.rotation_mode

    def rotation_euler_X(self, x):
        self.bone.rotation_euler.rotate_axis("X", self.direction * math.radians(x))

    def rotation_euler_Y(self, y):
        self.bone.rotation_euler.rotate_axis("Y", self.direction * math.radians(y))

    def rotation_euler_Z(self, z):
        self.bone.rotation_euler.rotate_axis("Z", self.direction * math.radians(z))

    def keyframe_insert(self, frame_id):
        self.bone.keyframe_insert(data_path="rotation_euler" ,frame = frame_id)

    def reset(self):
        bpy.data.objects[rigify].animation_data_clear()
        self.bone.rotation_euler  = [0, 0, 0]
        self.keyframe_insert(0)


class Body(object):
    def __init__(self):
        self.thigh_L = Thigh('L')
        self.thigh_R = Thigh('R')


class Thigh(Bone):
    def __init__(self, side):
        super().__init__(self.__class__.__name__.lower() + '.' + side)
        self.mass = 25
        self.direction = -1
        self.shin =  Shin(side)

    def estimate(self, args):
        rotation_x, self.vcx, frame_id = self.formula('x', args[0], args[3])

        self.rotation_x += int(rotation_x)
        self.rotation_euler_X(rotation_x)

        self.keyframe_x += int(frame_id)
        self.keyframe_insert(self.keyframe_x)
        
        print(self.rotation_x, self.vcx, self.keyframe_x)

    def formula(self, coordinate, torque, duration):
        # force_rate = fragment.torque_x / (fragment.torque_x + fragment.torque_y)

        vc = getattr(self, "vc"+coordinate)
        cur_rotation = getattr(self, "rotation_"+coordinate)
        if duration == -1: # until touch the ground
            a = (torque - self.gravity * self.mass) / self.mass
            if a != 0:
                duration = pow(-2 * cur_rotation / a, 0.5)
                vt = 0
            else:
                duration = cur_rotation / vc
                vt = 0
            rotation = -1 * cur_rotation
        elif duration == -2: # on the ground
            a = torque / self.mass
            vt = vc + a * duration
            rotation = (vt * vt - vc * vc) / (2 * a)
        elif duration == -3: # free fall until speed 0
            duration = vc / self.gravity
            a = -1 * self.gravity
            vt = 0
            rotation = (vt * vt - vc * vc) / (2 * a)
        else:
            a = (torque - self.gravity * self.mass) / self.mass
            if a != 0:
                vt = vc + a * duration
                rotation = (vt * vt - vc * vc) / (2 * a)
            else:
                vt = vc
                rotation = vt * duration

        frame_id = self.current_frame + duration * self.fps

        return rotation, vt, frame_id


class Shin(Bone):
    def __init__(self, side):
        super().__init__(self.__class__.__name__.lower() + '.' + side)
        self.mass = 15
        self.foot = Foot(side)


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


class Heel(Bone):
    def __init__(self, side):
        super().__init__(self.__class__.__name__.lower() + '.02.' + side)
        self.mass = 2


class Person(Body):
    def __init__(self):
        super().__init__()
        self.action = {
            'thigh_L': [],
            'thigh_R': []
        }

        self.body = Body()

        self.thigh_L = self.body.thigh_L
        self.shin_L = self.body.thigh_L.shin
        self.foot_L = self.body.thigh_L.shin.foot
        self.toe_L = self.body.thigh_L.shin.foot.toe

        self.thigh_R = self.body.thigh_R
        self.shin_R = self.body.thigh_R.shin
        self.foot_R = self.body.thigh_R.shin.foot
        self.toe_R = self.body.thigh_R.shin.foot.toe

    def walk(self):
        # thigh_R support -> motion
        self.thigh_R.reset()

        thigh_R_data = [
            (61111, 0, 0, 0.3),
            (0, 0, 0, -3),
            (35000, 0, 0, -1),
            (50000, 0, 0, 0.1),
            (-200, 0, 0, 0.4)
        ]

        for keyframe in thigh_R_data:
            self.thigh_R.estimate(keyframe)
        # shin_R support -> 

        # toe_L friction -> trigger root bone move 

    def run(self):
        pass


if __name__ == '__main__':
    # bpy.ops.import_scene.fbx(filepath = 'metarig.fbx')

    person = Person()
    person.walk()

    bpy.ops.screen.animation_play()
    # export_scene('walk.fbx')