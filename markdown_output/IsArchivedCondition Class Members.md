![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
IsArchivedCondition Class Members   
See Also Properties Methods Events [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic11858.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification.StandardConditions Namespace](topic11828.md) : IsArchivedCondition Class  
---  
  
Include Inherited Members    
Include Protected Members  


Glossary Item Box

The following tables list the members exposed by [IsArchivedCondition](topic11858.md).

# ![](dotnetimages/collapse.gif)Public Properties

| Name| Description  
---|---|---  
![Public Property](dotnetimages/publicProperty.gif)| [ExecutionTime](topic6957.md)| Gets the amount of time it took for this node to execute. (Inherited from [DriveWorks.EventFlow.ExecutableNodeBase](topic6938.md))  
![Public Property](dotnetimages/publicProperty.gif)| [FailBehavior](topic10815.md)| Gets/sets the fail behavior of the condition. (Inherited from [DriveWorks.Specification.Condition](topic10804.md))  
![Public Property](dotnetimages/publicProperty.gif)| [FailedOutput](topic10816.md)| The output that gets fulfilled when this condition does not pass. (Inherited from [DriveWorks.Specification.Condition](topic10804.md))  
![Public Property](dotnetimages/publicProperty.gif)| [Flow](topic10817.md)| Gets the flow this node is associated with. (Inherited from [DriveWorks.Specification.Condition](topic10804.md))  
![Public Property](dotnetimages/publicProperty.gif)| [IsDeleted](topic10818.md)| Determines whether the condition has been deleted. (Inherited from [DriveWorks.Specification.Condition](topic10804.md))  
![Public Property](dotnetimages/publicProperty.gif)| [Left](topic10819.md)| Gets the left position of this condition. (Inherited from [DriveWorks.Specification.Condition](topic10804.md))  
![Public Property](dotnetimages/publicProperty.gif)| [NavigationInput](topic10820.md)| Gets the navigation input of this node. (Inherited from [DriveWorks.Specification.Condition](topic10804.md))  
![Public Property](dotnetimages/publicProperty.gif)| [NavigationOutput](topic10821.md)| Gets the navigation output of this node. (Inherited from [DriveWorks.Specification.Condition](topic10804.md))  
![Public Property](dotnetimages/publicProperty.gif)| [Negated](topic10822.md)| Determins whether the condition evaluation is to be negated (have not applied to it). (Inherited from [DriveWorks.Specification.Condition](topic10804.md))  
![Public Property](dotnetimages/publicProperty.gif)| [Outputs](topic10823.md)| Gets a collection of all outputs of this node. (Inherited from [DriveWorks.Specification.Condition](topic10804.md))  
![Public Property](dotnetimages/publicProperty.gif)| [PassedOutput](topic10824.md)| The output that gets fulfilled when this condition passes. (Inherited from [DriveWorks.Specification.Condition](topic10804.md))  
![Public Property](dotnetimages/publicProperty.gif)| [Properties](topic10825.md)| Gets access to the property registration service. (Inherited from [DriveWorks.Specification.Condition](topic10804.md))  
![Public Property](dotnetimages/publicProperty.gif)| [Result](topic6965.md)| Gets the result of this node (if it has executed). (Inherited from [DriveWorks.EventFlow.ExecutableNodeBase](topic6938.md))  
![Public Property](dotnetimages/publicProperty.gif)| [ResultDetails](topic6966.md)| Gets additional information about the result of this node (if it has executed). (Inherited from [DriveWorks.EventFlow.ExecutableNodeBase](topic6938.md))  
![Public Property](dotnetimages/publicProperty.gif)| [State](topic6968.md)| Gets the execution state of this node. (Inherited from [DriveWorks.EventFlow.ExecutableNodeBase](topic6938.md))  
![Public Property](dotnetimages/publicProperty.gif)| [SuppressStandardOutputs](topic10827.md)| Gets whether standard outputs (Passed / Failed) should be suppressed. (Inherited from [DriveWorks.Specification.Condition](topic10804.md))  
![Public Property](dotnetimages/publicProperty.gif)| [Title](topic10828.md)| Gets/sets the human-readable title of the condition. (Inherited from [DriveWorks.Specification.Condition](topic10804.md))  
![Public Property](dotnetimages/publicProperty.gif)| [Top](topic10829.md)| Gets the top position of this condition. (Inherited from [DriveWorks.Specification.Condition](topic10804.md))  
![Public Property](dotnetimages/publicProperty.gif)| [Width](topic10830.md)| Gets/sets the width of the condition. (Inherited from [DriveWorks.Specification.Condition](topic10804.md))  
Top

# ![](dotnetimages/collapse.gif)Protected Properties

| Name| Description  
---|---|---  
![Protected Property](dotnetimages/protectedProperty.gif)| [ReportingClass](topic10826.md)| Gets the class name to be written to the report. (Inherited from [DriveWorks.Specification.Condition](topic10804.md))  
![Protected Property](dotnetimages/protectedProperty.gif)| [ResultReportLevel](topic6967.md)| Gets the reporting level to use when writing the result of this node to the report. (Inherited from [DriveWorks.EventFlow.ExecutableNodeBase](topic6938.md))  
Top

# ![](dotnetimages/collapse.gif)Public Methods

| Name| Description  
---|---|---  
Public Method| CreateObjRef|  (Inherited from System.MarshalByRefObject)  
Public Method| [Delete](topic10811.md)| Deletes the condition. (Inherited from [DriveWorks.Specification.Condition](topic10804.md))  
Public Method| [GetEditor](topic6945.md)| Gets the editor for this node. (Inherited from [DriveWorks.EventFlow.ExecutableNodeBase](topic6938.md))  
Public Method| [GetElement](topic10813.md)| Returns a deep copy of this condition's Xml Element. (Inherited from [DriveWorks.Specification.Condition](topic10804.md))  
Public Method| GetLifetimeService|  (Inherited from System.MarshalByRefObject)  
Public Method| [TryGetInputEndpoint](topic6955.md)| Attempts to find an input with the given name. (Inherited from [DriveWorks.EventFlow.ExecutableNodeBase](topic6938.md))  
Public Method| [TryGetOutputEndpoint](topic10814.md)| Attempts to retrieve the end point with the given name. (Inherited from [DriveWorks.Specification.Condition](topic10804.md))  
Top

# ![](dotnetimages/collapse.gif)Protected Methods

| Name| Description  
---|---|---  
Protected Method| [AssertNotDeleted](topic10810.md)| Throws an instance of the [DriveWorks.ItemDeletedException](topic3549.md) if the item has been deleted. (Inherited from [DriveWorks.Specification.Condition](topic10804.md))  
Protected Method| [DeleteCore](topic10812.md)| Performs any clean-up required when overridden by a derived class. (Inherited from [DriveWorks.Specification.Condition](topic10804.md))  
Protected Method| [ExecuteNodeCore](topic6944.md)|  (Inherited from [DriveWorks.EventFlow.ExecutableNodeBase](topic6938.md))  
Protected Method| MemberwiseClone| Overloaded. (Inherited from System.MarshalByRefObject)  
Protected Method| [RaiseLeftChanged](topic6946.md)| Raises the [DriveWorks.EventFlow.ExecutableNodeBase.LeftChanged](topic6978.md) event. (Inherited from [DriveWorks.EventFlow.ExecutableNodeBase](topic6938.md))  
Protected Method| [RaiseNameChanged](topic6947.md)| Raises the [DriveWorks.EventFlow.ExecutableNodeBase.NameChanged](topic6979.md) event. (Inherited from [DriveWorks.EventFlow.ExecutableNodeBase](topic6938.md))  
Protected Method| [RaiseTopChanged](topic6948.md)| Raises the [DriveWorks.EventFlow.ExecutableNodeBase.TopChanged](topic6981.md) event. (Inherited from [DriveWorks.EventFlow.ExecutableNodeBase](topic6938.md))  
Protected Method| [RaiseWidthChanged](topic6949.md)|  (Inherited from [DriveWorks.EventFlow.ExecutableNodeBase](topic6938.md))  
Protected Method| [SetState](topic6950.md)| Overloaded. Sets the result of executing this node. (Inherited from [DriveWorks.EventFlow.ExecutableNodeBase](topic6938.md))  
Top

# ![](dotnetimages/collapse.gif)Public Events

| Name| Description  
---|---|---  
![Public Event](dotnetimages/publicEvent.gif)| [Deleted](topic10831.md)| Occurs when the condition is deleted. (Inherited from [DriveWorks.Specification.Condition](topic10804.md))  
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

[IsArchivedCondition Class](topic11858.md)   
[DriveWorks.Specification.StandardConditions Namespace](topic11828.md)


