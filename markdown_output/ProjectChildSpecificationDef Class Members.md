![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
ProjectChildSpecificationDef Class Members   
See Also Properties Methods Events [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic4019.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) : ProjectChildSpecificationDef Class  
---  
  
Include Inherited Members    
Include Protected Members  


Glossary Item Box

The following tables list the members exposed by [ProjectChildSpecificationDef](topic4019.md).

# ![](dotnetimages/collapse.gif)Public Properties

| Name| Description  
---|---|---  
![Public Property](dotnetimages/publicProperty.gif)| [Name](topic4040.md)| Gets the name of the child specification definition.   
![Public Property](dotnetimages/publicProperty.gif)| [ProjectDefinitions](topic4041.md)| Gets the definition of each project which can provide the basis of a child specification for the child specification definition.   
![Public Property](dotnetimages/publicProperty.gif)| [SynchronizeEmbeddedSpecifications](topic4042.md)| Returns whether or not embedded specifications will be continuously updated as values change in both the child and parent specification.   
![Public Property](dotnetimages/publicProperty.gif)| [VariableColumns](topic4043.md)| Gets the variable columns for the child specification definition.   
Top

# ![](dotnetimages/collapse.gif)Public Methods

| Name| Description  
---|---|---  
Public Method| [AddItem](topic4026.md)| Adds a new item to this item list.   
Public Method| [AddProjectDefinition](topic4027.md)| Creates a new [ProjectChildSpecificationProjectDef](topic4067.md) instance and adds it to this [ProjectChildSpecificationDef](topic4019.md).   
Public Method| CreateObjRef|  (Inherited from System.MarshalByRefObject)  
Public Method| [DeleteItem](topic4028.md)| Removes a item from the item list.   
Public Method| [EditItem](topic4029.md)| Edits an existing item in this item list.   
Public Method| [GetChildSpecificationDetails](topic4030.md)| Gets the specification details for the specification name provided.   
Public Method| [GetData](topic4031.md)| Gets information about the child specifications that have been added to the current project or specification.   
Public Method| [GetItem](topic4032.md)| Gets the item at the specified index.   
Public Method| [GetItemCount](topic4033.md)| Gets the number of items that have been added to the child specification list.   
Public Method| [GetItems](topic4034.md)| Gets an collection of all items in this child specification list.   
Public Method| GetLifetimeService|  (Inherited from System.MarshalByRefObject)  
Public Method| [MoveItemDown](topic4035.md)| Moves an item down in the list of items.   
Public Method| [MoveItemUp](topic4036.md)| Moves an item up in the list of items.   
Public Method| [OpenProjectForQuery](topic4037.md)| Opens the specified project so that it's constants and variable information can be queried, and returns it as an System.IDisposable object.   
Public Method| [RemoveProjectDefinition](topic4038.md)| Removes a project definition from the item list.   
Public Method| [TryGetProjectDefinition](topic4039.md)| Gets the project definition for a specific child specification project.   
Top

# ![](dotnetimages/collapse.gif)Protected Methods

| Name| Description  
---|---|---  
Protected Method| MemberwiseClone| Overloaded. (Inherited from System.MarshalByRefObject)  
Top

# ![](dotnetimages/collapse.gif)Public Events

| Name| Description  
---|---|---  
![Public Event](dotnetimages/publicEvent.gif)| [ItemIndexChanged](topic4044.md)| Raised when any item is moved up or down.   
![Public Event](dotnetimages/publicEvent.gif)| [ItemsChanged](topic4045.md)| Raised when any items have been added/deleted/edited/moved.   
![Public Event](dotnetimages/publicEvent.gif)| [Renamed](topic4046.md)| Raised when [Name](topic4040.md) has changed.   
Top

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectChildSpecificationDef Class](topic4019.md)   
[DriveWorks Namespace](topic2159.md)


