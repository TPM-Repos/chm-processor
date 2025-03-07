Collapse All Expand All Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
NodeNavigationInput Class Members   
See Also Properties Methods Events [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic7058.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.EventFlow Namespace](topic6871.md) : NodeNavigationInput Class  
---  
  
Include Inherited Members    
Include Protected Members  


Glossary Item Box

The following tables list the members exposed by [NodeNavigationInput](topic7058.md).

# Public Properties

| Name| Description  
---|---|---  
![Public Property](dotnetimages/publicProperty.gif)| [Collection](topic6924.md)| Gets the collection this end point is a part of. (Inherited from [DriveWorks.EventFlow.ConnectionEndpoint](topic6918.md))  
![Public Property](dotnetimages/publicProperty.gif)| [Connections](topic7066.md)| Gets a collection of all connections that have been made to this input.   
![Public Property](dotnetimages/publicProperty.gif)| [Description](topic6925.md)| The localized description of this end point. (Inherited from [DriveWorks.EventFlow.ConnectionEndpoint](topic6918.md))  
![Public Property](dotnetimages/publicProperty.gif)| [DisplayName](topic6926.md)| Gets the user-friendly display name of this end point. (Inherited from [DriveWorks.EventFlow.ConnectionEndpoint](topic6918.md))  
![Public Property](dotnetimages/publicProperty.gif)| [Name](topic6927.md)| The name of the end point. (Inherited from [DriveWorks.EventFlow.ConnectionEndpoint](topic6918.md))  
![Public Property](dotnetimages/publicProperty.gif)| [Node](topic6928.md)| Gets the node this data end point belongs to. (Inherited from [DriveWorks.EventFlow.ConnectionEndpoint](topic6918.md))  
![Public Property](dotnetimages/publicProperty.gif)| [ValueType](topic6929.md)| The underlying CLR type of the end point. (Inherited from [DriveWorks.EventFlow.ConnectionEndpoint](topic6918.md))  
Top

# Public Methods

| Name| Description  
---|---|---  
Public Method| [Connect](topic7064.md)| Overridden. Create a connection between this input and the given [NodeOutput](topic7074.md), scheduling the [IFlowNode](topic6873.md) that owns this input to be executed if the mapped output is fulfilled during execution.   
Public Method| CreateObjRef|  (Inherited from System.MarshalByRefObject)  
Public Method| [Disconnect](topic7065.md)| Removes the given connection from this input.   
Public Method| GetLifetimeService|  (Inherited from System.MarshalByRefObject)  
Top

# Protected Methods

| Name| Description  
---|---|---  
Protected Method| MemberwiseClone| Overloaded. (Inherited from System.MarshalByRefObject)  
Protected Method| [RaiseConnectionAdded](topic7040.md)| Raises the [ConnectionAdded](topic7042.md) event. (Inherited from [DriveWorks.EventFlow.InputConnectionEndpoint](topic7033.md))  
Protected Method| [RaiseConnectionRemoved](topic7041.md)| Raises the [ConnectionRemoved](topic7043.md) event. (Inherited from [DriveWorks.EventFlow.InputConnectionEndpoint](topic7033.md))  
Top

# Public Events

| Name| Description  
---|---|---  
![Public Event](dotnetimages/publicEvent.gif)| [ConnectionAdded](topic7042.md)| Occurs when a connection has been added to this input. (Inherited from [DriveWorks.EventFlow.InputConnectionEndpoint](topic7033.md))  
![Public Event](dotnetimages/publicEvent.gif)| [ConnectionRemoved](topic7043.md)| Occurs when a connection has been removed from this input. (Inherited from [DriveWorks.EventFlow.InputConnectionEndpoint](topic7033.md))  
Top

# See Also

#### Reference

[NodeNavigationInput Class](topic7058.md)   
[DriveWorks.EventFlow Namespace](topic6871.md)


