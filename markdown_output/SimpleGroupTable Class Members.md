SimpleGroupTable Class Members   
See Also Properties Methods Events [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic10009.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.GroupTables Namespace](topic10007.md) : SimpleGroupTable Class  
---  
  
Include Inherited Members    
Include Protected Members  


Glossary Item Box

The following tables list the members exposed by [SimpleGroupTable](topic10009.md).

# Public Properties

| Name| Description  
---|---|---  
![Public Property](dotnetimages/publicProperty.gif)| [Id](topic3128.md)| Gets the unique identifier for this table. (Inherited from [DriveWorks.GroupDataTable](topic3110.md))  
![Public Property](dotnetimages/publicProperty.gif)| [MetaData](topic3130.md)| Information about this table. (Inherited from [DriveWorks.GroupDataTable](topic3110.md))  
![Public Property](dotnetimages/publicProperty.gif)| [Name](topic3131.md)| Gets the display name for this table. (Inherited from [DriveWorks.GroupDataTable](topic3110.md))  
Top

# Protected Properties

| Name| Description  
---|---|---  
![Protected Property](dotnetimages/protectedProperty.gif)| [IsDirty](topic3129.md)| Gets if the cache table data is not the latest version. (Inherited from [DriveWorks.GroupDataTable](topic3110.md))  
Top

# Public Methods

| Name| Description  
---|---|---  
Public Method| [Delete](topic3117.md)| Removes the table from the group. (Inherited from [DriveWorks.GroupDataTable](topic3110.md))  
Public Method| [GetColumns](topic3119.md)| Gets all columns present in this table. (Inherited from [DriveWorks.GroupDataTable](topic3110.md))  
Public Method| [GetTableData](topic3120.md)| Gets the data for this table. (Inherited from [DriveWorks.GroupDataTable](topic3110.md))  
Public Method| [SetRows](topic3126.md)| Updates rows of this table with the specified data based on control column names. (Inherited from [DriveWorks.GroupDataTable](topic3110.md))  
Public Method| [SetTableData](topic3127.md)| Sets the data of this table to the specified data. (Inherited from [DriveWorks.GroupDataTable](topic3110.md))  
Top

# Protected Methods

| Name| Description  
---|---|---  
Protected Method| [EnsureTableDataIsLatest](topic3118.md)| Will fetch the latest version of table data, if version is out of sync. (Inherited from [DriveWorks.GroupDataTable](topic3110.md))  
Protected Method| [Initialize](topic3122.md)| Called after table has been constructed and is ready for initialization. (Inherited from [DriveWorks.GroupDataTable](topic3110.md))  
Protected Method| [OnDeleted](topic3123.md)| Called before the table is about to be deleted. (Inherited from [DriveWorks.GroupDataTable](topic3110.md))  
Protected Method| [OnMetaDataChanged](topic3124.md)| Called whenever the data property changes. (Inherited from [DriveWorks.GroupDataTable](topic3110.md))  
Protected Method| [RaiseTableDataChanged](topic3125.md)| Raises the [DriveWorks.GroupDataTable.TableDataChanged](topic3135.md) event. (Inherited from [DriveWorks.GroupDataTable](topic3110.md))  
Top

# Public Events

| Name| Description  
---|---|---  
![Public Event](dotnetimages/publicEvent.gif)| [Deleted](topic3132.md)| Raised when this table is deleted. (Inherited from [DriveWorks.GroupDataTable](topic3110.md))  
![Public Event](dotnetimages/publicEvent.gif)| [MetaDataChanged](topic3133.md)| Raised when the metadata of this table changes. (Inherited from [DriveWorks.GroupDataTable](topic3110.md))  
![Public Event](dotnetimages/publicEvent.gif)| [NameChanged](topic3134.md)| Raised when the name of this table changes. (Inherited from [DriveWorks.GroupDataTable](topic3110.md))  
![Public Event](dotnetimages/publicEvent.gif)| [TableDataChanged](topic3135.md)| Raised when the data in this table changes. (Inherited from [DriveWorks.GroupDataTable](topic3110.md))  
Top

# See Also

#### Reference

[SimpleGroupTable Class](topic10009.md)   
[DriveWorks.GroupTables Namespace](topic10007.md)


