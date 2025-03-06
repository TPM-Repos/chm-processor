![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
ConditionOutput Class Members   
See Also Properties Methods Events [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic6901.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.EventFlow Namespace](topic6871.md) : ConditionOutput Class  
---  
  
Include Inherited Members    
Include Protected Members  


Glossary Item Box

The following tables list the members exposed by [ConditionOutput](topic6901.md).

# ![](dotnetimages/collapse.gif)Public Properties

| Name| Description  
---|---|---  
![Public Property](dotnetimages/publicProperty.gif)| [Collection](topic6924.md)| Gets the collection this end point is a part of. (Inherited from [DriveWorks.EventFlow.ConnectionEndpoint](topic6918.md))  
![Public Property](dotnetimages/publicProperty.gif)| [Description](topic6925.md)| The localized description of this end point. (Inherited from [DriveWorks.EventFlow.ConnectionEndpoint](topic6918.md))  
![Public Property](dotnetimages/publicProperty.gif)| [DisplayName](topic6926.md)| Gets the user-friendly display name of this end point. (Inherited from [DriveWorks.EventFlow.ConnectionEndpoint](topic6918.md))  
![Public Property](dotnetimages/publicProperty.gif)| [IsFulfilled](topic7082.md)| Gets whether this output has been given a value. (Inherited from [DriveWorks.EventFlow.NodeOutput](topic7074.md))  
![Public Property](dotnetimages/publicProperty.gif)| [Name](topic6927.md)| The name of the end point. (Inherited from [DriveWorks.EventFlow.ConnectionEndpoint](topic6918.md))  
![Public Property](dotnetimages/publicProperty.gif)| [Node](topic6928.md)| Gets the node this data end point belongs to. (Inherited from [DriveWorks.EventFlow.ConnectionEndpoint](topic6918.md))  
![Public Property](dotnetimages/publicProperty.gif)| [Unlocked](topic6908.md)| Gets whether this condition path has been unlocked.   
![Public Property](dotnetimages/publicProperty.gif)| [Value](topic7083.md)| Gets the value of this output. (Inherited from [DriveWorks.EventFlow.NodeOutput](topic7074.md))  
![Public Property](dotnetimages/publicProperty.gif)| [ValueType](topic6929.md)| The underlying CLR type of the end point. (Inherited from [DriveWorks.EventFlow.ConnectionEndpoint](topic6918.md))  
Top

# ![](dotnetimages/collapse.gif)Public Methods

| Name| Description  
---|---|---  
![Public Method](dotnetimages/publicMethod.gif)| CreateObjRef|  (Inherited from System.MarshalByRefObject)  
![Public Method](dotnetimages/publicMethod.gif)| [Fulfill](topic7080.md)| Assign a static value to this input. (Inherited from [DriveWorks.EventFlow.NodeOutput](topic7074.md))  
![Public Method](dotnetimages/publicMethod.gif)| [GetConnections](topic7081.md)| Gets all connections that has been made to this output. (Inherited from [DriveWorks.EventFlow.NodeOutput](topic7074.md))  
![Public Method](dotnetimages/publicMethod.gif)| GetLifetimeService|  (Inherited from System.MarshalByRefObject)  
![Public Method](dotnetimages/publicMethod.gif)| [Unlock](topic6907.md)| Unlocks this condition path. Letting the [IFlowNode](topic6873.md) execution engine know that it should follow the connections made to this output.   
Top

# ![](dotnetimages/collapse.gif)Protected Methods

| Name| Description  
---|---|---  
![Protected Method](dotnetimages/protectedMethod.gif)| MemberwiseClone| Overloaded. (Inherited from System.MarshalByRefObject)  
Top

# ![](dotnetimages/collapse.gif)Public Events

| Name| Description  
---|---|---  
![Public Event](dotnetimages/publicEvent.gif)| [ConnectionAdded](topic7084.md)| Raised whenever a connection has been made to this output. (Inherited from [DriveWorks.EventFlow.NodeOutput](topic7074.md))  
![Public Event](dotnetimages/publicEvent.gif)| [ConnectionRemoved](topic7085.md)| Raised whenever a connection has been removed from this output. (Inherited from [DriveWorks.EventFlow.NodeOutput](topic7074.md))  
![Public Event](dotnetimages/publicEvent.gif)| [ValueChanged](topic7086.md)| Raised whenever the value of this output has been set. (Inherited from [DriveWorks.EventFlow.NodeOutput](topic7074.md))  
Top

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ConditionOutput Class](topic6901.md)   
[DriveWorks.EventFlow Namespace](topic6871.md)

©2024 DriveWorks Ltd. All Rights Reserved.
