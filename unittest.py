from abaqus import *  # type: ignore
from abaqusConstants import *   # type: ignore
import regionToolset  # type: ignore
import os
from typing import List

# abaqus related modules
modules = ['sketch', 'part', 'material', 'assembly'
           'mesh']
for module in modules:
    # easier way of importing multiple modules at the same time.
    globals()[module] = __import__(module)

# changing current directory to that of the source code

# get file path of current file
current_working_dir = os.path.dirname(os.path.abspath(__file__))
# change file path
os.chdir(current_working_dir)
# we going to create a logging module to print the current file path to, using decorators!



class Unittest(object):
    """
        Python class for defining unittests for Abaqus Simulation.
        -> This class will define create different models, loads, boundary conditions
        -> Provide visualization of the unit testing process
        -> provide logging ability
        -> compare with analytical solution
        -> plot grapths and provide a document of the unit tests conducted.
        -> more functions to be added
    """

    def __init__(self,
                model_name: str = 'model',
                material_name: str = 'material',
                density: float = 7872,  # default AISI 1005 Steel
                modulus: float = 200E9,
                poisson_ratio: float = 0.29,
                nlgeom: bool = False,   # this is off by default
                initialInc: float = 0.1,
                maxInc: float = 0.1,
                minInc: float = 1e-05,
                maxNumInc: int = 100,
                # this has a default value of stress, strain, displacement, reaction
                field_outputs: List[str] = ("S", "E", "U", "RF"),
                geom_coords: List[float] = (0.0, 0.0, 1.0, 1.0, 1.0),   # x1, y1, x2, y2, z
                boundary_coords: List[float] = (0.0, 0.5, 0.5),  # these are default values
                # fixed in x, free in y, fixed in z-direction (prevent out of plane movement)
                boundary_constraints: List[float] = (0.0, UNSET, 0.0),  # type: ignore
                displacement_coords: List[float] = (1.0, 0.5, 0.5),
                # displacement controlled
                # 0.1 mm displacement in the X-direction
                # No constrain in the Y-direction (free to deform)
                # No constraint in the Z-direction (free to expand or contract)
                displacement_constraints: List[float] = (0.001, UNSET, UNSET),  # type: ignore
                mesh_type: str = 'C3D8R',
                mesh_size: float = 1.0,
                mesh_deviation_factor: float = 0.1
                ):
        
        # user provided variables, some are optional or have default values.

        self.model_name: str = model_name
        self.material_name: str = material_name
        self.density: float = density
        self.modulus: float = modulus
        self.poisson_ratio: float = poisson_ratio
        self.nlgeom: bool = nlgeom
        self.initialInc: float = initialInc
        self.maxInc: float = maxInc
        self.minInc: float = minInc
        self.maxNumInc: float = maxNumInc
        self.field_outputs: List[str] = field_outputs
        self.geom_coords: List[float] = geom_coords
        self.boundary_coords: List[float] = boundary_coords
        self.boundary_constraints: List[float] = boundary_constraints
        self.displacement_coords: List[float] = displacement_coords
        self.displacement_constraints: List[float] = displacement_constraints
        self.mesh_type: str = mesh_type
        self.mesh_size: float = mesh_size
        self.mesh_deviation_factor: float = mesh_deviation_factor,

        # internal variables
        self._part_name: str = self.model_name + '_Part'  # partName
        self._sketch_name: str = self.model_name + '_Sketch'  # sketchName
        self._section_name: str = self.model_name + '_Section'  # SectionName
        self._assembly_name: str = self.model_name + '_Instance'  # Assembly name
        self._fieldOutReqName: str = self.model_name + '_field_output_requests'
        self._amplitude_name: str = self.model_name + '_DisplacementAmp'
        self._step_name: str = self.model_name + '_Displacement_Step'
        self._step_description: str = self.model_name + '_Apply controlled displacement in this step'
        self._displacementBC_fixed_name: str = self.model_name + '_FixedFace'
        self._displacementBC_edge_name: str = self.model_name + '_DisplacementEdge'
        self._job_name = self.model_name + '_Job'
        self._job_description = self.model_name + '_Single element test'
        self._result_viewport = self.model_name + '_ResultsViewport'
        self._odb_name = self.model_name = '.odb'  # odb file extension
        self._sheet_size: float = 2.0

        def _run_unittest(self):
            mdb.models.changeKey(fromName='Model-1', toName=self.model_name)  # type: ignore
            myModel = mdb.models[self.model_name]  # type: ignore
            myPart = myModel.Part(
                name=self._part_name,
                dimensionality=THREE_D,  # type: ignore
                type=DEFORMABLE_BODY  # type: ignore
            )
            mySketch = myModel.ConstrainedSketch(
                name=self._sketch_name,
                sheetSize=self._sheet_size
            ) 
            mySketch.rectangle(
                # x1, y1, x2, y2
                point1=(geom_coords[0], geom_coords[1]),
                point2=(geom_coords[2], geom_coords[3])
            )
            myPart.BaseSolidExtrude(sketch=mySketch, depth=geom_coords[4])
            



        def _mesh_type_selector(self):
            '''
                This internal function allows us to choose a suitable mesh type from abaqus
            '''
            mesh_type = None
            if self.mesh_type == 'C3D8R':
                mesh_type = C3D8R  # type: ignore
            else:
                # raise an error and and to logger file
                raise ValueError(f'Incorrect mesh type.\nCheck mesh_type parameter.')


