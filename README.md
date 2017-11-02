 # FME-Workspace

SQL Server does not create spatial index of geometry type automatically. Created a separate workspace for creating spatial index. First workspace loads the data into sql server database and the second workspace (which creates the spatial index) runs after the translation is complete.

The second workspace is run by the Python shutdown script.
