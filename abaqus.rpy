# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2024 replay file
# Internal Version: 2023_09_21-08.55.25 RELr426 190762
# Run by Faisal on Thu Jun 19 04:02:44 2025
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
execfile('unittest.py', __main__.__dict__)
#* AttributeError: 'Unittest' object has no attribute 'run_unittest'
#* File "unittest.py", line 370, in <module>
#*     obj.run_unittest()
