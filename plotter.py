# abaqus viewer script
from odbAccess import openOdb
import matplotlib.pyplot as plt
import numpy as np
import os

# --- USER INPUTS ---
odb_path = 'twenty_seven_Job.odb'  # Change to your ODB filename if different
step_name = 'twenty_seven_Displacement_Step'  # Your simulation step
frame_index = -1  # Use -1 for last frame
output_variable = 'U'  # 'U' = displacement, 'S' = stress, etc.

# --- LOAD ODB ---
if not os.path.exists(odb_path):
    raise FileNotFoundError(f"ODB file not found: {odb_path}")

odb = openOdb(name=odb_path)
step = odb.steps[step_name]
frame = step.frames[frame_index]

# --- GET INSTANCE NAME ---
instance_name = list(odb.rootAssembly.instances.keys())[0]  # assumes only 1 instance
instance = odb.rootAssembly.instances[instance_name]

# --- EXTRACT FIELD OUTPUT ---
field = frame.fieldOutputs[output_variable]
field_data = field.getSubset(region=instance, position=NODAL)

# Store node labels and magnitudes
node_labels = []
magnitudes = []

for v in field_data.values:
    node_labels.append(v.nodeLabel)
    if output_variable == 'U':  # displacement
        magnitudes.append(np.linalg.norm(v.data))  # magnitude of displacement vector
    elif output_variable == 'S':  # stress
        magnitudes.append(v.mises)  # von Mises stress

# --- PLOT ---
plt.figure(figsize=(8, 4))
plt.plot(node_labels, magnitudes, 'o-', markersize=4)
plt.title(f"{output_variable} Magnitude per Node")
plt.xlabel("Node Label")
plt.ylabel("Magnitude")
plt.grid(True)
plt.tight_layout()
plt.show()

odb.close()
