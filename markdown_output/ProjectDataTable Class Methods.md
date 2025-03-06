![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
ProjectDataTable Class Methods   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic4282.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) : ProjectDataTable Class  
---  
  
Include Inherited Members    
Include Protected Members    


Glossary Item Box

For a list of all members of this type, see [ProjectDataTable members](topic4283.md).

# ![](dotnetimages/collapse.gif)Public Methods

| Name| Description  
---|---|---  
![Public Method](dotnetimages/publicMethod.gif)| CreateObjRef|  (Inherited from System.MarshalByRefObject)  
![Public Method](dotnetimages/publicMethod.gif)| [Delete](topic4290.md)| Deletes the table from the project.   
![Public Method](dotnetimages/publicMethod.gif)| [GetCachedTableData](topic4292.md)| Gets the cached table data from the design master.   
![Public Method](dotnetimages/publicMethod.gif)| GetLifetimeService|  (Inherited from System.MarshalByRefObject)  
![Public Method](dotnetimages/publicMethod.gif)![static \(Shared in Visual Basic\)](dotnetimages/static.gif)| [GetName](topic4293.md)| Gets the invariant name of the table from a display name.   
![Public Method](dotnetimages/publicMethod.gif)![static \(Shared in Visual Basic\)](dotnetimages/static.gif)| [GetTableReferenceName](topic4295.md)| Converts a table display name to a reference name (how it would be used in rules).   
![Public Method](dotnetimages/publicMethod.gif)| [Refresh](topic4300.md)| Refreshes the data table by asking the provider to re-retrieve the data.   
Top

# ![](dotnetimages/collapse.gif)Protected Methods

| Name| Description  
---|---|---  
![Protected Method](dotnetimages/protectedMethod.gif)| [AssertInitialized](topic4288.md)| Throws an exception if the document hasn't been initialized.   
![Protected Method](dotnetimages/protectedMethod.gif)| [AssertNotDeleted](topic4289.md)| Throws an exception if the document has been deleted.   
![Protected Method](dotnetimages/protectedMethod.gif)| [DeleteCore](topic4291.md)| When overridden in a derived class, performs any clean-up necessary to delete the document from the project.   
![Protected Method](dotnetimages/protectedMethod.gif)| [GetTableData](topic4294.md)|   
![Protected Method](dotnetimages/protectedMethod.gif)| [InitializeExistingCore](topic4296.md)| When overridden in a derived class, performs initialization tasks relevant to an existing document, i.e. during project load.   
![Protected Method](dotnetimages/protectedMethod.gif)| [InitializeNewCore](topic4297.md)| When overridden in a derived class, performs initialization tasks relevant to a newly created document.   
![Protected Method](dotnetimages/protectedMethod.gif)| [IsNameValidCore](topic4298.md)| When overridden in a derived class, checks to see if the specified new name is a valid name for the given type of document.   
![Protected Method](dotnetimages/protectedMethod.gif)| MemberwiseClone| Overloaded. (Inherited from System.MarshalByRefObject)  
![Protected Method](dotnetimages/protectedMethod.gif)| [NotifyStoreRead](topic4299.md)| When overridden in a derived class, handles the store being read for the first time.   
![Protected Method](dotnetimages/protectedMethod.gif)| [RefreshOnProjectLoad](topic4301.md)| Determines if the data table is to be refreshed each time the project is loaded.   
Top

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectDataTable Class](topic4282.md)   
[DriveWorks Namespace](topic2159.md)

©2024 DriveWorks Ltd. All Rights Reserved.
