ReleaseComponentController Class Members   
See Also Properties Methods [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic6252.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) : ReleaseComponentController Class  
---  
  
Include Inherited Members    
Include Protected Members  


Glossary Item Box

The following tables list the members exposed by [ReleaseComponentController](topic6252.md).

# Public Properties

| Name| Description  
---|---|---  
![Public Property](dotnetimages/publicProperty.gif)| [DeferAllDrawings](topic6269.md)| Gets whether all drawings should be flagged for generation at a later stage.   
![Public Property](dotnetimages/publicProperty.gif)| [DrawingsToDefer](topic6270.md)| Gets the name of the drawings that should be flagged for generation at a later stage.   
![Public Property](dotnetimages/publicProperty.gif)| [IsRoot](topic6271.md)| Determines whether the component being released is a root component.   
![Public Property](dotnetimages/publicProperty.gif)| [ReleasedComponentId](topic6272.md)| Gets the unique identifier that is assigned to the component.   
![Public Property](dotnetimages/publicProperty.gif)| [SpecificationContext](topic6273.md)| Gets the specification context associated with the current release process.   
![Public Property](dotnetimages/publicProperty.gif)| [Tracker](topic6274.md)| Gets the release tracker for the current release process.   
Top

# Public Methods

| Name| Description  
---|---|---  
![Public Method](dotnetimages/publicMethod.gif)| [AddChildComponentFromComponentSet](topic6258.md)| Overloaded. Adds the named component set as a child of the component being released.   
![Public Method](dotnetimages/publicMethod.gif)| [AddDrivenChildComponent](topic6261.md)| Overloaded. Adds a new component as a child of the component being released.   
![Public Method](dotnetimages/publicMethod.gif)| [AddStaticChildReplacement](topic6264.md)| Adds a new static child replacement for the child with the given master path   
![Public Method](dotnetimages/publicMethod.gif)| CreateObjRef|  (Inherited from System.MarshalByRefObject)  
![Public Method](dotnetimages/publicMethod.gif)| [GetComponentByComponentSetName](topic6265.md)| Gets the root component for the component set with the given name from the local release results. See remarks for details.   
![Public Method](dotnetimages/publicMethod.gif)| [GetComponentByName](topic6266.md)| Gets a component with the given name from the local release results. See remarks for details.   
![Public Method](dotnetimages/publicMethod.gif)| GetLifetimeService|  (Inherited from System.MarshalByRefObject)  
![Public Method](dotnetimages/publicMethod.gif)| [GetReferenceByComponentSetName](topic6267.md)| Gets the root component reference for the component set with the given name from the local release results. See remarks for details.   
![Public Method](dotnetimages/publicMethod.gif)| [GetTasksInScope](topic6268.md)| Gets all scoped tasks in the given scope.   
Top

# Protected Methods

| Name| Description  
---|---|---  
![Protected Method](dotnetimages/protectedMethod.gif)| MemberwiseClone| Overloaded. (Inherited from System.MarshalByRefObject)  
Top

# See Also

#### Reference

[ReleaseComponentController Class](topic6252.md)   
[DriveWorks.Components Namespace](topic6089.md)


