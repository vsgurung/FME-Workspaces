# FME-Workspace

SQL Server does not create spatial index of geometry type automatically. Create two workspace for the purpose. First workspace loads the data into sql server database and the second workspace (which creates the spatial index) runs after the translation is complete.
