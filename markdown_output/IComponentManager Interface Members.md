Collapse All Expand All Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
IComponentManager Interface Members   
See Also Properties Methods Events [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic13385.md)  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) : IComponentManager Interface  
---  
  
Include Inherited Members    


Glossary Item Box

The following tables list the members exposed by [IComponentManager](topic13385.md).

# Public Properties

| Name| Description  
---|---|---  
![ Property](dotnetimages/Property.gif)| [HasChanges](topic13408.md)| Gets whether there are any unsaved changes to components or their state.   
![ Property](dotnetimages/Property.gif)| [LastChangeIndex](topic13409.md)| Gets the index of the last change.   
Top

# Public Methods

| Name| Description  
---|---|---  
![ Method](dotnetimages/Method.gif)| [CaptureComponent](topic13390.md)| Captures the component with the given path.   
![ Method](dotnetimages/Method.gif)| [CaptureComponentReferenceWithCreate](topic13391.md)| Captures the component with the given path and adds it as a child to the given parent.   
![ Method](dotnetimages/Method.gif)| [GetComponent](topic13392.md)| Gets the captured component for the component with the given handle.   
![ Method](dotnetimages/Method.gif)| [GetComponentHandle](topic13393.md)| Gets the component handle for the component with the given path.   
![ Method](dotnetimages/Method.gif)| [GetComponentHandles](topic13394.md)| Gets an array of all known component handles.   
![ Method](dotnetimages/Method.gif)| [GetComponentParents](topic13395.md)| Gets all parents that holds references the given component.   
![ Method](dotnetimages/Method.gif)| [GetComponentReferences](topic13396.md)| Overloaded. Gets all components that hold references to the given component.   
![ Method](dotnetimages/Method.gif)| [GetRootComponentHandles](topic13399.md)| Overloaded. Gets an array of handles to all root components.   
![ Method](dotnetimages/Method.gif)| [NotifyModifiedComponent](topic13402.md)| Notify the component manager that the given component has changed.   
![ Method](dotnetimages/Method.gif)| [RemoveComponent](topic13403.md)| Removes the component with the given handle.   
![ Method](dotnetimages/Method.gif)| [RemoveComponentReference](topic13404.md)| Overloaded. Uncaptures the specified child from the parent and returns the number of places where the child is still used.   
![ Method](dotnetimages/Method.gif)| [Save](topic13407.md)| Pushes the unsaved changes to the group.   
Top

# Public Events

| Name| Description  
---|---|---  
![ Event](dotnetimages/Event.gif)| [HasChangesChanged](topic13410.md)| Raised whenever the value of the [HasChanges](topic13408.md) property changes.   
Top

# See Also

#### Reference

[IComponentManager Interface](topic13385.md)   
[DriveWorks.SolidWorks Namespace](topic13345.md)


