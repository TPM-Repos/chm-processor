![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
ExecutableNodeBase Class Members   
See Also Fields Properties Methods Events [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic6938.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.EventFlow Namespace](topic6871.md) : ExecutableNodeBase Class  
---  
  
Include Inherited Members    
Include Protected Members  


Glossary Item Box

The following tables list the members exposed by [ExecutableNodeBase](topic6938.md).

# ![](dotnetimages/collapse.gif)Public Fields

| Name| Description  
---|---|---  
![Public Field](dotnetimages/publicField.gif)| [MAX_WIDTH](topic6972.md)| The maximum width of the node.   
![Public Field](dotnetimages/publicField.gif)| [MIN_LEFT](topic6973.md)| The minimum allowed value of the [Left](topic6959.md) property.   
![Public Field](dotnetimages/publicField.gif)| [MIN_TOP](topic6974.md)| The minimum allowed value of the [Top](topic6970.md) property.   
![Public Field](dotnetimages/publicField.gif)| [MIN_WIDTH](topic6975.md)| The minimum width of the node.   
Top

# ![](dotnetimages/collapse.gif)Public Properties

| Name| Description  
---|---|---  
![Public Property](dotnetimages/publicProperty.gif)| [ExecutionTime](topic6957.md)| Gets the amount of time it took for this node to execute.   
![Public Property](dotnetimages/publicProperty.gif)| [Flow](topic6958.md)| Gets the flow this node is associated with.   
![Public Property](dotnetimages/publicProperty.gif)| [Left](topic6959.md)| Gets the left position of this node.   
![Public Property](dotnetimages/publicProperty.gif)| [NavigationInput](topic6960.md)| Gets the navigation input of this node.   
![Public Property](dotnetimages/publicProperty.gif)| [NavigationOutput](topic6961.md)| Gets the navigation output of this node.   
![Public Property](dotnetimages/publicProperty.gif)| [Outputs](topic6962.md)| Gets a collection of all outputs of this node.   
![Public Property](dotnetimages/publicProperty.gif)| [Properties](topic6963.md)| Gets access to the property registration service.   
![Public Property](dotnetimages/publicProperty.gif)| [Result](topic6965.md)| Gets the result of this node (if it has executed).   
![Public Property](dotnetimages/publicProperty.gif)| [ResultDetails](topic6966.md)| Gets additional information about the result of this node (if it has executed).   
![Public Property](dotnetimages/publicProperty.gif)| [State](topic6968.md)| Gets the execution state of this node.   
![Public Property](dotnetimages/publicProperty.gif)| [Title](topic6969.md)| Gets/sets the human-readable title of the node.   
![Public Property](dotnetimages/publicProperty.gif)| [Top](topic6970.md)| Gets the top position of this node.   
![Public Property](dotnetimages/publicProperty.gif)| [Width](topic6971.md)| Gets/sets the design time width of this node.   
Top

# ![](dotnetimages/collapse.gif)Protected Properties

| Name| Description  
---|---|---  
![Protected Property](dotnetimages/protectedProperty.gif)| [ReportingClass](topic6964.md)| Gets the class name to use when writing the result to the report.   
![Protected Property](dotnetimages/protectedProperty.gif)| [ResultReportLevel](topic6967.md)| Gets the reporting level to use when writing the result of this node to the report.   
Top

# ![](dotnetimages/collapse.gif)Public Methods

| Name| Description  
---|---|---  
Public Method| CreateObjRef|  (Inherited from System.MarshalByRefObject)  
Public Method| [GetEditor](topic6945.md)| Gets the editor for this node.   
Public Method| GetLifetimeService|  (Inherited from System.MarshalByRefObject)  
Public Method| [TryGetInputEndpoint](topic6955.md)| Attempts to find an input with the given name.   
Public Method| [TryGetOutputEndpoint](topic6956.md)| Attempts to retrieve the output end point with the given name.   
Top

# ![](dotnetimages/collapse.gif)Protected Methods

| Name| Description  
---|---|---  
Protected Method| [ExecuteNodeCore](topic6944.md)|   
Protected Method| MemberwiseClone| Overloaded. (Inherited from System.MarshalByRefObject)  
Protected Method| [RaiseLeftChanged](topic6946.md)| Raises the [LeftChanged](topic6978.md) event.   
Protected Method| [RaiseNameChanged](topic6947.md)| Raises the [NameChanged](topic6979.md) event.   
Protected Method| [RaiseTopChanged](topic6948.md)| Raises the [TopChanged](topic6981.md) event.   
Protected Method| [RaiseWidthChanged](topic6949.md)|   
Protected Method| [SetState](topic6950.md)| Overloaded. Sets the result of executing this node.   
Top

# ![](dotnetimages/collapse.gif)Public Events

| Name| Description  
---|---|---  
![Public Event](dotnetimages/publicEvent.gif)| [ExecutionTimeChanged](topic6976.md)| Occurs whenever the [ExecutionTime](topic6957.md) property's value has changed.   
![Public Event](dotnetimages/publicEvent.gif)| [InputsChanged](topic6977.md)| Occurs whenever a property has been added or removed from the [Properties](topic6963.md) collection.   
![Public Event](dotnetimages/publicEvent.gif)| [LeftChanged](topic6978.md)| Occurs whenever the [Left](topic6959.md) property's value has changed.   
![Public Event](dotnetimages/publicEvent.gif)| [NameChanged](topic6979.md)| Occurs when the name of the node has changed.   
![Public Event](dotnetimages/publicEvent.gif)| [StateChanged](topic6980.md)| Occurs whenever the [State](topic6968.md) property's value has changed.   
![Public Event](dotnetimages/publicEvent.gif)| [TopChanged](topic6981.md)| Occurs whenever the [Top](topic6970.md) property's value has changed.   
![Public Event](dotnetimages/publicEvent.gif)| [WidthChanged](topic6982.md)| Occurs when the width of the node has changed.   
Top

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ExecutableNodeBase Class](topic6938.md)   
[DriveWorks.EventFlow Namespace](topic6871.md)


