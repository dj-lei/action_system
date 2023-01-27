import bpy

from body.bone import Bone

def import_scene(path):
    bpy.ops.import_scene.fbx(filepath = path)

def export_scene(path):
    bpy.ops.export_scene.fbx(filepath = path)