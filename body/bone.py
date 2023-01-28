from utils import *

rigify = 'metarig'

class Config(object):
    def __init__(self):
        self.gravity = 100
        self.fps = 120
        self.current_frame = 0

class Bone(Config):
    def __init__(self, name):
        self.rotation_mode = 'XYZ'
        self.bone = ''
        self.name = name
        self.mass = 0

        self.vcx = 0
        self.vcy = 0
        self.vcz = 0

        self.support = 0
        self.friction = 0

        self.rotation_x = 0
        self.rotation_y = 0
        self.rotation_z = 0

        self.init()

    def init(self):
        self.bone = bpy.data.objects[rigify].pose.bones[self.name]
        self.bone.rotation_mode = self.rotation_mode

    def rotation_euler_X(self, x):
        self.bone.rotation_euler.rotate_axis("X", x)

    def rotation_euler_Y(self, y):
        self.bone.rotation_euler.rotate_axis("Y", y)

    def rotation_euler_Z(self, z):
        self.bone.rotation_euler.rotate_axis("Z", z)

    def keyframe_insert(self, frame_id):
        self.bone.keyframe_insert(data_path="rotation_euler" ,frame = frame_id)