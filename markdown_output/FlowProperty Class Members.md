![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
FlowProperty Class Members   
See Also Properties Methods Events [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic10946.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) : FlowProperty Class  
---  
  
Include Inherited Members    
Include Protected Members  


Glossary Item Box

The following tables list the members exposed by [FlowProperty](topic10946.md).

# ![](dotnetimages/collapse.gif)Public Properties

| Name| Description  
---|---|---  
![Public Property](dotnetimages/publicProperty.gif)| [Category](topic10965.md)| Gets the category to which the property belongs.   
![Public Property](dotnetimages/publicProperty.gif)| [Collection](topic6924.md)| Gets the collection this end point is a part of. (Inherited from [DriveWorks.EventFlow.ConnectionEndpoint](topic6918.md))  
![Public Property](dotnetimages/publicProperty.gif)| [Connection](topic10966.md)| Gets the connection that's been created for this property, or a null reference if no connection has been made.   
![Public Property](dotnetimages/publicProperty.gif)| [DefaultValue](topic10968.md)| Gets the default value of the property.   
![Public Property](dotnetimages/publicProperty.gif)| [Description](topic6925.md)| The localized description of this end point. (Inherited from [DriveWorks.EventFlow.ConnectionEndpoint](topic6918.md))  
![Public Property](dotnetimages/publicProperty.gif)| [DisplayName](topic6926.md)| Gets the user-friendly display name of this end point. (Inherited from [DriveWorks.EventFlow.ConnectionEndpoint](topic6918.md))  
![Public Property](dotnetimages/publicProperty.gif)| [HasValue](topic10969.md)| Gets whether a value has been given to this property.   
![Public Property](dotnetimages/publicProperty.gif)| [Id](topic10970.md)| Gets the invariant identifier of the rule.   
![Public Property](dotnetimages/publicProperty.gif)| [Info](topic10971.md)| Gets information about the property.   
![Public Property](dotnetimages/publicProperty.gif)| [IsBound](topic10972.md)| Determines whether the property value is bound to a rule.   
![Public Property](dotnetimages/publicProperty.gif)| [IsConnected](topic10973.md)| Gets whether a connection has been made to this property.   
![Public Property](dotnetimages/publicProperty.gif)| [IsRequired](topic10974.md)| Gets whether this input is required for the owning task to execute.   
![Public Property](dotnetimages/publicProperty.gif)| [Name](topic10975.md)| Overridden. Gets the name of the property.   
![Public Property](dotnetimages/publicProperty.gif)| [Node](topic6928.md)| Gets the node this data end point belongs to. (Inherited from [DriveWorks.EventFlow.ConnectionEndpoint](topic6918.md))  
![Public Property](dotnetimages/publicProperty.gif)| [ValueType](topic6929.md)| The underlying CLR type of the end point. (Inherited from [DriveWorks.EventFlow.ConnectionEndpoint](topic6918.md))  
Top

# ![](dotnetimages/collapse.gif)Protected Properties

| Name| Description  
---|---|---  
![Protected Property](dotnetimages/protectedProperty.gif)| [DataElement](topic10967.md)|   
Top

# ![](dotnetimages/collapse.gif)Public Methods

| Name| Description  
---|---|---  
Public Method| [Bind](topic10952.md)| Overloaded. Binds the property to a rule.   
Public Method| [Connect](topic10955.md)| Overridden. Connects this input to the given output.   
Public Method| [ConvertToNativeType](topic10956.md)| Takes the given object and converts it into the native type of the property.   
Public Method| CreateObjRef|  (Inherited from System.MarshalByRefObject)  
Public Method| [Disconnect](topic10957.md)|   
Public Method| GetLifetimeService|  (Inherited from System.MarshalByRefObject)  
Public Method| [GetValue](topic10958.md)| Gets the value of the property.   
Public Method| [GetVersionHistory](topic10959.md)|   
Public Method| [SetValue](topic10963.md)| Sets the value of the property.   
Public Method| [Unbind](topic10964.md)| Unbinds the property.   
Top

# ![](dotnetimages/collapse.gif)Protected Methods

| Name| Description  
---|---|---  
Protected Method| [InitializeCore](topic10960.md)|   
Protected Method| MemberwiseClone| Overloaded. (Inherited from System.MarshalByRefObject)  
Protected Method| [RaiseConnectionAdded](topic7040.md)| Raises the [DriveWorks.EventFlow.InputConnectionEndpoint.ConnectionAdded](topic7042.md) event. (Inherited from [DriveWorks.EventFlow.InputConnectionEndpoint](topic7033.md))  
Protected Method| [RaiseConnectionRemoved](topic7041.md)| Raises the [DriveWorks.EventFlow.InputConnectionEndpoint.ConnectionRemoved](topic7043.md) event. (Inherited from [DriveWorks.EventFlow.InputConnectionEndpoint](topic7033.md))  
Protected Method| [RaiseRuleChanged](topic10961.md)| Raises the [RuleChanged](topic10976.md) event.   
Protected Method| [RaiseValueChanged](topic10962.md)| Raises the [ValueChanged](topic10977.md) event.   
Top

# ![](dotnetimages/collapse.gif)Public Events

| Name| Description  
---|---|---  
![Public Event](dotnetimages/publicEvent.gif)| [ConnectionAdded](topic7042.md)| Occurs when a connection has been added to this input. (Inherited from [DriveWorks.EventFlow.InputConnectionEndpoint](topic7033.md))  
![Public Event](dotnetimages/publicEvent.gif)| [ConnectionRemoved](topic7043.md)| Occurs when a connection has been removed from this input. (Inherited from [DriveWorks.EventFlow.InputConnectionEndpoint](topic7033.md))  
![Public Event](dotnetimages/publicEvent.gif)| [RuleChanged](topic10976.md)| Raised when the rule for this flow property is changed.   
![Public Event](dotnetimages/publicEvent.gif)| [ValueChanged](topic10977.md)| Raised when the value for this flow property is changed.   
Top

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[FlowProperty Class](topic10946.md)   
[DriveWorks.Specification Namespace](topic10764.md)


