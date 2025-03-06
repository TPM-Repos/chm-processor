Task Class Methods   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) : Task Class  
---  
  
Include Inherited Members    
Include Protected Members    


Glossary Item Box

For a list of all members of this type, see [Task members](topic11630.md).

# Public Methods

| Name| Description  
---|---|---  
Public Method| CreateObjRef|  (Inherited from System.MarshalByRefObject)  
Public Method| [Delete](topic11636.md)| Deletes the condition.   
Public Method| [GetEditor](topic6945.md)| Gets the editor for this node. (Inherited from [DriveWorks.EventFlow.ExecutableNodeBase](topic6938.md))  
Public Method| [GetElement](topic11640.md)| Returns a deep copy of this task's Xml Element.   
Public Method| GetLifetimeService|  (Inherited from System.MarshalByRefObject)  
Public Method| [TryGetInputEndpoint](topic6955.md)| Attempts to find an input with the given name. (Inherited from [DriveWorks.EventFlow.ExecutableNodeBase](topic6938.md))  
Public Method| [TryGetOutputEndpoint](topic11646.md)| Overridden. Attempts to retrieve the end point with the given name.   
Top

# Protected Methods

| Name| Description  
---|---|---  
Protected Method| [AssertNotDeleted](topic11635.md)| Throws an instance of the [DriveWorks.ItemDeletedException](topic3549.md) if the item has been deleted.   
Protected Method| [DeleteCore](topic11637.md)| Performs any clean-up required when overridden by a derived class.   
Protected Method| [Execute](topic11638.md)| When overridden by a derived class, executes the action represented by the task.   
Protected Method| [ExecuteNodeCore](topic6944.md)|  (Inherited from [DriveWorks.EventFlow.ExecutableNodeBase](topic6938.md))  
Protected Method| [GetConfirmationMessage](topic11639.md)| When overridden by a derived class, gets a confirmation message which should be shown to an interactive user before executing the task sequence to which task belongs.   
Protected Method| [InitializeMetadata](topic11641.md)| Called when the backing store for this task has been initialized and the meta data is available to be read.   
Protected Method| [IsDeferred](topic11642.md)| Determines whether the task should be executed after the design master for the specification is saved.   
Protected Method| [IsDeleteContextTask](topic11643.md)| Determines whether the task will be deleting the specification context in it's execution.   
Protected Method| [IsRunningRequired](topic11644.md)| Determines whether the task requires the specification context to be open.   
Protected Method| MemberwiseClone| Overloaded. (Inherited from System.MarshalByRefObject)  
Protected Method| [RaiseLeftChanged](topic6946.md)| Raises the [DriveWorks.EventFlow.ExecutableNodeBase.LeftChanged](topic6978.md) event. (Inherited from [DriveWorks.EventFlow.ExecutableNodeBase](topic6938.md))  
Protected Method| [RaiseNameChanged](topic6947.md)| Raises the [DriveWorks.EventFlow.ExecutableNodeBase.NameChanged](topic6979.md) event. (Inherited from [DriveWorks.EventFlow.ExecutableNodeBase](topic6938.md))  
Protected Method| [RaiseTopChanged](topic6948.md)| Raises the [DriveWorks.EventFlow.ExecutableNodeBase.TopChanged](topic6981.md) event. (Inherited from [DriveWorks.EventFlow.ExecutableNodeBase](topic6938.md))  
Protected Method| [RaiseWidthChanged](topic6949.md)|  (Inherited from [DriveWorks.EventFlow.ExecutableNodeBase](topic6938.md))  
Protected Method| [RequiresSingleContext](topic11645.md)| Determines whether the task can be executed if there is more than one specification selected.   
Protected Method| [SetState](topic6950.md)| Overloaded. Sets the result of executing this node. (Inherited from [DriveWorks.EventFlow.ExecutableNodeBase](topic6938.md))  
Top

# See Also

#### Reference

[Task Class](topic11629.md)   
[DriveWorks.Specification Namespace](topic10764.md)


