       

 Collapse All Expand All  Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
SpecificationContext Class Methods   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic11149.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) : SpecificationContext Class  
---  
  
Include Inherited Members    
Include Protected Members    


Glossary Item Box

For a list of all members of this type, see [SpecificationContext members](topic11150.md).

# Public Methods

| Name| Description  
---|---|---  
![Public Method](dotnetimages/publicMethod.gif)| [Cancel](topic11160.md)| Cancels the specification.   
![Public Method](dotnetimages/publicMethod.gif)| [Copy](topic11161.md)| Overloaded. Starts a new specification based on the given specification.   
![Public Method](dotnetimages/publicMethod.gif)| CreateObjRef|  (Inherited from System.MarshalByRefObject)  
![Public Method](dotnetimages/publicMethod.gif)| [Delete](topic11164.md)| Deletes the specification represented by the context.   
![Public Method](dotnetimages/publicMethod.gif)| [DriveInputs](topic11165.md)|   
![Public Method](dotnetimages/publicMethod.gif)| [EnsureRunnableProject](topic11166.md)| Returns if the current specification is valid or not.   
![Public Method](dotnetimages/publicMethod.gif)| [GetExpectedSpecificationDirectory](topic11167.md)| Gets the current expected specification directory of a running specification.   
![Public Method](dotnetimages/publicMethod.gif)| GetLifetimeService|  (Inherited from System.MarshalByRefObject)  
![Public Method](dotnetimages/publicMethod.gif)| [GetOperations](topic11168.md)| Gets an array of transitions with the evaluated result of their conditions.   
![Public Method](dotnetimages/publicMethod.gif)| [GetTransitions](topic11169.md)| Gets an array of transitions with the evaluated result of their conditions.   
![Public Method](dotnetimages/publicMethod.gif)| [InvokeOperation](topic11170.md)| Overloaded. Invokes the specified operation.   
![Public Method](dotnetimages/publicMethod.gif)| [InvokeTransition](topic11173.md)| Overloaded. Invokes the specified transition.   
![Public Method](dotnetimages/publicMethod.gif)| [Navigate](topic11176.md)| Navigates the forms in a running specification.   
![Public Method](dotnetimages/publicMethod.gif)| [NavigateTo](topic11177.md)| Navigates to a specified form in a running specification.   
![Public Method](dotnetimages/publicMethod.gif)| [OnForceFormUpdateAsync](topic11188.md)| Raises the [ForceFormUpdate](topic11258.md) event, as well as despatching an asynchronus update event on the root [SpecificationContext](topic11149.md).   
![Public Method](dotnetimages/publicMethod.gif)| [OnFormValueChanged](topic11189.md)| Raises the [FormValueChanged](topic11259.md) event. The event data for the event.   
![Public Method](dotnetimages/publicMethod.gif)| [Open](topic11190.md)| Opens the given existing specification.   
![Public Method](dotnetimages/publicMethod.gif)| [QueryOperation](topic11191.md)| Queries an operation's tasks for confirmation messages that should be shown to an interactive user before invoking the operation.   
![Public Method](dotnetimages/publicMethod.gif)| [QueryTransition](topic11192.md)| Queries an transition's tasks for confirmation messages that should be shown to an interactive user before invoking the transition.   
![Public Method](dotnetimages/publicMethod.gif)| [Start](topic11193.md)| Starts a new specification based on the given project.   
![Public Method](dotnetimages/publicMethod.gif)| [UpdateArchivedState](topic11194.md)| Sets the archived state of a loaded/running specification.   
Top

# Protected Methods

| Name| Description  
---|---|---  
![Protected Method](dotnetimages/protectedMethod.gif)| [AllocateSpecificationId](topic11155.md)| Allocates a specification identifier to the specification, by default, uses the next specification identifier from the group.   
![Protected Method](dotnetimages/protectedMethod.gif)| [AssertLoaded](topic11156.md)| Raises an exception if the specification context is open.   
![Protected Method](dotnetimages/protectedMethod.gif)| [AssertNotLoaded](topic11157.md)| Raises an exception if the specification context is not open.   
![Protected Method](dotnetimages/protectedMethod.gif)| [AssertNotRunning](topic11158.md)| Raises an exception if the specification context is in a running state.   
![Protected Method](dotnetimages/protectedMethod.gif)| [AssertRunning](topic11159.md)| Raises an exception if the specification context is not in a running state.   
![Protected Method](dotnetimages/protectedMethod.gif)| MemberwiseClone| Overloaded. (Inherited from System.MarshalByRefObject)  
![Protected Method](dotnetimages/protectedMethod.gif)| [OnActiveDialogChanged](topic11178.md)| Raises the [ActiveDialogChanged](topic11237.md) event.   
![Protected Method](dotnetimages/protectedMethod.gif)| [OnActiveDialogChanging](topic11179.md)| Raises the [ActiveDialogChanging](topic11238.md) event.   
![Protected Method](dotnetimages/protectedMethod.gif)| [OnActiveDialogOrFormChanged](topic11180.md)| Raises the [ActiveDialogOrFormChanged](topic11239.md) event.   
![Protected Method](dotnetimages/protectedMethod.gif)| [OnActiveDialogOrFormChanging](topic11181.md)| Raises the [ActiveDialogOrFormChanging](topic11240.md) event.   
![Protected Method](dotnetimages/protectedMethod.gif)| [OnActiveDialogOrFormUpdated](topic11182.md)| Raises the [ActiveDialogOrFormUpdated](topic11241.md) event.   
![Protected Method](dotnetimages/protectedMethod.gif)| [OnActiveFormChanged](topic11183.md)| Raises the [ActiveFormChanged](topic11242.md) event.   
![Protected Method](dotnetimages/protectedMethod.gif)| [OnActiveFormChanging](topic11184.md)| Raises the [ActiveFormChanging](topic11243.md) event.   
![Protected Method](dotnetimages/protectedMethod.gif)| [OnDialogClosed](topic11185.md)| Raises the [OnDialogClosed](topic11185.md) event.   
![Protected Method](dotnetimages/protectedMethod.gif)| [OnDialogClosing](topic11186.md)| Raises the [OnDialogClosing](topic11186.md) event.   
![Protected Method](dotnetimages/protectedMethod.gif)| [OnDialogOpening](topic11187.md)| Raises the [OnDialogOpening](topic11187.md) event.   
Top

# See Also

#### Reference

[SpecificationContext Class](topic11149.md)   
[DriveWorks.Specification Namespace](topic10764.md)

©2024 DriveWorks Ltd. All Rights Reserved.
