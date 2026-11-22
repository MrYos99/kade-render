# render_front32.py — NEONFALL Kade, front view, 32 samples, GPU/CUDA.
# Run: blender -b kade_tahap3_gabungan_flap.blend -P render_front32.py
import bpy
import time

prefs = bpy.context.preferences.addons['cycles'].preferences
prefs.get_devices()
print("CYCLES DEVICES:")
for d in prefs.devices:
    print("  -", d.type, d.name, "use:", d.use)
for d in prefs.devices:
    if d.type in ('CUDA', 'OPTIX', 'HIP', 'METAL', 'ONEAPI'):
        d.use = True
prefs.compute_device_type = 'CUDA'

scene = bpy.context.scene
scene.render.engine = 'CYCLES'
scene.cycles.device = 'GPU'
scene.cycles.samples = 32
scene.cycles.use_denoising = True
scene.render.resolution_x = 1280
scene.render.resolution_y = 720
cam = bpy.data.objects['Cam_front']
cam.location = (0.0, -9.5, 1.0)
scene.camera = cam
scene.render.filepath = '/content/kade_gpu_front32.png'
print("ENGINE:", scene.render.engine, "| DEVICE:", scene.cycles.device)
print("RESOLUTION:", scene.render.resolution_x, "x", scene.render.resolution_y)
print("SAMPLES:", scene.cycles.samples)
print("CAMERA:", scene.camera.name, tuple(round(v, 2) for v in scene.camera.location))
t0 = time.time()
bpy.ops.render.render(animation=False, write_still=True)
print("RENDER DONE in %.1f s ->" % (time.time() - t0), scene.render.filepath)
