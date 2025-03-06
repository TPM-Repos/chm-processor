![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
ComponentTaskReleaseCondition Class Members   
See Also Properties Methods Events [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic6647.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components.Tasks Namespace](topic6391.md) : ComponentTaskReleaseCondition Class  
---  
  
Include Inherited Members    
Include Protected Members  


Glossary Item Box

The following tables list the members exposed by [ComponentTaskReleaseCondition](topic6647.md).

# ![](dotnetimages/collapse.gif)Public Properties

| Name| Description  
---|---|---  
![Public Property](dotnetimages/publicProperty.gif)| [Id](topic6655.md)| Gets the unique identifier of this condition.   
![Public Property](dotnetimages/publicProperty.gif)| [Index](topic6656.md)| Gets the index of this condition within the parent collection.   
![Public Property](dotnetimages/publicProperty.gif)| [Info](topic6657.md)| Gets additional meta information about the condition, such as the localized title and description.   
![Public Property](dotnetimages/publicProperty.gif)| [Negated](topic6658.md)| Determins whether the condition evaluation is to be negated (have not applied to it).   
![Public Property](dotnetimages/publicProperty.gif)| [Parent](topic6659.md)| Gets the collection this condition belongs to.   
![Public Property](dotnetimages/publicProperty.gif)| [Properties](topic6660.md)| Represents all properties of the task that can have rules written for them.   
![Public Property](dotnetimages/publicProperty.gif)| [Title](topic6661.md)| Gets/sets the title of this condition.   
Top

# ![](dotnetimages/collapse.gif)Public Methods

| Name| Description  
---|---|---  
![Public Method](dotnetimages/publicMethod.gif)| CreateObjRef|  (Inherited from System.MarshalByRefObject)  
![Public Method](dotnetimages/publicMethod.gif)| GetLifetimeService|  (Inherited from System.MarshalByRefObject)  
![Public Method](dotnetimages/publicMethod.gif)| [Save](topic6654.md)| Pushes the current condition information into the backing store.   
Top

# ![](dotnetimages/collapse.gif)Protected Methods

| Name| Description  
---|---|---  
![Protected Method](dotnetimages/protectedMethod.gif)| [Evaluate](topic6653.md)| When overridden by a derived class, evaluates the condition.   
![Protected Method](dotnetimages/protectedMethod.gif)| MemberwiseClone| Overloaded. (Inherited from System.MarshalByRefObject)  
Top

# ![](dotnetimages/collapse.gif)Public Events

| Name| Description  
---|---|---  
![Public Event](dotnetimages/publicEvent.gif)| [TitleChanged](topic6662.md)| The event that gets raised whenever the value of the [Title](topic6661.md) property has changed.   
Top

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ComponentTaskReleaseCondition Class](topic6647.md)   
[DriveWorks.Components.Tasks Namespace](topic6391.md)


