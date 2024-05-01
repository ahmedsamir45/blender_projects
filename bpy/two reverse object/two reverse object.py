import bpy

# add cylinder and get instance
bpy.ops.mesh.primitive_cylinder_add()
clyinder1 = bpy.context.active_object

#intial location
clyinder1.location=(5,5,5)
# frame 1
start = 1
clyinder1.keyframe_insert("location",frame=start)
# the clyinder will try to change its position until the middle frame
clyinder1.location.x = -5
clyinder1.location.y = -5
clyinder1.location.z = -5

middle = 120
clyinder1.keyframe_insert("location",frame=middle)
# the clyinder will try to come back untill the final frame
clyinder1.location.x = 5
clyinder1.location.y = 5
clyinder1.location.z = 5

final = 250
clyinder1.keyframe_insert("location",frame=final)

###################################################################################
# add cone and get instance
bpy.ops.mesh.primitive_cone_add()
cone = bpy.context.active_object

# intial location will the be the end point of the clyinder
cone.location=(-5,-5,-5)
start = 1 # you can remove this variable because you assign it in above
cone.keyframe_insert("location",frame=start)

# this is the start position of clyinder and so on
cone.location.x = 5
cone.location.y = 5
cone.location.z = 5

middle = 120 # you can remove this variable because you assign it in above
cone.keyframe_insert("location",frame=middle)


cone.location.x = -5
cone.location.y = -5
cone.location.z = -5

final = 250 # you can remove this variable because you assign it in above
cone.keyframe_insert("location",frame=final)