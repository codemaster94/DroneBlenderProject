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



ob = bpy.data.objects['Sphere']
for f in range(sce.frame_start, scene_frames):
    if (((f-1) % nth_frame) == 0):
        sce.frame_set(f)
        # get scaled position
        x = int(ob.matrix_world.to_translation().x * 100 * scale)
        y = int(ob.matrix_world.to_translation().y * 100 * scale)
        z = int(ob.matrix_world.to_translation().z * 100 * scale)
        # get color
        r = int(ob.active_material.diffuse_color[1] * 255)
        g = int(ob.active_material.diffuse_color[2] * 255)
        b = int(ob.active_material.diffuse_color[3] * 255)
        print("X_cordinate = " + x +"mm")
   
