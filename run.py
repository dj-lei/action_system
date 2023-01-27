from utils import *
from role.person import Person


if __name__ == '__main__':
    bpy.ops.import_scene.fbx(filepath = 'metarig.fbx')

    person = Person()
    person.walk()

    export_scene('walk.fbx')