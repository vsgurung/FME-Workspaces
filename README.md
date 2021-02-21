 # FME-Workspace

SQL Server does creates spatial index automatically however the bounding box coordinates needs to be typed in manually. A FME workspace has been created for creating spatial index. First workspace loads the data into sql server database and the second workspace (which creates the spatial index) runs after the translation is complete.

runfmeworkspace.py is the python shutdown script in the workspace loading data into SQL Server. This script calls the FME workspace and creates spatial index.

# 20 Feb 2021
Added more workspaces. These FME workbench uses REST API provided by the organisation to download data. The data that can be downloaded are:
* Special Area of Conservation
* Special Protection Areas
* Sites of Special Scientific Interest.
* Nitrate Vulnerable Zones 2021.
* Felling Licence Application

# 21 Feb 2021
Updated the FME workbenches added on 20 Feb 2021. The workbenches now contain private parameters populated by Python script. The parameters are SRID, xmin, xmax, ymin & ymax. These are used while in setting the coordinate system and X, Y extents while creating table in Oracle database.
