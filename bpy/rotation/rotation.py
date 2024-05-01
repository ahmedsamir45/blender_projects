import math
import bpy

bpy.ops.mesh.primitive_cube_add()
cube = bpy.context.active_object

cube.rotation_euler.z=0


start_frame = 1
cube.keyframe_insert("rotation_euler",frame=start_frame)

degree1 = math.radians(360)

cube.rotation_euler.z=degree1

mid_frame = 125
cube.keyframe_insert("rotation_euler",frame=mid_frame)

degree2 = math.radians(0)

cube.rotation_euler.z=degree2

fin_frame=360
cube.keyframe_insert("rotation_euler",frame=fin_frame)