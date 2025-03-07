Collapse All Expand All Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
ComponentTaskCondition Class Members   
See Also Fields Properties Methods Events [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic6493.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components.Tasks Namespace](topic6391.md) : ComponentTaskCondition Class  
---  
  
Include Inherited Members    
Include Protected Members  


Glossary Item Box

The following tables list the members exposed by [ComponentTaskCondition](topic6493.md).

# Public Fields

| Name| Description  
---|---|---  
![Public Field](dotnetimages/publicField.gif)![static \(Shared in Visual Basic\)](dotnetimages/static.gif)| [CONDITION_RELEASE_TYPE_ID](topic6507.md)| The id of the released condition within the parents collection of released conditions.   
![Public Field](dotnetimages/publicField.gif)![static \(Shared in Visual Basic\)](dotnetimages/static.gif)| [INDEX_PARAM_TYPE_ID](topic6508.md)| The index of the task within the parents collection.   
![Public Field](dotnetimages/publicField.gif)![static \(Shared in Visual Basic\)](dotnetimages/static.gif)| [TITLE_PARAM_TYPE_ID](topic6509.md)| Gets the unique identifier of the [Title](topic6505.md) parameter in the release data.   
Top

# Public Properties

| Name| Description  
---|---|---  
![Public Property](dotnetimages/publicProperty.gif)| [Id](topic6500.md)| Gets the id of the condition.   
![Public Property](dotnetimages/publicProperty.gif)| [Index](topic6501.md)| Gets the index of the condition in the parent collection.   
![Public Property](dotnetimages/publicProperty.gif)| [Info](topic6502.md)| Gets the meta data describing the type of the condition.   
![Public Property](dotnetimages/publicProperty.gif)| [Parent](topic6503.md)| Gets the collection of conditions this condition belongs to.   
![Public Property](dotnetimages/publicProperty.gif)| [Properties](topic6504.md)| Gets the collection of properties for this condition.   
![Public Property](dotnetimages/publicProperty.gif)| [Title](topic6505.md)| Gets/sets the title of the condition.   
![Public Property](dotnetimages/publicProperty.gif)| [TypeName](topic6506.md)| Gets the type of the type of the condition.   
Top

# Public Methods

| Name| Description  
---|---|---  
Public Method| CreateObjRef|  (Inherited from System.MarshalByRefObject)  
Public Method| GetLifetimeService|  (Inherited from System.MarshalByRefObject)  
Public Method| [Save](topic6499.md)| Saves the condition to the backing XML store.   
Top

# Protected Methods

| Name| Description  
---|---|---  
Protected Method| MemberwiseClone| Overloaded. (Inherited from System.MarshalByRefObject)  
Top

# Public Events

| Name| Description  
---|---|---  
![Public Event](dotnetimages/publicEvent.gif)| [IndexChanged](topic6510.md)| The event that is raised whenever the index of this task within the parent collection changes.   
![Public Event](dotnetimages/publicEvent.gif)| [TitleChanged](topic6511.md)| The event that is raised whenever the [Title](topic6505.md) property's value has changed.   
Top

# See Also

#### Reference

[ComponentTaskCondition Class](topic6493.md)   
[DriveWorks.Components.Tasks Namespace](topic6391.md)


