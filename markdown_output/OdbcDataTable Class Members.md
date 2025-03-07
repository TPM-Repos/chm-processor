Collapse All Expand All Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
OdbcDataTable Class Members   
See Also Properties Methods Events [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3746.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) : OdbcDataTable Class  
---  
  
Include Inherited Members    
Include Protected Members  


Glossary Item Box

The following tables list the members exposed by [OdbcDataTable](topic3746.md).

# Public Properties

| Name| Description  
---|---|---  
![Public Property](dotnetimages/publicProperty.gif)| [AllFields](topic3756.md)| If all the avialable fields should be read, as apposed to reading the specified ones.   
![Public Property](dotnetimages/publicProperty.gif)| [DataSourceName](topic3757.md)| The name of the odbc data source.   
![Public Property](dotnetimages/publicProperty.gif)| [DisplayName](topic4303.md)| Gets/sets the name of the data source. (Inherited from [DriveWorks.ProjectDataTable](topic4282.md))  
![Public Property](dotnetimages/publicProperty.gif)| [Fields](topic3758.md)| The fields that are used from the selected table.   
![Public Property](dotnetimages/publicProperty.gif)| [InvariantName](topic4304.md)| Gets the invariant name of the table. (Inherited from [DriveWorks.ProjectDataTable](topic4282.md))  
![Public Property](dotnetimages/publicProperty.gif)| [IsDeleted](topic4305.md)| Gets whether the table has been deleted. (Inherited from [DriveWorks.ProjectDataTable](topic4282.md))  
![Public Property](dotnetimages/publicProperty.gif)| [IsInitialized](topic4306.md)| Gets whether the table has been initialized. (Inherited from [DriveWorks.ProjectDataTable](topic4282.md))  
![Public Property](dotnetimages/publicProperty.gif)| [Password](topic3759.md)| The password (if any) used to connect to the odbc data source.   
![Public Property](dotnetimages/publicProperty.gif)| [RefreshOnLoad](topic4307.md)| Gets whether the data table should be refreshed from it's source when the project is loaded. (Inherited from [DriveWorks.ProjectDataTable](topic4282.md))  
![Public Property](dotnetimages/publicProperty.gif)| [RefreshTableOnLoad](topic3760.md)| If the data from the talbew should be re-loaded each time the project is launched.   
![Public Property](dotnetimages/publicProperty.gif)| [TableName](topic3761.md)| The name of the table to read from the odbc data source.   
![Public Property](dotnetimages/publicProperty.gif)| [Username](topic3762.md)| The username (if any) used to connect to the odbc data source.   
Top

# Protected Properties

| Name| Description  
---|---|---  
![Protected Property](dotnetimages/protectedProperty.gif)| [Data](topic4302.md)| Gets/sets the custom data for the document. (Inherited from [DriveWorks.ProjectDataTable](topic4282.md))  
![Protected Property](dotnetimages/protectedProperty.gif)| [StoreIsSerialized](topic4308.md)| Gets whether the table's backing store should be serialized or not. (Inherited from [DriveWorks.ProjectDataTable](topic4282.md))  
Top

# Public Methods

| Name| Description  
---|---|---  
Public Method| CreateObjRef|  (Inherited from System.MarshalByRefObject)  
Public Method| [Delete](topic4290.md)| Deletes the table from the project. (Inherited from [DriveWorks.ProjectDataTable](topic4282.md))  
Public Method| [GetCachedTableData](topic4292.md)| Gets the cached table data from the design master. (Inherited from [DriveWorks.ProjectDataTable](topic4282.md))  
Public Method| GetLifetimeService|  (Inherited from System.MarshalByRefObject)  
Public Method| [Refresh](topic4300.md)| Refreshes the data table by asking the provider to re-retrieve the data. (Inherited from [DriveWorks.ProjectDataTable](topic4282.md))  
Top

# Protected Methods

| Name| Description  
---|---|---  
Protected Method| [AssertInitialized](topic4288.md)| Throws an exception if the document hasn't been initialized. (Inherited from [DriveWorks.ProjectDataTable](topic4282.md))  
Protected Method| [AssertNotDeleted](topic4289.md)| Throws an exception if the document has been deleted. (Inherited from [DriveWorks.ProjectDataTable](topic4282.md))  
Protected Method| [DeleteCore](topic4291.md)| When overridden in a derived class, performs any clean-up necessary to delete the document from the project. (Inherited from [DriveWorks.ProjectDataTable](topic4282.md))  
Protected Method| [GetTableData](topic3752.md)| Overridden.   
Protected Method| [InitializeExistingCore](topic3753.md)| Overridden.   
Protected Method| [InitializeNewCore](topic3754.md)| Overridden.   
Protected Method| [IsNameValidCore](topic4298.md)| When overridden in a derived class, checks to see if the specified new name is a valid name for the given type of document. (Inherited from [DriveWorks.ProjectDataTable](topic4282.md))  
Protected Method| MemberwiseClone| Overloaded. (Inherited from System.MarshalByRefObject)  
Protected Method| [NotifyStoreRead](topic4299.md)| When overridden in a derived class, handles the store being read for the first time. (Inherited from [DriveWorks.ProjectDataTable](topic4282.md))  
Protected Method| [RefreshOnProjectLoad](topic3755.md)| Overridden. Allow fresh on load option.   
Top

# Public Events

| Name| Description  
---|---|---  
![Public Event](dotnetimages/publicEvent.gif)| [Deleted](topic4309.md)| Raised when the document is deleted. (Inherited from [DriveWorks.ProjectDataTable](topic4282.md))  
![Public Event](dotnetimages/publicEvent.gif)| [NameChanged](topic4310.md)| Raised when the document's name changes. (Inherited from [DriveWorks.ProjectDataTable](topic4282.md))  
Top

# See Also

#### Reference

[OdbcDataTable Class](topic3746.md)   
[DriveWorks Namespace](topic2159.md)


