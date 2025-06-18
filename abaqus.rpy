# -*- coding: mbcs -*-
#
# Abaqus/Viewer Release 2024 replay file
# Internal Version: 2023_09_21-08.55.25 RELr426 190762
# Run by Faisal on Wed Jun 18 11:10:15 2025
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
execfile('test.py', __main__.__dict__)
#* ImportError: No module named 'regionToolset'
#* File "test.py", line 6, in <module>
#*     import regionToolset
