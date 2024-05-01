
from bpy import *
from math import *


ops.mesh.primitive_cube_add()
c=context.active_object

f=0
angle=0
radius=5
c.location=(radius,0,0)

while angle <=(2*3.14*radius):
    x= cos(angle)*radius
    y= sin(angle)*radius
    c.location=(x,y,0)
    c.keyframe_insert("location",frame=f)
    
    f+=20
    angle+=1
 
fra=(int(2*3.14*radius)/1)*20   
frame_rate=context.scene
frame_rate.frame_start=0
frame_rate.frame_end=fra
