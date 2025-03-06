StartChildSpecificationTask Class Methods   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification.StandardTasks Namespace](topic11896.md) : StartChildSpecificationTask Class  
---  
  
Include Inherited Members    
Include Protected Members    


Glossary Item Box

For a list of all members of this type, see [StartChildSpecificationTask members](topic12654.md).

# Public Methods

| Name| Description  
---|---|---  
Public Method| CreateObjRef|  (Inherited from System.MarshalByRefObject)  
Public Method| [Delete](topic11636.md)| Deletes the condition. (Inherited from [DriveWorks.Specification.Task](topic11629.md))  
Public Method| [GetEditor](topic6945.md)| Gets the editor for this node. (Inherited from [DriveWorks.EventFlow.ExecutableNodeBase](topic6938.md))  
Public Method| [GetElement](topic11640.md)| Returns a deep copy of this task's Xml Element. (Inherited from [DriveWorks.Specification.Task](topic11629.md))  
Public Method| GetLifetimeService|  (Inherited from System.MarshalByRefObject)  
Public Method| [TryGetInputEndpoint](topic6955.md)| Attempts to find an input with the given name. (Inherited from [DriveWorks.EventFlow.ExecutableNodeBase](topic6938.md))  
Public Method| [TryGetOutputEndpoint](topic11646.md)| Attempts to retrieve the end point with the given name. (Inherited from [DriveWorks.Specification.Task](topic11629.md))  
Top

# Protected Methods

| Name| Description  
---|---|---  
Protected Method| [AssertNotDeleted](topic11635.md)| Throws an instance of the [DriveWorks.ItemDeletedException](topic3549.md) if the item has been deleted. (Inherited from [DriveWorks.Specification.Task](topic11629.md))  
Protected Method| [DeleteCore](topic11637.md)| Performs any clean-up required when overridden by a derived class. (Inherited from [DriveWorks.Specification.Task](topic11629.md))  
Protected Method| [Execute](topic12659.md)| Overridden.   
Protected Method| [ExecuteNodeCore](topic6944.md)|  (Inherited from [DriveWorks.EventFlow.ExecutableNodeBase](topic6938.md))  
Protected Method| [GetConfirmationMessage](topic11639.md)| When overridden by a derived class, gets a confirmation message which should be shown to an interactive user before executing the task sequence to which task belongs. (Inherited from [DriveWorks.Specification.Task](topic11629.md))  
Protected Method| [InitializeMetadata](topic11641.md)| Called when the backing store for this task has been initialized and the meta data is available to be read. (Inherited from [DriveWorks.Specification.Task](topic11629.md))  
Protected Method| [IsDeferred](topic11642.md)| Determines whether the task should be executed after the design master for the specification is saved. (Inherited from [DriveWorks.Specification.Task](topic11629.md))  
Protected Method| [IsDeleteContextTask](topic11643.md)| Determines whether the task will be deleting the specification context in it's execution. (Inherited from [DriveWorks.Specification.Task](topic11629.md))  
Protected Method| [IsRunningRequired](topic11644.md)| Determines whether the task requires the specification context to be open. (Inherited from [DriveWorks.Specification.Task](topic11629.md))  
Protected Method| MemberwiseClone| Overloaded. (Inherited from System.MarshalByRefObject)  
Protected Method| [RaiseLeftChanged](topic6946.md)| Raises the [DriveWorks.EventFlow.ExecutableNodeBase.LeftChanged](topic6978.md) event. (Inherited from [DriveWorks.EventFlow.ExecutableNodeBase](topic6938.md))  
Protected Method| [RaiseNameChanged](topic6947.md)| Raises the [DriveWorks.EventFlow.ExecutableNodeBase.NameChanged](topic6979.md) event. (Inherited from [DriveWorks.EventFlow.ExecutableNodeBase](topic6938.md))  
Protected Method| [RaiseTopChanged](topic6948.md)| Raises the [DriveWorks.EventFlow.ExecutableNodeBase.TopChanged](topic6981.md) event. (Inherited from [DriveWorks.EventFlow.ExecutableNodeBase](topic6938.md))  
Protected Method| [RaiseWidthChanged](topic6949.md)|  (Inherited from [DriveWorks.EventFlow.ExecutableNodeBase](topic6938.md))  
Protected Method| [RequiresSingleContext](topic11645.md)| Determines whether the task can be executed if there is more than one specification selected. (Inherited from [DriveWorks.Specification.Task](topic11629.md))  
Protected Method| [SetState](topic6950.md)| Overloaded. Sets the result of executing this node. (Inherited from [DriveWorks.EventFlow.ExecutableNodeBase](topic6938.md))  
Top

# See Also

#### Reference

[StartChildSpecificationTask Class](topic12653.md)   
[DriveWorks.Specification.StandardTasks Namespace](topic11896.md)


