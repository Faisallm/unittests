# imports all abaqus modules and creates reference to all public
# objects defined by that module.
# objects like mdb and session
from abaqus import *
from abaqusConstants import *
import regionToolset

# emptying my display viewpoint
session.viewports['Viewport: 1'].setValues(displayedObject=None)

# create the model
mdb.models.changeKey(fromName='Model-1', toName="Cantilever Beam")
beamModel = mdb.models['Cantilever Beam']

# sketching the beam using a rectangular tool
import sketch
import part

# sketching the beam cross-section using rectangular tool
beamProfileSketch = beamModel.ConstrainedSketch(
    name='Beam CS Profile',
    sheetSize=5
)
beamProfileSketch.rectangle(
    point1=(0.1, 0.1),
    point2=(0.3, -0.1)
)

# creating a 3D deformable part from the sketch
beamPart = beamModel.Part(
    name='Beam',
    # THREE_D: 3D (from abaqusConstants), DEFORMABLE_BODY
    dimensionality=THREE_D,
    type=DEFORMABLE_BODY
)

beamPart.BaseSolidExtrude(
    sketch=beamProfileSketch,
    # this is akin to the z-direction
    depth=5
)

# defining the materials
import material

# so we can create multiple materials with this
beamMaterial = beamModel.Material(
    name='AISI 1005 Steel'
)

# here, our density is not temperature dependent
# (density1, temperature1), (density2, temperature2), (density3, temperature3)
beamMaterial.Density(table=((7872, ), ))
beamMaterial.Elastic(table=((200E9, 0.29), ))

# Create a solid section and apply the beam to it
import section

beamSection = beamModel.HomogeneousSolidSection(
    # section name
    name='Beam Section',
    # this should match our material name
    material='AISI 1005 Steel'
)

# assign the beam to this section

# assigning all the cells to this section
# combining part, material, section into one

# the cell object defines the volumetric regions of a geometry
beam_region = (beamPart.cells,)
beamPart.SectionAssignment(
    region=beam_region,
    sectionName='Beam Section'
)

# create the assembly

import assembly

beamAssembly = beamModel.rootAssembly  # to avoid beamModel.rootAssembly.Instance
# we use the assembly to find where to apply our loads
beamInstance = beamAssembly.Instance(
    name='Beam Instance',
    part=beamPart,
    # Dependent (mesh on part)
    # ON is gotten from abaqusConstants
    dependent=ON
)


# Create the Step

# (a step is a period of time during which the analysis 
# proceeds under a specified set of conditions).

# It defines a phase in the simulation where the loading...
# boundary conditions, and analysis procedure remains consistent.

import step

beamModel.StaticStep(
    name='Apply Load',
    previous='Initial',
    description='Load is applied during this step'
)

# create and define the field output request
beamModel.fieldOutputRequests.changeKey(
    fromName='F-Output-1',
    toName='Selected Field Outputs'
)

# properties we want to include in our field output request.

beamModel.fieldOutputRequests['Selected Field Outputs'] \
    .setValues(variables=('S', 'E', 'PEMAG', 'U', 'RF', 'CF'))

# create and define history output requests
beamModel.HistoryOutputRequest(
    name='Default History Outputs',
    createStepName='Apply Load',
    # leaving the defaults
    variables=PRESELECT
)

del beamModel.historyOutputRequests['H-Output-1']


# apply load
# x, Y, and Z coordinates of a point on the top surface of the beam to variables.
top_face_pt_x = 0.2
top_face_pt_y = 0.1
top_face_pt_z = 2.5
top_face_pt = (top_face_pt_x, top_face_pt_y, top_face_pt_z)   # (0.2, 0.1, 2.5)

# The face on which that point lies is the face we are looking at
# -> findAt() method finds a face that is at that point or at a 
# distance less than 1E-6 from it.
# the point should not be shared by more than one face because...
# the model will return the first face it encounters.
top_face = beamInstance.faces.findAt((top_face_pt,))

# we extract the region of the face choosing which direction its normal points in
# the region object can accept faces, edges, vertices, and so on.
# if we had written ,side2Faces=top_face, the normal to our region...
# will be pointed into the beam rather than out of it.
top_face_region = regionToolset.Region(side1Faces=top_face)

# applying pressur to the top face region.
beamModel.Pressure(
    name='Uniform Applied Pressure',
    # the step where we are applying the pressure.
    createStepName='Apply Load',
    region=top_face_region,
    # UNIFORM is the default value
    distributionType=UNIFORM,
    magnitude=10,
    # UNSET is the default value.
    amplitude=UNSET
)

# applying constraints
fixed_end_face_pt_x = 0.2
fixed_end_face_pt_y = 0
fixed_end_face_pt_z = 0
fixed_end_face_pt = (fixed_end_face_pt_x, fixed_end_face_pt_y, fixed_end_face_pt_z)

# finds the face
fixed_end_face = beamInstance.faces.findAt((fixed_end_face_pt,))

fixed_end_face_region = regionToolset.Region(faces=fixed_end_face)

# applying the constraints
beamModel.EncastreBC(
    name='Encaster one end',
    createStepName='Initial',
    region=fixed_end_face_region
)


# applying mesh
import mesh

# coordinates of the middle of the beam
beam_inside_xcoord = 0.2
beam_inside_ycoord = 0
beam_inside_zcoord = 2.5

# defining mesh type
elemType1 = mesh.ElemType(
    # this is the only required argument
    elemCode=C3D8R,
    elemLibrary=STANDARD,
    kinematicSplit=AVERAGE_STRAIN,
    secondOrderAccuracy=OFF,
    hourglassControl=DEFAULT,
    distortionControl=DEFAULT
)

# getting region where we are applying mesh
beamCells = beamPart.cells  # VOLUMETRIC REGION OF A GEOMETRY
selectedBeamCells = beamCells.findAt((beam_inside_xcoord, beam_inside_ycoord,
                                      beam_inside_zcoord),)
beamMeshRegion = (selectedBeamCells,)

# applying choosen mesh type to region.
beamPart.setElementType(
    regions=beamMeshRegion,
    elemTypes=(elemType1,)
)

beamPart.seedPart(
    # size of mesh
    size=0.01,
    # ratio of chordal deformation to the element length
    deviationFactor=0.1
)

# generate mesh
beamPart.generateMesh()


# creating and running the job
import job

mdb.Job(
    name='CantileverBeamJob',
    model='Cantilever Beam',
    type=ANALYSIS,
    explicitPrecision=SINGLE,
    nodalOutputPrecision=SINGLE,
    description='Job simulates a loaded cantilever beam',
    parallelizationMethodExplicit=DOMAIN,
    multiprocessingMode=DEFAULT,
    numDomains=1,
    userSubroutine='',
    numCpus=1,
    memory=50,
    memoryUnits=PERCENTAGE,
    scratch='',
    echoPrint=OFF,
    modelPrint=OFF,
    contactPrint=OFF,
    historyPrint=OFF
)

mdb.jobs['CantileverBeamJob'].submit(consistencyChecking=OFF)

mdb.jobs['CantileverBeamJob'].waitForCompletion()

# visualization

import visualization

beam_viewport = session.Viewport(name='Beam Resulst Viewport')
beam_Odb_Path = 'CantileverBeamJob.odb'
an_odb_object = session.openOdb(name=beam_Odb_Path)
beam_viewport.setValues(displayedObject=an_odb_object)
beam_viewport.odbDisplay.display.setValues(plotState=(DEFORMED, ))













