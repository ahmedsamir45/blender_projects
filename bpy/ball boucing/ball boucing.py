import bpy
from bpy import *

# add sphere
ops.mesh.primitive_uv_sphere_add()
sphere = context.active_object


# add plane
ops.mesh.primitive_plane_add()
plane =context.active_object


# plane location and size
plane.location = (0,0,0)
plane.scale=(3,3,3)


# intial hieght
temp=10
sphere.location.z = temp 
startFrame=1
frameRate=30


# frames
while (frameRate>0 and sphere.location.z > 1) :
    
    # frame1
    sphere.keyframe_insert("location",frame=startFrame)
    
    # change location and increase frames by frame rate
    startFrame+=frameRate
    sphere.location.z=1
    
    
#    frame2
    sphere.keyframe_insert("location",frame=startFrame)
    
    
    # update height and change location increase frames by frame rate
    temp=temp//2
    startFrame+=frameRate 
    sphere.location.z =temp
    
    
#    frame3   
    sphere.keyframe_insert("location",frame=startFrame)
    
    
    # decrese the frame rate for increase velocety
    frameRate-=10
   