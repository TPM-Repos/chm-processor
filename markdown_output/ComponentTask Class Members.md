Collapse All Expand All Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
ComponentTask Class Members   
See Also Fields Properties Methods Events [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic6407.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components.Tasks Namespace](topic6391.md) : ComponentTask Class  
---  
  
Include Inherited Members    
Include Protected Members  


Glossary Item Box

The following tables list the members exposed by [ComponentTask](topic6407.md).

# Public Fields

| Name| Description  
---|---|---  
![Public Field](dotnetimages/publicField.gif)![static \(Shared in Visual Basic\)](dotnetimages/static.gif)| [INDEX_PARAM_TYPE_ID](topic6423.md)| The type id of the [Index](topic6415.md) parameter the release data for [ComponentTask](topic6407.md)s.   
![Public Field](dotnetimages/publicField.gif)![static \(Shared in Visual Basic\)](dotnetimages/static.gif)| [LOCATION_PARAM_TYPE_ID](topic6424.md)| The type id of the [Location](topic6416.md) parameter the release data for [ComponentTask](topic6407.md)s.   
![Public Field](dotnetimages/publicField.gif)![static \(Shared in Visual Basic\)](dotnetimages/static.gif)| [TASK_RELEASE_TYPE_ID](topic6425.md)| The element type id of released [ComponentTask](topic6407.md)s in the underlying release data.   
Top

# Public Properties

| Name| Description  
---|---|---  
![Public Property](dotnetimages/publicProperty.gif)| [ComponentId](topic6413.md)| Gets the id of the component this task is associated with.   
![Public Property](dotnetimages/publicProperty.gif)| [Id](topic6414.md)| Gets the unique identifier of this task.   
![Public Property](dotnetimages/publicProperty.gif)| [Index](topic6415.md)| Gets the index of this task in the parent collection.   
![Public Property](dotnetimages/publicProperty.gif)| [Location](topic6416.md)| Gets/sets the location of this task in the generation sequence.   
![Public Property](dotnetimages/publicProperty.gif)| [Name](topic6417.md)| Gets/sets the title of the task.   
![Public Property](dotnetimages/publicProperty.gif)| [Parameters](topic6418.md)| Gets the collection of parameters for this task.   
![Public Property](dotnetimages/publicProperty.gif)| [ReleaseConditions](topic6419.md)| Gets the collection of conditions that governs whether this task gets released alongside the associated component.   
![Public Property](dotnetimages/publicProperty.gif)| [RuntimeConditions](topic6420.md)| Gets the collection of conditions that will be released alongside the component and evaluated at run time.   
![Public Property](dotnetimages/publicProperty.gif)| [Scope](topic6421.md)| Gets the scope the task has been added to.   
![Public Property](dotnetimages/publicProperty.gif)| [Type](topic6422.md)| Gets the type of the task.   
Top

# Public Methods

| Name| Description  
---|---|---  
Public Method| CreateObjRef|  (Inherited from System.MarshalByRefObject)  
Public Method| GetLifetimeService|  (Inherited from System.MarshalByRefObject)  
Top

# Protected Methods

| Name| Description  
---|---|---  
Protected Method| MemberwiseClone| Overloaded. (Inherited from System.MarshalByRefObject)  
Top

# Public Events

| Name| Description  
---|---|---  
![Public Event](dotnetimages/publicEvent.gif)| [IndexChanged](topic6426.md)| The event that gets raised when the index of the task has changed in the parent collection.   
![Public Event](dotnetimages/publicEvent.gif)| [LocationChanged](topic6427.md)| The even that gets raised when the location of the task has changed.   
![Public Event](dotnetimages/publicEvent.gif)| [NameChanged](topic6428.md)| The event that gets raised when the name of the task has changed.   
Top

# See Also

#### Reference

[ComponentTask Class](topic6407.md)   
[DriveWorks.Components.Tasks Namespace](topic6391.md)


