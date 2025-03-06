![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
CompleteChildSpecificationTask Class Members   
See Also Properties Methods Events [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic12027.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification.StandardTasks Namespace](topic11896.md) : CompleteChildSpecificationTask Class  
---  
  
Include Inherited Members    
Include Protected Members  


Glossary Item Box

The following tables list the members exposed by [CompleteChildSpecificationTask](topic12027.md).

# ![](dotnetimages/collapse.gif)Public Properties

| Name| Description  
---|---|---  
![Public Property](dotnetimages/publicProperty.gif)| [Conditions](topic11647.md)| Gets a condition manager which can be used to add and work with conditions which can control whether the task gets executed. (Inherited from [DriveWorks.Specification.Task](topic11629.md))  
![Public Property](dotnetimages/publicProperty.gif)| [ExecutionTime](topic6957.md)| Gets the amount of time it took for this node to execute. (Inherited from [DriveWorks.EventFlow.ExecutableNodeBase](topic6938.md))  
![Public Property](dotnetimages/publicProperty.gif)| [FailedOutput](topic6996.md)| Gets the end point that allows logical navigation connections to be made from this node when this node fails during execution. (Inherited from [DriveWorks.EventFlow.ExecutableNodeWithStatus](topic6990.md))  
![Public Property](dotnetimages/publicProperty.gif)| [Flow](topic11648.md)| Gets the [DriveWorks.EventFlow.FlowBase](topic6999.md) that owns this Task. (Inherited from [DriveWorks.Specification.Task](topic11629.md))  
![Public Property](dotnetimages/publicProperty.gif)| [Left](topic11649.md)| Gets the left position of this task. (Inherited from [DriveWorks.Specification.Task](topic11629.md))  
![Public Property](dotnetimages/publicProperty.gif)| [NavigationInput](topic11650.md)| Gets the end point that allows logical navigation connections to be made to this task. (Inherited from [DriveWorks.Specification.Task](topic11629.md))  
![Public Property](dotnetimages/publicProperty.gif)| [NavigationOutput](topic11651.md)| Gets the end point that allows logical navigation connections to be made from this task. (Inherited from [DriveWorks.Specification.Task](topic11629.md))  
![Public Property](dotnetimages/publicProperty.gif)| [Outputs](topic11652.md)| Gets the collection of all outputs that belong to this task. (Inherited from [DriveWorks.Specification.Task](topic11629.md))  
![Public Property](dotnetimages/publicProperty.gif)| [Properties](topic11653.md)| Gets access to the property registration service. (Inherited from [DriveWorks.Specification.Task](topic11629.md))  
![Public Property](dotnetimages/publicProperty.gif)| [Result](topic6965.md)| Gets the result of this node (if it has executed). (Inherited from [DriveWorks.EventFlow.ExecutableNodeBase](topic6938.md))  
![Public Property](dotnetimages/publicProperty.gif)| [ResultDetails](topic6966.md)| Gets additional information about the result of this node (if it has executed). (Inherited from [DriveWorks.EventFlow.ExecutableNodeBase](topic6938.md))  
![Public Property](dotnetimages/publicProperty.gif)| [State](topic6968.md)| Gets the execution state of this node. (Inherited from [DriveWorks.EventFlow.ExecutableNodeBase](topic6938.md))  
![Public Property](dotnetimages/publicProperty.gif)| [SuccessOutput](topic6997.md)| Gets the end point that allows logical navigation connections to be made from this node when this node successfully executes. (Inherited from [DriveWorks.EventFlow.ExecutableNodeWithStatus](topic6990.md))  
![Public Property](dotnetimages/publicProperty.gif)| [Title](topic11655.md)| Gets/sets the human-readable title of the task. (Inherited from [DriveWorks.Specification.Task](topic11629.md))  
![Public Property](dotnetimages/publicProperty.gif)| [Top](topic11656.md)| Gets the top position of this task. (Inherited from [DriveWorks.Specification.Task](topic11629.md))  
![Public Property](dotnetimages/publicProperty.gif)| [WarningOutput](topic6998.md)| Gets the end point that allows logical navigation connections to be made from this node when this node produces a warning as it's state. (Inherited from [DriveWorks.EventFlow.ExecutableNodeWithStatus](topic6990.md))  
![Public Property](dotnetimages/publicProperty.gif)| [Width](topic11657.md)| Gets/sets the width of the task. (Inherited from [DriveWorks.Specification.Task](topic11629.md))  
Top

# ![](dotnetimages/collapse.gif)Protected Properties

| Name| Description  
---|---|---  
![Protected Property](dotnetimages/protectedProperty.gif)| [ReportingClass](topic12035.md)| Overridden. Gets the class name used for reporting.   
![Protected Property](dotnetimages/protectedProperty.gif)| [ResultReportLevel](topic6967.md)| Gets the reporting level to use when writing the result of this node to the report. (Inherited from [DriveWorks.EventFlow.ExecutableNodeBase](topic6938.md))  
Top

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
![Protected Method](dotnetimages/protectedMethod.gif)| [Execute](topic12033.md)| Overridden.   
![Protected Method](dotnetimages/protectedMethod.gif)| [ExecuteNodeCore](topic6944.md)|  (Inherited from [DriveWorks.EventFlow.ExecutableNodeBase](topic6938.md))  
![Protected Method](dotnetimages/protectedMethod.gif)| [GetConfirmationMessage](topic11639.md)| When overridden by a derived class, gets a confirmation message which should be shown to an interactive user before executing the task sequence to which task belongs. (Inherited from [DriveWorks.Specification.Task](topic11629.md))  
![Protected Method](dotnetimages/protectedMethod.gif)| [InitializeMetadata](topic11641.md)| Called when the backing store for this task has been initialized and the meta data is available to be read. (Inherited from [DriveWorks.Specification.Task](topic11629.md))  
![Protected Method](dotnetimages/protectedMethod.gif)| [IsDeferred](topic11642.md)| Determines whether the task should be executed after the design master for the specification is saved. (Inherited from [DriveWorks.Specification.Task](topic11629.md))  
![Protected Method](dotnetimages/protectedMethod.gif)| [IsDeleteContextTask](topic11643.md)| Determines whether the task will be deleting the specification context in it's execution. (Inherited from [DriveWorks.Specification.Task](topic11629.md))  
![Protected Method](dotnetimages/protectedMethod.gif)| [IsRunningRequired](topic12034.md)| Overridden.   
![Protected Method](dotnetimages/protectedMethod.gif)| MemberwiseClone| Overloaded. (Inherited from System.MarshalByRefObject)  
![Protected Method](dotnetimages/protectedMethod.gif)| [RaiseLeftChanged](topic6946.md)| Raises the [DriveWorks.EventFlow.ExecutableNodeBase.LeftChanged](topic6978.md) event. (Inherited from [DriveWorks.EventFlow.ExecutableNodeBase](topic6938.md))  
![Protected Method](dotnetimages/protectedMethod.gif)| [RaiseNameChanged](topic6947.md)| Raises the [DriveWorks.EventFlow.ExecutableNodeBase.NameChanged](topic6979.md) event. (Inherited from [DriveWorks.EventFlow.ExecutableNodeBase](topic6938.md))  
![Protected Method](dotnetimages/protectedMethod.gif)| [RaiseTopChanged](topic6948.md)| Raises the [DriveWorks.EventFlow.ExecutableNodeBase.TopChanged](topic6981.md) event. (Inherited from [DriveWorks.EventFlow.ExecutableNodeBase](topic6938.md))  
![Protected Method](dotnetimages/protectedMethod.gif)| [RaiseWidthChanged](topic6949.md)|  (Inherited from [DriveWorks.EventFlow.ExecutableNodeBase](topic6938.md))  
![Protected Method](dotnetimages/protectedMethod.gif)| [RequiresSingleContext](topic11645.md)| Determines whether the task can be executed if there is more than one specification selected. (Inherited from [DriveWorks.Specification.Task](topic11629.md))  
![Protected Method](dotnetimages/protectedMethod.gif)| [SetState](topic6950.md)| Overloaded. Sets the result of executing this node. (Inherited from [DriveWorks.EventFlow.ExecutableNodeBase](topic6938.md))  
Top

# ![](dotnetimages/collapse.gif)Public Events

| Name| Description  
---|---|---  
![Public Event](dotnetimages/publicEvent.gif)| [Deleted](topic11658.md)| Occurs when the task is deleted. (Inherited from [DriveWorks.Specification.Task](topic11629.md))  
![Public Event](dotnetimages/publicEvent.gif)| [ExecutionTimeChanged](topic6976.md)| Occurs whenever the [DriveWorks.EventFlow.ExecutableNodeBase.ExecutionTime](topic6957.md) property's value has changed. (Inherited from [DriveWorks.EventFlow.ExecutableNodeBase](topic6938.md))  
![Public Event](dotnetimages/publicEvent.gif)| [InputsChanged](topic6977.md)| Occurs whenever a property has been added or removed from the [DriveWorks.EventFlow.ExecutableNodeBase.Properties](topic6963.md) collection. (Inherited from [DriveWorks.EventFlow.ExecutableNodeBase](topic6938.md))  
![Public Event](dotnetimages/publicEvent.gif)| [LeftChanged](topic6978.md)| Occurs whenever the [DriveWorks.EventFlow.ExecutableNodeBase.Left](topic6959.md) property's value has changed. (Inherited from [DriveWorks.EventFlow.ExecutableNodeBase](topic6938.md))  
![Public Event](dotnetimages/publicEvent.gif)| [NameChanged](topic6979.md)| Occurs when the name of the node has changed. (Inherited from [DriveWorks.EventFlow.ExecutableNodeBase](topic6938.md))  
![Public Event](dotnetimages/publicEvent.gif)| [StateChanged](topic6980.md)| Occurs whenever the [DriveWorks.EventFlow.ExecutableNodeBase.State](topic6968.md) property's value has changed. (Inherited from [DriveWorks.EventFlow.ExecutableNodeBase](topic6938.md))  
![Public Event](dotnetimages/publicEvent.gif)| [TopChanged](topic6981.md)| Occurs whenever the [DriveWorks.EventFlow.ExecutableNodeBase.Top](topic6970.md) property's value has changed. (Inherited from [DriveWorks.EventFlow.ExecutableNodeBase](topic6938.md))  
![Public Event](dotnetimages/publicEvent.gif)| [WidthChanged](topic6982.md)| Occurs when the width of the node has changed. (Inherited from [DriveWorks.EventFlow.ExecutableNodeBase](topic6938.md))  
Top

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[CompleteChildSpecificationTask Class](topic12027.md)   
[DriveWorks.Specification.StandardTasks Namespace](topic11896.md)


