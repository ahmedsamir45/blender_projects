import bpy
import math
bpy.ops.mesh.primitive_cube_add()

## cube 1
cube1 = bpy.context.active_object

cube1.scale = (.5,.5,.5)
cube1.location = (0,-20,0)

cube1.keyframe_insert("scale",frame=1)
cube1.keyframe_insert("rotation_euler",frame=1)
cube1.keyframe_insert("location",frame=1)

cube1.scale = (1.5,1.5,1.5)
cube1.location = (0,0,40)
cube1.rotation_euler.z= math.radians(360)

cube1.keyframe_insert("scale",frame=90)

cube1.keyframe_insert("location",frame=90)


cube1.scale = (.5,.5,.5)
cube1.location = (0,20,0)

cube1.keyframe_insert("scale",frame=140)
cube1.keyframe_insert("location",frame=140)

cube1.scale = (1,1,1)
cube1.location = (0,-20,0)

cube1.keyframe_insert("scale",frame=180)
cube1.keyframe_insert("rotation_euler",frame=180)
cube1.keyframe_insert("location",frame=180)



## cylinder 1
bpy.ops.mesh.primitive_cylinder_add()
cylinder = bpy.context.active_object

cylinder.scale = (.5,.5,.5)
cylinder.location = (0,20,0)

cylinder.keyframe_insert("scale",frame=1)
cylinder.keyframe_insert("rotation_euler",frame=1)
cylinder.keyframe_insert("location",frame=1)

cylinder.scale = (1.5,1.5,1.5)
cylinder.location = (0,0,40)
cylinder.rotation_euler.x= math.radians(360)

cylinder.keyframe_insert("scale",frame=90)

cylinder.keyframe_insert("location",frame=90)


cylinder.scale = (.5,.5,.5)
cylinder.location = (0,-20,0)

cylinder.keyframe_insert("scale",frame=140)
cylinder.keyframe_insert("location",frame=140)

cylinder.scale = (1,1,1)
cylinder.location = (0,20,0)

cylinder.keyframe_insert("scale",frame=180)
cylinder.keyframe_insert("rotation_euler",frame=180)
cylinder.keyframe_insert("location",frame=180)
