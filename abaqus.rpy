# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2024 replay file
# Internal Version: 2023_09_21-08.55.25 RELr426 190762
# Run by Faisal on Thu Jun 19 05:46:34 2025
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(1.5625, 1.5463), width=230, 
    height=153.393)
session.viewports['Viewport: 1'].makeCurrent()
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
execfile('main.py', __main__.__dict__)
#: Running with __name__ = __main__
#: Arguments: ['C:\\SIMULIA\\EstProducts\\2024\\win_b64\\code\\bin\\ABQcaeK.exe', '-cae', '-noGUI', 'main.py', '-tmpdir', 'C:\\Users\\Faisal\\AppData\\Local\\Temp', '-lmlog', 'ON']
#: model name: NineElement
#: mesh deviation factor: 0.1
#: Model: C:/SIMULIA/EstProducts/2024/win_b64/code/bin/NineElement_Job.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       1
#: Number of Node Sets:          1
#: Number of Steps:              1
print('RT script done')
#: RT script done
