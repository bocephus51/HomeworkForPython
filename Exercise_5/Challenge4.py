import arcpy
from arcpy import env
env.workspace = "P:/Fall2015/PythonProgramming"
if arcpy.CheckExtension("3D") == "Available" and arcpy.CheckExtension("Spatial") == "Available" and arcpy.CheckExtension("Network") == "Available":
    print "The following extensions are available: 3D, Spatial and Network"
elif arcpy.CheckExtension("3D") == "Unavailable" and arcpy.CheckExtension("Spatial") == "Unavailable" and arcpy.CheckExtension("Network") == "Unavailable":
    print "Unavailable"
