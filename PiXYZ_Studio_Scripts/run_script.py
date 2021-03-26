from PiXYZ_Studio_Scripts.demoBatch import processDirectory
input_dir  = "U:/dloveridge/_User_Examples/bmerva/Whirlpool/QRefresh_Stl"
output_dir = "U:/dloveridge/_User_Examples/bmerva/Whirlpool/QRefresh_Fbx"
processDirectory(input_dir, ["stp"], output_dir, ["fbx"])