SpecificationContext Class Methods   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) : SpecificationContext Class  
---  
  
Include Inherited Members    
Include Protected Members    


Glossary Item Box

For a list of all members of this type, see [SpecificationContext members](topic11150.md).

# Public Methods

| Name| Description  
---|---|---  
Public Method| [Cancel](topic11160.md)| Cancels the specification.   
Public Method| [Copy](topic11161.md)| Overloaded. Starts a new specification based on the given specification.   
Public Method| CreateObjRef|  (Inherited from System.MarshalByRefObject)  
Public Method| [Delete](topic11164.md)| Deletes the specification represented by the context.   
Public Method| [DriveInputs](topic11165.md)|   
Public Method| [EnsureRunnableProject](topic11166.md)| Returns if the current specification is valid or not.   
Public Method| [GetExpectedSpecificationDirectory](topic11167.md)| Gets the current expected specification directory of a running specification.   
Public Method| GetLifetimeService|  (Inherited from System.MarshalByRefObject)  
Public Method| [GetOperations](topic11168.md)| Gets an array of transitions with the evaluated result of their conditions.   
Public Method| [GetTransitions](topic11169.md)| Gets an array of transitions with the evaluated result of their conditions.   
Public Method| [InvokeOperation](topic11170.md)| Overloaded. Invokes the specified operation.   
Public Method| [InvokeTransition](topic11173.md)| Overloaded. Invokes the specified transition.   
Public Method| [Navigate](topic11176.md)| Navigates the forms in a running specification.   
Public Method| [NavigateTo](topic11177.md)| Navigates to a specified form in a running specification.   
Public Method| [OnForceFormUpdateAsync](topic11188.md)| Raises the [ForceFormUpdate](topic11258.md) event, as well as despatching an asynchronus update event on the root [SpecificationContext](topic11149.md).   
Public Method| [OnFormValueChanged](topic11189.md)| Raises the [FormValueChanged](topic11259.md) event. The event data for the event.   
Public Method| [Open](topic11190.md)| Opens the given existing specification.   
Public Method| [QueryOperation](topic11191.md)| Queries an operation's tasks for confirmation messages that should be shown to an interactive user before invoking the operation.   
Public Method| [QueryTransition](topic11192.md)| Queries an transition's tasks for confirmation messages that should be shown to an interactive user before invoking the transition.   
Public Method| [Start](topic11193.md)| Starts a new specification based on the given project.   
Public Method| [UpdateArchivedState](topic11194.md)| Sets the archived state of a loaded/running specification.   
Top

# Protected Methods

| Name| Description  
---|---|---  
Protected Method| [AllocateSpecificationId](topic11155.md)| Allocates a specification identifier to the specification, by default, uses the next specification identifier from the group.   
Protected Method| [AssertLoaded](topic11156.md)| Raises an exception if the specification context is open.   
Protected Method| [AssertNotLoaded](topic11157.md)| Raises an exception if the specification context is not open.   
Protected Method| [AssertNotRunning](topic11158.md)| Raises an exception if the specification context is in a running state.   
Protected Method| [AssertRunning](topic11159.md)| Raises an exception if the specification context is not in a running state.   
Protected Method| MemberwiseClone| Overloaded. (Inherited from System.MarshalByRefObject)  
Protected Method| [OnActiveDialogChanged](topic11178.md)| Raises the [ActiveDialogChanged](topic11237.md) event.   
Protected Method| [OnActiveDialogChanging](topic11179.md)| Raises the [ActiveDialogChanging](topic11238.md) event.   
Protected Method| [OnActiveDialogOrFormChanged](topic11180.md)| Raises the [ActiveDialogOrFormChanged](topic11239.md) event.   
Protected Method| [OnActiveDialogOrFormChanging](topic11181.md)| Raises the [ActiveDialogOrFormChanging](topic11240.md) event.   
Protected Method| [OnActiveDialogOrFormUpdated](topic11182.md)| Raises the [ActiveDialogOrFormUpdated](topic11241.md) event.   
Protected Method| [OnActiveFormChanged](topic11183.md)| Raises the [ActiveFormChanged](topic11242.md) event.   
Protected Method| [OnActiveFormChanging](topic11184.md)| Raises the [ActiveFormChanging](topic11243.md) event.   
Protected Method| [OnDialogClosed](topic11185.md)| Raises the [OnDialogClosed](topic11185.md) event.   
Protected Method| [OnDialogClosing](topic11186.md)| Raises the [OnDialogClosing](topic11186.md) event.   
Protected Method| [OnDialogOpening](topic11187.md)| Raises the [OnDialogOpening](topic11187.md) event.   
Top

# See Also

#### Reference

[SpecificationContext Class](topic11149.md)   
[DriveWorks.Specification Namespace](topic10764.md)


