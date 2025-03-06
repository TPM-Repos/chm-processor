State Class Members   
See Also Properties Methods Events [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic11559.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) : State Class  
---  
  
Include Inherited Members    
Include Protected Members  


Glossary Item Box

The following tables list the members exposed by [State](topic11559.md).

# Public Properties

| Name| Description  
---|---|---  
![Public Property](dotnetimages/publicProperty.gif)| [Id](topic11566.md)| Gets the unique identifier of the state.   
![Public Property](dotnetimages/publicProperty.gif)| [IsDeleted](topic11567.md)| Gets whether the state has been deleted and therefore can't be used.   
![Public Property](dotnetimages/publicProperty.gif)| [OnEnterEvent](topic11568.md)| Gets the event definition which describes the actions taken when the state is entered.   
![Public Property](dotnetimages/publicProperty.gif)| [OnLeaveEvent](topic11569.md)| Gets the event definition which describes the actions taken when the state is exited.   
![Public Property](dotnetimages/publicProperty.gif)| [Operations](topic11570.md)| Gets the operation manager for the state.   
![Public Property](dotnetimages/publicProperty.gif)| [Teams](topic11571.md)| Gets the teams which have access to the state.   
![Public Property](dotnetimages/publicProperty.gif)| [Title](topic11572.md)| Gets/sets the title.   
![Public Property](dotnetimages/publicProperty.gif)| [Transitions](topic11573.md)| Gets the transition manager for the state.   
![Public Property](dotnetimages/publicProperty.gif)| [Type](topic11574.md)| Gets/sets the type of state.   
Top

# Public Methods

| Name| Description  
---|---|---  
![Public Method](dotnetimages/publicMethod.gif)| CreateObjRef|  (Inherited from System.MarshalByRefObject)  
![Public Method](dotnetimages/publicMethod.gif)| [Delete](topic11565.md)| Deletes the state from the specification-flow.   
![Public Method](dotnetimages/publicMethod.gif)| GetLifetimeService|  (Inherited from System.MarshalByRefObject)  
Top

# Protected Methods

| Name| Description  
---|---|---  
![Protected Method](dotnetimages/protectedMethod.gif)| MemberwiseClone| Overloaded. (Inherited from System.MarshalByRefObject)  
Top

# Public Events

| Name| Description  
---|---|---  
![Public Event](dotnetimages/publicEvent.gif)| [Deleted](topic11575.md)| Raised when the [Delete](topic11565.md) method is called to delete the state.   
![Public Event](dotnetimages/publicEvent.gif)| [TitleChanged](topic11576.md)| Raised when the [Title](topic11572.md) property changes.   
![Public Event](dotnetimages/publicEvent.gif)| [TypeChanged](topic11577.md)| Raised when the [Type](topic11574.md) property changes.   
Top

# See Also

#### Reference

[State Class](topic11559.md)   
[DriveWorks.Specification Namespace](topic10764.md)


