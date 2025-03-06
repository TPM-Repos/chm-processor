![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
GroupDataTable Class Members   
See Also Properties Methods Events [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3110.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) : GroupDataTable Class  
---  
  
Include Inherited Members    
Include Protected Members  


Glossary Item Box

The following tables list the members exposed by [GroupDataTable](topic3110.md).

# ![](dotnetimages/collapse.gif)Public Properties

| Name| Description  
---|---|---  
![Public Property](dotnetimages/publicProperty.gif)| [Id](topic3128.md)| Gets the unique identifier for this table.   
![Public Property](dotnetimages/publicProperty.gif)| [MetaData](topic3130.md)| Information about this table.   
![Public Property](dotnetimages/publicProperty.gif)| [Name](topic3131.md)| Gets the display name for this table.   
Top

# ![](dotnetimages/collapse.gif)Protected Properties

| Name| Description  
---|---|---  
![Protected Property](dotnetimages/protectedProperty.gif)| [IsDirty](topic3129.md)| Gets if the cache table data is not the latest version.   
Top

# ![](dotnetimages/collapse.gif)Public Methods

| Name| Description  
---|---|---  
Public Method| [Delete](topic3117.md)| Removes the table from the group.   
Public Method| [GetColumns](topic3119.md)| Gets all columns present in this table.   
Public Method| [GetTableData](topic3120.md)| Gets the data for this table.   
Public Method| [SetRows](topic3126.md)| Updates rows of this table with the specified data based on control column names.   
Public Method| [SetTableData](topic3127.md)| Sets the data of this table to the specified data.   
Top

# ![](dotnetimages/collapse.gif)Protected Methods

| Name| Description  
---|---|---  
Protected Method| [EnsureTableDataIsLatest](topic3118.md)| Will fetch the latest version of table data, if version is out of sync.   
Protected Method| [Initialize](topic3122.md)| Called after table has been constructed and is ready for initialization.   
Protected Method| [OnDeleted](topic3123.md)| Called before the table is about to be deleted.   
Protected Method| [OnMetaDataChanged](topic3124.md)| Called whenever the data property changes.   
Protected Method| [RaiseTableDataChanged](topic3125.md)| Raises the [TableDataChanged](topic3135.md) event.   
Top

# ![](dotnetimages/collapse.gif)Public Events

| Name| Description  
---|---|---  
![Public Event](dotnetimages/publicEvent.gif)| [Deleted](topic3132.md)| Raised when this table is deleted.   
![Public Event](dotnetimages/publicEvent.gif)| [MetaDataChanged](topic3133.md)| Raised when the metadata of this table changes.   
![Public Event](dotnetimages/publicEvent.gif)| [NameChanged](topic3134.md)| Raised when the name of this table changes.   
![Public Event](dotnetimages/publicEvent.gif)| [TableDataChanged](topic3135.md)| Raised when the data in this table changes.   
Top

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[GroupDataTable Class](topic3110.md)   
[DriveWorks Namespace](topic2159.md)


