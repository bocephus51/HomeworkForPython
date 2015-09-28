#
#
inFeatures = "parks"
>>> templayer = "parksLYR"
>>> expression = arcpy.AddFieldDelimiters(inFeatures, "PARK_TYPE") + " <> ' ' "
>>> outFeatureClass = "P:/Fall2015/PythonProgramming/Exercise05/parkslayer_dissolved"
>>> dissolveFields = ["PARK_TYPE"]
>>> arcpy.MakeFeatureLayer_management(inFeatures, templayer)
<Result 'parksLYR'>
