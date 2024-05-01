import bpy
import math
bpy.ops.mesh.primitive_cube_add()

cube = bpy.context.active_object

start_frame = 1
cube.keyframe_insert("rotation_euler",frame=start_frame)

degrees = 90
radians = math.radians(degrees)
cube.rotation_euler.z= radians

mid_frame = 90
cube.keyframe_insert("rotation_euler",frame=mid_frame)

degrees = 90
radians = math.radians(degrees)
cube.rotation_euler.x= radians


end_frame=180

cube.keyframe_insert("rotation_euler",frame=end_frame)
