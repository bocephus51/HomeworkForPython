import arcpy
from arcpy import env
env.workspace = "P:/Fall2015/PythonProgramming/Exercise07/Exercise07data"
fc = "Results/raods.shp"
newfield = "FERRY"
fieldtype = "TEXT"
fieldname = arcpy.ValidateFieldName(newfield)
fieldlist = arcpy.ListFields(fc)
fieldnames = []
for field in fieldlist:
    if field = "FERRY":
        print "Yes"
    else:
        print "No"
