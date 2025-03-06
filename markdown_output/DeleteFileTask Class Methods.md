![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
DeleteFileTask Class Methods   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic12134.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification.StandardTasks Namespace](topic11896.md) : DeleteFileTask Class  
---  
  
Include Inherited Members    
Include Protected Members    


Glossary Item Box

For a list of all members of this type, see [DeleteFileTask members](topic12135.md).

# ![](dotnetimages/collapse.gif)Public Methods

| Name| Description  
---|---|---  
![Public Method](dotnetimages/publicMethod.gif)| CreateObjRef|  (Inherited from System.MarshalByRefObject)  
![Public Method](dotnetimages/publicMethod.gif)| [Delete](topic11636.md)| Deletes the condition. (Inherited from [DriveWorks.Specification.Task](topic11629.md))  
![Public Method](dotnetimages/publicMethod.gif)| [GetEditor](topic6945.md)| Gets the editor for this node. (Inherited from [DriveWorks.EventFlow.ExecutableNodeBase](topic6938.md))  
![Public Method](dotnetimages/publicMethod.gif)| [GetElement](topic11640.md)| Returns a deep copy of this task's Xml Element. (Inherited from [DriveWorks.Specification.Task](topic11629.md))  
![Public Method](dotnetimages/publicMethod.gif)| GetLifetimeService|  (Inherited from System.MarshalByRefObject)  
![Public Method](dotnetimages/publicMethod.gif)| [TryGetInputEndpoint](topic6955.md)| Attempts to find an input with the given name. (Inherited from [DriveWorks.EventFlow.ExecutableNodeBase](topic6938.md))  
![Public Method](dotnetimages/publicMethod.gif)| [TryGetOutputEndpoint](topic11646.md)| Attempts to retrieve the end point with the given name. (Inherited from [DriveWorks.Specification.Task](topic11629.md))  
Top

# ![](dotnetimages/collapse.gif)Protected Methods

| Name| Description  
---|---|---  
![Protected Method](dotnetimages/protectedMethod.gif)| [AssertNotDeleted](topic11635.md)| Throws an instance of the [DriveWorks.ItemDeletedException](topic3549.md) if the item has been deleted. (Inherited from [DriveWorks.Specification.Task](topic11629.md))  
![Protected Method](dotnetimages/protectedMethod.gif)| [DeleteCore](topic11637.md)| Performs any clean-up required when overridden by a derived class. (Inherited from [DriveWorks.Specification.Task](topic11629.md))  
![Protected Method](dotnetimages/protectedMethod.gif)| [Execute](topic12140.md)| Overridden.   
![Protected Method](dotnetimages/protectedMethod.gif)| [ExecuteNodeCore](topic6944.md)|  (Inherited from [DriveWorks.EventFlow.ExecutableNodeBase](topic6938.md))  
![Protected Method](dotnetimages/protectedMethod.gif)| [GetConfirmationMessage](topic11639.md)| When overridden by a derived class, gets a confirmation message which should be shown to an interactive user before executing the task sequence to which task belongs. (Inherited from [DriveWorks.Specification.Task](topic11629.md))  
![Protected Method](dotnetimages/protectedMethod.gif)| [InitializeMetadata](topic11641.md)| Called when the backing store for this task has been initialized and the meta data is available to be read. (Inherited from [DriveWorks.Specification.Task](topic11629.md))  
![Protected Method](dotnetimages/protectedMethod.gif)| [IsDeferred](topic11642.md)| Determines whether the task should be executed after the design master for the specification is saved. (Inherited from [DriveWorks.Specification.Task](topic11629.md))  
![Protected Method](dotnetimages/protectedMethod.gif)| [IsDeleteContextTask](topic11643.md)| Determines whether the task will be deleting the specification context in it's execution. (Inherited from [DriveWorks.Specification.Task](topic11629.md))  
![Protected Method](dotnetimages/protectedMethod.gif)| [IsRunningRequired](topic11644.md)| Determines whether the task requires the specification context to be open. (Inherited from [DriveWorks.Specification.Task](topic11629.md))  
![Protected Method](dotnetimages/protectedMethod.gif)| MemberwiseClone| Overloaded. (Inherited from System.MarshalByRefObject)  
![Protected Method](dotnetimages/protectedMethod.gif)| [RaiseLeftChanged](topic6946.md)| Raises the [DriveWorks.EventFlow.ExecutableNodeBase.LeftChanged](topic6978.md) event. (Inherited from [DriveWorks.EventFlow.ExecutableNodeBase](topic6938.md))  
![Protected Method](dotnetimages/protectedMethod.gif)| [RaiseNameChanged](topic6947.md)| Raises the [DriveWorks.EventFlow.ExecutableNodeBase.NameChanged](topic6979.md) event. (Inherited from [DriveWorks.EventFlow.ExecutableNodeBase](topic6938.md))  
![Protected Method](dotnetimages/protectedMethod.gif)| [RaiseTopChanged](topic6948.md)| Raises the [DriveWorks.EventFlow.ExecutableNodeBase.TopChanged](topic6981.md) event. (Inherited from [DriveWorks.EventFlow.ExecutableNodeBase](topic6938.md))  
![Protected Method](dotnetimages/protectedMethod.gif)| [RaiseWidthChanged](topic6949.md)|  (Inherited from [DriveWorks.EventFlow.ExecutableNodeBase](topic6938.md))  
![Protected Method](dotnetimages/protectedMethod.gif)| [RequiresSingleContext](topic11645.md)| Determines whether the task can be executed if there is more than one specification selected. (Inherited from [DriveWorks.Specification.Task](topic11629.md))  
![Protected Method](dotnetimages/protectedMethod.gif)| [SetState](topic6950.md)| Overloaded. Sets the result of executing this node. (Inherited from [DriveWorks.EventFlow.ExecutableNodeBase](topic6938.md))  
Top

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[DeleteFileTask Class](topic12134.md)   
[DriveWorks.Specification.StandardTasks Namespace](topic11896.md)

©2024 DriveWorks Ltd. All Rights Reserved.
