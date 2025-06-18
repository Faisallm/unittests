from abaqus import *
from abaqusConstants import *
import regionToolset  #type:ignore

# blank out the current viewport
session.viewports["Viewport: 1"].setValues(displayedObject=None)

# renaming the default model
# 1: name we want to name our model
mdb.models.changeKey(fromName="Model-1", toName="SingleElementModel")
myModel = mdb.models['SingleElementModel']

# create the part
import sketch  #type:ignore
import part

cubePart = myModel.Part(
    # internal variables(_): we will be adding (_) to the  
    name="SingleElementCube",
    dimensionality=THREE_D,
    type=DEFORMABLE_BODY
)
# creating a sketchpad
cubeSketch = myModel.ConstrainedSketch(
    # internal variable
    name="cubeSketch",
    # doesn't really matter, since we are not viewing it
    sheetSize=2.0
)

# 2: dimensions of the model, # default values available
# x1:1, x2:1, y1:1, y2:1, z:1
cubeSketch.rectangle(
    point1=(0.0, 0.0),
    point2=(1.0, 1.0)
)

# this creates a feature object by calling the BaseShell() method.
# 1 x 1 x 1
cubePart.BaseSolidExtrude(sketch=cubeSketch, depth=1.0)

import material  # type: ignore

cubeMaterial = myModel.Material(
    # 3) name of our material
    name="AISI 1005 Steel"
)

# 4, density, modulus, poisson ratio
cubeMaterial.Density(table=((7872, ), ))
cubeMaterial.Elastic(table=((200E9, 0.29), ))

# Create solid sections and make section assignments

# HomogeneousShellSection object
# (we don't need to create this, maybe!)
plateSection = myModel.HomogeneousSolidSection(
    # internal variable (_): this should take the model name and add + '_section:str' to it
    name='cubeSection',
    # this would reference the material name in str
    material="AISI 1005 Steel"
)

# assign section to the entire cube
cube_region = regionToolset.Region(cells=cubePart.cells)
cubePart.SectionAssignment(
    region=cube_region,
    sectionName="cubeSection"
)

# create an assembly
import assembly  # type: ignore

cubeAssembly = myModel.rootAssembly
cubeAssembly.regenerate()  # recommended for stability
cubeInstance = cubeAssembly.Instance(
    # internal variable (_): we will add + '_Instance' to model name
    name="cubeInstance",
    part=cubePart,
    dependent=ON
)


# create step
myModel.StaticStep(
    # internal variable: to be defined as 'displacement step'
    name="Displacement Step",
    previous="Initial",
    # internal variable: to be defined as: 'Apply controlled displacement in this step'
    description="Apply controlled displacement in this step",
    # default values, can be modified by users
    nlgeom=OFF,
    initialInc=0.1,
    maxInc=0.1,
    minInc=1e-05,
    maxNumInc=100
)

# create the field output requests
myModel.fieldOutputRequests.changeKey(
    fromName="F-Output-1",
    toName="Output Stresses and Displacements"
)

# fields to be outputted in our field output requests.
myModel.fieldOutputRequests["Output Stresses and Displacements"] \
    .setValues(variables=("S", "E", "U", "RF"))  # stress, strain, displacement, reaction

# delete history output requests because we are not using it
del myModel.historyOutputRequests['H-Output-1']

# Applying boundary conditions
fixed_face = cubeInstance.faces.findAt(((0.0, 0.5, 0.5),))
fixed_region = regionToolset.Region(faces=fixed_face)

myModel.DisplacementBC(
    name="FixedFace",
    # the step where the displacement BC is applied
    createStepName="Initial",
    # where we are applying the displacement BC.
    region=fixed_region,
    u1=0.0,  # Fixed in X-direction
    u2=UNSET,  # Free in Y-direction
    u3=0.0,  # Fixed in Z-direction (prevent out-of-plane movement)
    # uniform distribution of boundary condition at the region.
    distributionType=UNIFORM
)




# applying displacement to right edge at (X=5)
displaced_face = cubeInstance.faces.findAt(((1.0, 0.5, 0.5),))
displaced_region = regionToolset.Region(faces=displaced_face)

# define amplitude for smooth displacement application
myModel.TabularAmplitude(
    name='DisplacementAmp',
    timeSpan=STEP,
    # this helps with numerical stability and mimics quasi-static loading.
    data=((0.0, 0.0), (1.0, 1.0))
)

myModel.DisplacementBC(
    name="DisplacementEdge",
    createStepName="Displacement Step",
    region=displaced_region,
    u1=0.001,  # 0.1 mm displacement in X-direction
    u2=UNSET,  # No constraint in the Y-direction (free to deform)
    u3=UNSET,   # No constraint in the Z-direction (free to expand or contract)
    amplitude="DisplacementAmp",
    distributionType=UNIFORM,
    localCsys=None
)

# mesh our domain and region
import mesh

# region of the plate.
cube_mesh_region = cube_region
# defining the type of element.
elemType1 = mesh.ElemType(
    elemCode=C3D8R,
    elemLibrary=STANDARD
)

cubePart.setElementType(
    regions=cube_mesh_region,
    elemTypes=(elemType1,)
)

cubePart.seedPart(
    size=1,
    deviationFactor=0.1
)

cubePart.generateMesh()


# create and run the job
import job  # type:ignore

mdb.Job(
    name='SingleElementJob',
    model="SingleElementModel",
    type=ANALYSIS,
    description="Single element test"
)

mdb.jobs['SingleElementJob'].submit(consistencyChecking=OFF)
mdb.jobs['SingleElementJob'].waitForCompletion()

# Display results
import visualization
import time
import os

resultsViewport = session.Viewport(name='ResultsViewport')

odbPath = "SingleElementJob.odb"

while not os.path.exists(odbPath):
    time.sleep(1)

odb = session.openOdb(name=odbPath)
resultsViewport.setValues(displayedObject=odb)
resultsViewport.odbDisplay.display.setValues(plotState=(CONTOURS_ON_DEF,))



