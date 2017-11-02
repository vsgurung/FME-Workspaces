 # FME-Workspace

SQL Server does creates spatial index automatically however the bounding box coordinates needs to be typed in manually. A FME workspace has been created for creating spatial index. First workspace loads the data into sql server database and the second workspace (which creates the spatial index) runs after the translation is complete.

runfmeworkspace.py is the python shutdown script in the workspace loading data into SQL Server. This script calls the FME workspace and creates spatial index.
