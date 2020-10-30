import bpy
import os
sce = bpy.context.scene
scene_frames = 250
scale = 1
blender_frame_rate = 24 
frame_rate = 4 

print("\nBlender frame rate: " + str(blender_frame_rate))
print("Target frame rate: " + str(frame_rate))

if (blender_frame_rate % frame_rate != 0):
    nth_frame = int(round(blender_frame_rate / frame_rate))
else:
    nth_frame = int(blender_frame_rate / frame_rate)

print("\nCalculating coordinates for every " + str(nth_frame) + "th frame")
