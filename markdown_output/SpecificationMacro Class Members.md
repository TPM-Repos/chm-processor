SpecificationMacro Class Members   
See Also Properties Methods Events [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic11429.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) : SpecificationMacro Class  
---  
  
Include Inherited Members    
Include Protected Members  


Glossary Item Box

The following tables list the members exposed by [SpecificationMacro](topic11429.md).

# Public Properties

| Name| Description  
---|---|---  
![Public Property](dotnetimages/publicProperty.gif)| [Conditions](topic11443.md)| Gets the conditions in this macro.   
![Public Property](dotnetimages/publicProperty.gif)| [ConsistencyLevel](topic11444.md)| Gets the consistency-level of the macro.   
![Public Property](dotnetimages/publicProperty.gif)| [HasExecuted](topic7006.md)| Gets whether this flow has executed. (Inherited from [DriveWorks.EventFlow.FlowBase](topic6999.md))  
![Public Property](dotnetimages/publicProperty.gif)| [IsDeleted](topic11445.md)| Determines whether the macro has been deleted.   
![Public Property](dotnetimages/publicProperty.gif)| [Name](topic11446.md)| Overridden. Gets the name of the macro.   
![Public Property](dotnetimages/publicProperty.gif)| [Nodes](topic11447.md)| Overridden. Gets all flow nodes in this specification macro.   
![Public Property](dotnetimages/publicProperty.gif)| [Parent](topic11448.md)| Gets/sets the category to which the macro belongs.   
![Public Property](dotnetimages/publicProperty.gif)| [StartNode](topic11449.md)| Overridden. Gets the first node that will execute when this macro executes as a part of a flow.   
![Public Property](dotnetimages/publicProperty.gif)| [Tasks](topic11450.md)| Gets/sets the tasks which make up the macro.   
Top

# Public Methods

| Name| Description  
---|---|---  
Public Method| CreateObjRef|  (Inherited from System.MarshalByRefObject)  
Public Method| [Delete](topic11435.md)| Deletes the macro.   
Public Method| [Execute](topic11436.md)| Executes the macro.   
Public Method| GetLifetimeService|  (Inherited from System.MarshalByRefObject)  
Public Method| [Save](topic11438.md)| Overloaded. Saves the macro to a string.   
Public Method| [Serialize](topic11441.md)| Serializes this [SpecificationMacro](topic11429.md) to the provided System.Xml.XmlWriter.   
Public Method| [TryGetNode](topic11442.md)| Overridden.   
Top

# Protected Methods

| Name| Description  
---|---|---  
Protected Method| MemberwiseClone| Overloaded. (Inherited from System.MarshalByRefObject)  
Protected Method| [RaiseCategoryChanged](topic11437.md)|   
Top

# Public Events

| Name| Description  
---|---|---  
![Public Event](dotnetimages/publicEvent.gif)| [ConnectionsChanged](topic11451.md)| Raised whenever a connection between a property and an output in this macro has been created or removed.   
![Public Event](dotnetimages/publicEvent.gif)| [ConsistencyLevelChanged](topic11452.md)| Raised when the [ConsistencyLevel](topic11444.md) property is changed.   
![Public Event](dotnetimages/publicEvent.gif)| [Deleted](topic11453.md)| Raised when the macro is deleted.   
![Public Event](dotnetimages/publicEvent.gif)| [Executed](topic7010.md)| Raised when this flow has been executed and can no longer be edited. (Inherited from [DriveWorks.EventFlow.FlowBase](topic6999.md))  
![Public Event](dotnetimages/publicEvent.gif)| [NameChanged](topic11454.md)| Raised when the [Name](topic11446.md) property is changed.   
![Public Event](dotnetimages/publicEvent.gif)| [ParentChanged](topic11455.md)| Raised when the category is changed.   
Top

# See Also

#### Reference

[SpecificationMacro Class](topic11429.md)   
[DriveWorks.Specification Namespace](topic10764.md)


