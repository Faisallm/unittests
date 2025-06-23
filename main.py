from abaqus import *  # type: ignore
from abaqusConstants import *   # type: ignore
import regionToolset  # type: ignore
import os
import time
import sys
from typing import List, Any, Tuple
import assembly  # type: ignore

# abaqus related modules
modules = ['sketch', 'part', 'material',
            'step', 'mesh', 'job', 'visualization']
for module in modules:
    # easier way of importing multiple modules at the same time.
    globals()[module] = __import__(module)

# changing current directory to that of the source code

# get file path of current file
current_working_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
# change file path
# os.chdir(current_working_dir)
os.chdir(r'C:\Users\Faisal\Desktop\unittests')
# we going to create a logging module to print the current file path to, using decorators!

print(f"Running with __name__ = {__name__}")
print(f"Arguments: {sys.argv}")


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
                model_name: str = 'Model',
                material_name: str = 'smp-10',
                density: float = 1.2e-9,  # default AISI 1005 Steel
                modulus: float = 2500,
                poisson_ratio: float = 0.35,
                nlgeom: bool = False,   # this is off by default
                initialInc: float = 60.0,
                maxInc: float = 1000000,
                minInc: float = 1e-6,
                deltmx: float = 10.0,
                maxNumInc: int = 100,
                # this has a default value of stress, strain, displacement, reaction
                field_outputs: Tuple[str] = ("S", "E", "U", "RF"),
                geom_coords: Tuple[float] = (0.0, 0.0, 1.0, 1.0, 1.0),   # x1, y1, x2, y2, z
                boundary_coords: Tuple[float] = (0.0, 0.5, 0.5),  # these are default values
                # fixed in x, free in y, fixed in z-direction (prevent out of plane movement)
                boundary_constraints: Tuple[Any] = (0.0, UNSET, 0.0),  # type: ignore
                displacement_coords: Tuple[float] = (1.0, 0.5, 0.5),
                # displacement controlled
                # 0.1 mm displacement in the X-direction
                # No constrain in the Y-direction (free to deform)
                # No constraint in the Z-direction (free to expand or contract)
                displacement_constraints: Tuple[Any] = (0.1, UNSET, UNSET),  # type: ignore
                mesh_type: str = 'C3D8RT',
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
        self.field_outputs: Tuple[str] = field_outputs
        self.geom_coords: Tuple[float] = geom_coords
        self.boundary_coords: Tuple[float] = boundary_coords
        self.boundary_constraints: Tuple[Any] = boundary_constraints
        self.displacement_coords: Tuple[float] = displacement_coords
        self.displacement_constraints: Tuple[Any] = displacement_constraints
        self.mesh_type: str = mesh_type
        self.mesh_size: float = mesh_size
        self.mesh_deviation_factor: float = mesh_deviation_factor

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
        self._odb_name = self.model_name + '.odb'  # odb file extension
        self._sheet_size: float = 2.0

    # extrude the depth, the 3D component
    def _mesh_type_selector(self):
        '''
            This internal function allows us to choose a suitable mesh type from abaqus
        '''
        mesh_type = None
        if self.mesh_type == 'C3D8RT':
            mesh_type = C3D8RT  # type: ignore
        else:
            # raise an error and and to logger file
            raise ValueError(f'Incorrect mesh type.\nCheck mesh_type parameter.')
        return mesh_type

    # create the model
    def _create_model(self):
        """This internal function creates or accesses a model in Abaqus."""
        # Check if model already exists
        if self.model_name in mdb.models.keys():  # type: ignore
            return mdb.models[self.model_name]  # type: ignore
        print(f'model name: {self.model_name}')
        # Create new model if it doesn't exist
        mdb.models.changeKey(fromName="Model-1", toName=str(self.model_name))  # type: ignore
        myModel = mdb.models[self.model_name]  # type: ignore
        return myModel 
    
    # create the part
    def _create_part(self, myModel: object) -> object:
        """
            This internal function creates the part and the sketch.
        """
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
            point1=tuple(self.geom_coords[:2]),
            point2=tuple(self.geom_coords[2:4]) 
        )
        myPart.BaseSolidExtrude(sketch=mySketch, depth=self.geom_coords[4])

        return myPart
    
    # define material properties
    # the Any type is their because my lazy ass don't know the return type
    def _define_material(self, myModel: object) -> Any:
        """This internal defines the material properties in our model"""

        myMaterial = myModel.Material(
            name=self.material_name,
        )
        myMaterial.Density(table=((self.density, ), ))
        myMaterial.Elastic(table=((self.modulus, self.poisson_ratio), ))

        # Thermal properties (required for CoupledTempDisplacementStep)
        # myMaterial.SpecificHeat(table=((1800.0,),))              # J/kg·K
        # myMaterial.Conductivity(table=((0.2,),))                # W/m·K
        # myMaterial.Expansion(table=((150e-6,),), type=ISOTROPIC)      # type: ignore # 1/K, isotropic  
        myMaterial.SpecificHeat(table=((1000.0,),))  # J/kg-K (example)
        myMaterial.Conductivity(table=((0.5,),))    # W/m-K (example)
        myMaterial.Depvar(n=30)  # State variables

        # UMAT for shape memory effects (critical!)
        # myMaterial.UserMaterial(
        #     mechanicalConstants=(2500, 0.35),  # E, ν (glassy state)
        #     thermalConstants=(),           # Tg (°C) (example: 60°C)
        #     type=THERMOMECHANICAL  # type: ignore
        # )

        return myMaterial
    
    def _create_section(self, myModel: object, myPart: object) -> Any:
        """
            This internal function defines and returns the section.
        """
        mySection = myModel.HomogeneousSolidSection(
            name=self._section_name,
            material=self.material_name
        )
        mySection_region = regionToolset.Region(cells=myPart.cells)
        myPart.SectionAssignment(
            region=mySection_region,
            sectionName=self._section_name
        )
        return mySection
    
    def _create_assembly(self, myModel: object, myPart: object) -> object:
        """
            This internal function defines and returns the assembly.
        """
        myAssembly = myModel.rootAssembly
        myAssembly.regenerate()  # recommended for stability
        myInstance = myAssembly.Instance(
            # internal variable (_): we will add + '_Instance' to model name
            name=self._assembly_name,
            part=myPart,
            dependent=ON  # type: ignore
        )
        return myInstance
    
    def _create_step(self, myModel: object) -> None:
        """
            This creates the steps of the simulation.
            Definitions: 
                (1) A step is a period of time during which the analysis...
                proceeds under a specified set of conditions.

                (2) It defines a phase in the simulation where the loading...
                boundary conditions, and analysis procedure remains consistent.
        """

        # old code, I was using this before adding temperature constraints
        # myModel.StaticStep(
        #     name=self._step_name,
        #     previous='Initial',  # this should not be changed!, Abaqus default
        #     description=self._step_description
        # )

        myModel.CoupledTempDisplacementStep(
            name=self._step_name,
            previous='Initial',
            description=self._step_description,
            timePeriod=34800.0,  # my simulation time 
            maxNumInc=1000000,
            initialInc=60.0,
            minInc=1e-6,
            deltmx=10.0,
            nlgeom=OFF    # type: ignore  # or ON if you need geometric nonlinearity
        )

    def _define_field_output_requests(self, myModel: object) -> None:
        """
            This internal function defines field output requests.
            This is like a subroutine in fortran, it isn't a pure function.
        """

        myModel.fieldOutputRequests.changeKey(
            fromName='F-Output-1',
            toName=self._fieldOutReqName
        )
        myModel.fieldOutputRequests[str(self._fieldOutReqName)] \
            .setValues(variables=self.field_outputs)
        
    def _define_history_output_requests(self, myModel: object) -> None:
        """
            This defines history output requests.
        """
        myModel.HistoryOutputRequest(
            name='Default History Outputs',
            createStepName=self._step_name,
            variables=PRESELECT  # type: ignore
        )

        # deleting the old history output
        del myModel.historyOutputRequests['H-Output-1']

    def _apply_BC(self, myModel: object, myInstance: object) -> None:
        """
            This applies the displacement boundary condition. 
            The displacement constraints.
        """
        # the face we will be applying the constraints to
        fixed_face = myInstance.faces.findAt((self.boundary_coords,))

        # region
        fixed_region = regionToolset.Region(faces=fixed_face)

        u1, u2, u3 = self.boundary_constraints

        myModel.DisplacementBC(
            name=self._displacementBC_fixed_name,
            createStepName="Initial",
            region=fixed_region,
            u1=u1,
            u2=u2,
            u3=u3,
            distributionType=UNIFORM  # type: ignore
        )

    def _apply_temp_bc(self, myModel: object, myInstance: object) -> None:
        """
            This applies an initial temperature boundary condition.
        """
        all_nodes = myModel.rootAssembly.instances[self._assembly_name].nodes
        print(f"Number of nodes in instance: {len(all_nodes)}")  # Debug print
        myModel.rootAssembly.Set(name='ALLNODESSET', nodes=all_nodes)
        myModel.rootAssembly.regenerate()  # ensure it’s updated

        all_nodes_region = myModel.rootAssembly.sets['ALLNODESSET']

        myModel.TemperatureBC(
            name='TempBC',
            createStepName=self._step_name,
            region=all_nodes_region,
            magnitude=20.0,
            amplitude=self._amplitude_name,
            distributionType=UNIFORM,  # type: ignore
            fixed=OFF  # type: ignore
        )

    def _apply_pressure(self, myModel: object, myInstance: object) -> None:
        """
            Apply pressure boundary conditions.
        """
        # finding the face to apply the pressure
        displaced_face = myInstance.faces.findAt(((self.displacement_coords),))
        # volumetric region
        displaced_region = regionToolset.Region(faces=displaced_face)

        # define amplitude for smooth displacement application
        myModel.TabularAmplitude(
            name=self._amplitude_name,
            timeSpan=STEP,  # type: ignore
            data=((0, 20), (13800, 250), (21000, 250), (34800, 20))
        )

        u1, u2, u3 = self.displacement_constraints

        myModel.DisplacementBC(
            name=self._displacementBC_edge_name,
            createStepName=self._step_name,
            region=displaced_region,
            u1=u1,
            u2=u2,
            u3=u3,
            amplitude=self._amplitude_name,
            distributionType=UNIFORM,  # type: ignore
            localCsys=None
        )


    def _generate_mesh(self, 
                        myPart: object, 
                        mesh_type) -> None:
        """
            Generates mesh on part.
        """

        part_region= regionToolset.Region(cells=myPart.cells)
        elemType1 = mesh.ElemType(  # type: ignore
            elemCode=mesh_type,
            elemLibrary=STANDARD  # type: ignore
        )
        myPart.setElementType(
            regions=part_region,
            elemTypes=(elemType1,)
        )
        # print(f'mesh deviation factor: {self.mesh_deviation_factor[0]}')
        myPart.seedPart(
            size=self.mesh_size,
            deviationFactor=self.mesh_deviation_factor
        )
        # generate mesh
        myPart.generateMesh()

    def _run_job(self) -> Any:
        """
            This internal function runs the job.
        """

        mdb.Job(  # type: ignore
            name=self._job_name,
            model=self.model_name,
            type=ANALYSIS,  # type: ignore
            description=self._job_description
        )  
        mdb.jobs[self._job_name].submit(consistencyChecking=OFF)  # type: ignore
        mdb.jobs[self._job_name].waitForCompletion()  # type: ignore

    def _visualize_results(self) -> Any:
        """
            Visualize results.
        """
        resultsViewport = session.Viewport(name='ResultsViewport')  # type: ignore
        odbPath = self._job_name + '.odb'
        while not os.path.exists(odbPath):
            time.sleep(1)
        odb = session.openOdb(name=odbPath)  # type: ignore
        resultsViewport.setValues(displayedObject=odb)
        resultsViewport.odbDisplay.display.setValues(plotState=(CONTOURS_ON_DEF,))  # type: ignore


    def run_unittest(self):
        """
            Creates and runs the unittest.
        """

        # create model
        myModel = self._create_model()
        # create part
        myPart = self._create_part(myModel=myModel)
        # define material
        self._define_material(myModel)
        # create section
        self._create_section(myModel=myModel, myPart=myPart)
        # create assembly
        myInstance = self._create_assembly(myModel=myModel, myPart=myPart)
        # create step
        self._create_step(myModel=myModel)
        # define field output requests
        self._define_field_output_requests(myModel=myModel)
        # define history output requests
        self._define_history_output_requests(myModel=myModel)
        mesh_type = self._mesh_type_selector()
        # generate mesh
        self._generate_mesh(myPart=myPart, mesh_type=mesh_type)

        # apply displacement boundary condition
        self._apply_BC(myModel=myModel, myInstance=myInstance)
        # apply pressure
        self._apply_pressure(myModel=myModel, myInstance=myInstance)
        # regenerate after mesh to activate nodes
        myModel.rootAssembly.regenerate()
        # apply temperature
        self._apply_temp_bc(myModel=myModel, myInstance=myInstance)

        # write input file BEFORE running the job
        myJob = mdb.Job(  # type: ignore
            name=self.model_name,
            model=myModel.name
        )
        myJob.writeInput()
        # _run job
        self._run_job()
        # produce odb output (visualization)
        self._visualize_results()
        myJob = mdb.Job(  # type: ignore
            name=self.model_name,
            model=myModel.name
        )


# Single element method

# obj = Unittest(model_name='SingleElementModel')


# nine (9) element method
# obj = Unittest(
#     model_name='NineElement',
#     geom_coords=(0.0, 0.0, 3.0, 3.0, 1.0),
#     boundary_coords=(0.0, 1.5, 0.5),
#     displacement_coords=(3.0, 1.5, 0.5)
# )

# 27 elements
obj = Unittest(model_name='twenty_seven',
               mesh_size=1.0/3.0)
obj.run_unittest()