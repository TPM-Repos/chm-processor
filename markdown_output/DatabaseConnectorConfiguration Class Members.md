![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
DatabaseConnectorConfiguration Class Members   
See Also Properties Methods [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic6756.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Connectors.Database Namespace](topic6754.md) : DatabaseConnectorConfiguration Class  
---  
  
Include Inherited Members    
Include Protected Members  


Glossary Item Box

The following tables list the members exposed by [DatabaseConnectorConfiguration](topic6756.md).

# ![](dotnetimages/collapse.gif)Public Constructors

| Name| Description  
---|---|---  
![Public Constructor](dotnetimages/publicConstructor.gif)| [DatabaseConnectorConfiguration Constructor](topic6762.md)|   
Top

# ![](dotnetimages/collapse.gif)Public Properties

| Name| Description  
---|---|---  
![Public Property](dotnetimages/publicProperty.gif)| [DataSourceElement](topic6767.md)| Gets/sets the data used for configuring the data source for the connector.   
![Public Property](dotnetimages/publicProperty.gif)| [DataSourceTypeName](topic6768.md)| Get/sets the name of the type that is responsible for configuring the data source for the connector.   
![Public Property](dotnetimages/publicProperty.gif)| [EnabledMachineNames](topic3094.md)| Get/sets A pipe bar delimited list of machine names that have the connector enabled. (Inherited from [DriveWorks.GroupConnectorInformation](topic3084.md))  
![Public Property](dotnetimages/publicProperty.gif)| [Id](topic3095.md)| Gets the identifier value for the connector. (Inherited from [DriveWorks.GroupConnectorInformation](topic3084.md))  
![Public Property](dotnetimages/publicProperty.gif)| [IdFieldName](topic6769.md)| Gets/set the name of the field that contains a unique identifier for each row.   
![Public Property](dotnetimages/publicProperty.gif)| [Inputs](topic6770.md)| Gets the input bindings used in this configuration.   
![Public Property](dotnetimages/publicProperty.gif)| [Name](topic3096.md)| Gets/sets the unique name for the connector. (Inherited from [DriveWorks.GroupConnectorInformation](topic3084.md))  
![Public Property](dotnetimages/publicProperty.gif)| [OperationFieldName](topic6771.md)| Gets/sets the name of the optional field that contains the name of the operation to invoke.   
![Public Property](dotnetimages/publicProperty.gif)| [OperationName](topic6772.md)| Gets/sets the name of the operation to invoke.   
![Public Property](dotnetimages/publicProperty.gif)| [ProcessFailedValue](topic6773.md)| Gets/sets the value that indicates that a row has failed to be processed into a specification.   
![Public Property](dotnetimages/publicProperty.gif)| [ProcessFieldName](topic6774.md)| Gets/sets the name of the field that contains the process state information.   
![Public Property](dotnetimages/publicProperty.gif)| [ProcessingValue](topic6775.md)| Gets/sets the value that indicates that a row is being processed currently.   
![Public Property](dotnetimages/publicProperty.gif)| [ProcessSuccessValue](topic6776.md)| Gets/sets the value that indicates that a row has been successfully processed into a specification.   
![Public Property](dotnetimages/publicProperty.gif)| [ProjectFieldName](topic6777.md)| Gets/sets the optional field name that will contain the name of the project to create specifications from.   
![Public Property](dotnetimages/publicProperty.gif)| [ProjectName](topic6778.md)| Gets/sets the name of the project to create specifications from if the project field could not be used.   
![Public Property](dotnetimages/publicProperty.gif)| [SpecificationId](topic6779.md)| Gets/sets the id of the specification to modify.   
![Public Property](dotnetimages/publicProperty.gif)| [SpecificationIdFieldName](topic6780.md)| Gets/sets the optional field name that will contain the id of the specification to modify.   
![Public Property](dotnetimages/publicProperty.gif)| [SpecificationName](topic6781.md)| Gets/sets the name of the specification to modify.   
![Public Property](dotnetimages/publicProperty.gif)| [SpecificationNameFieldName](topic6782.md)| Gets/sets the optional field name that will contain the name of the specification to modify.   
![Public Property](dotnetimages/publicProperty.gif)| [TableName](topic6783.md)| Gets/sets the name of the table that will be read from.   
![Public Property](dotnetimages/publicProperty.gif)| [TimerInterval](topic6784.md)| Gets/sets the time between checks to the database for new data to process.   
![Public Property](dotnetimages/publicProperty.gif)| [ToProcessValue](topic6785.md)| Gets/sets the value that indicates that a row is ready to be processed by this connector.   
![Public Property](dotnetimages/publicProperty.gif)| [TransitionFieldName](topic6786.md)| Gets/sets the name of the optional field that contains the name of the transition to invoke to close the specification.   
![Public Property](dotnetimages/publicProperty.gif)| [TransitionName](topic6787.md)| Gets/sets the name of the transition to invoke if transition field could not be used.   
Top

# ![](dotnetimages/collapse.gif)Protected Properties

| Name| Description  
---|---|---  
![Protected Property](dotnetimages/protectedProperty.gif)| [Data](topic3093.md)| Gets/sets Value used by connector containing configuration information. (Inherited from [DriveWorks.GroupConnectorInformation](topic3084.md))  
Top

# ![](dotnetimages/collapse.gif)Public Methods

| Name| Description  
---|---|---  
![Public Method](dotnetimages/publicMethod.gif)| [AddInput](topic6763.md)| Adds a new input bindings for this configuration.   
![Public Method](dotnetimages/publicMethod.gif)| [ClearInputs](topic6764.md)| Removes all input bindings from this configuration.   
![Public Method](dotnetimages/publicMethod.gif)| CreateObjRef|  (Inherited from System.MarshalByRefObject)  
![Public Method](dotnetimages/publicMethod.gif)| [GetClone](topic3091.md)| Creates a cloned version of this object. (Inherited from [DriveWorks.GroupConnectorInformation](topic3084.md))  
![Public Method](dotnetimages/publicMethod.gif)| GetLifetimeService|  (Inherited from System.MarshalByRefObject)  
Top

# ![](dotnetimages/collapse.gif)Protected Methods

| Name| Description  
---|---|---  
![Protected Method](dotnetimages/protectedMethod.gif)| [EnsureDataStored](topic6765.md)| Overridden.   
![Protected Method](dotnetimages/protectedMethod.gif)| MemberwiseClone| Overloaded. (Inherited from System.MarshalByRefObject)  
![Protected Method](dotnetimages/protectedMethod.gif)| [OnInitialized](topic6766.md)| Overridden.   
Top

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[DatabaseConnectorConfiguration Class](topic6756.md)   
[DriveWorks.Connectors.Database Namespace](topic6754.md)


