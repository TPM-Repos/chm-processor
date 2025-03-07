Collapse All Expand All Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
ProjectDataTable Class Methods   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) : ProjectDataTable Class  
---  
  
Include Inherited Members    
Include Protected Members    


Glossary Item Box

For a list of all members of this type, see [ProjectDataTable members](topic4283.md).

# Public Methods

| Name| Description  
---|---|---  
Public Method| CreateObjRef|  (Inherited from System.MarshalByRefObject)  
Public Method| [Delete](topic4290.md)| Deletes the table from the project.   
Public Method| [GetCachedTableData](topic4292.md)| Gets the cached table data from the design master.   
Public Method| GetLifetimeService|  (Inherited from System.MarshalByRefObject)  
Public Method![static \(Shared in Visual Basic\)](dotnetimages/static.gif)| [GetName](topic4293.md)| Gets the invariant name of the table from a display name.   
Public Method![static \(Shared in Visual Basic\)](dotnetimages/static.gif)| [GetTableReferenceName](topic4295.md)| Converts a table display name to a reference name (how it would be used in rules).   
Public Method| [Refresh](topic4300.md)| Refreshes the data table by asking the provider to re-retrieve the data.   
Top

# Protected Methods

| Name| Description  
---|---|---  
Protected Method| [AssertInitialized](topic4288.md)| Throws an exception if the document hasn't been initialized.   
Protected Method| [AssertNotDeleted](topic4289.md)| Throws an exception if the document has been deleted.   
Protected Method| [DeleteCore](topic4291.md)| When overridden in a derived class, performs any clean-up necessary to delete the document from the project.   
Protected Method| [GetTableData](topic4294.md)|   
Protected Method| [InitializeExistingCore](topic4296.md)| When overridden in a derived class, performs initialization tasks relevant to an existing document, i.e. during project load.   
Protected Method| [InitializeNewCore](topic4297.md)| When overridden in a derived class, performs initialization tasks relevant to a newly created document.   
Protected Method| [IsNameValidCore](topic4298.md)| When overridden in a derived class, checks to see if the specified new name is a valid name for the given type of document.   
Protected Method| MemberwiseClone| Overloaded. (Inherited from System.MarshalByRefObject)  
Protected Method| [NotifyStoreRead](topic4299.md)| When overridden in a derived class, handles the store being read for the first time.   
Protected Method| [RefreshOnProjectLoad](topic4301.md)| Determines if the data table is to be refreshed each time the project is loaded.   
Top

# See Also

#### Reference

[ProjectDataTable Class](topic4282.md)   
[DriveWorks Namespace](topic2159.md)


