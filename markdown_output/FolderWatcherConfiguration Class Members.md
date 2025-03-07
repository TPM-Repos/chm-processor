Collapse All Expand All Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
FolderWatcherConfiguration Class Members   
See Also Properties Methods [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic6823.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Connectors.Folder Namespace](topic6821.md) : FolderWatcherConfiguration Class  
---  
  
Include Inherited Members    
Include Protected Members  


Glossary Item Box

The following tables list the members exposed by [FolderWatcherConfiguration](topic6823.md).

# Public Constructors

| Name| Description  
---|---|---  
![Public Constructor](dotnetimages/publicConstructor.gif)| [FolderWatcherConfiguration Constructor](topic6829.md)|   
Top

# Public Properties

| Name| Description  
---|---|---  
![Public Property](dotnetimages/publicProperty.gif)| [EnabledMachineNames](topic3094.md)| Get/sets A pipe bar delimited list of machine names that have the connector enabled. (Inherited from [DriveWorks.GroupConnectorInformation](topic3084.md))  
![Public Property](dotnetimages/publicProperty.gif)| [FailedFolder](topic6832.md)| Gets/sets where files that are have been scanned and unsuccessfully used/rejected will be moved into.   
![Public Property](dotnetimages/publicProperty.gif)| [Id](topic3095.md)| Gets the identifier value for the connector. (Inherited from [DriveWorks.GroupConnectorInformation](topic3084.md))  
![Public Property](dotnetimages/publicProperty.gif)| [Name](topic3096.md)| Gets/sets the unique name for the connector. (Inherited from [DriveWorks.GroupConnectorInformation](topic3084.md))  
![Public Property](dotnetimages/publicProperty.gif)| [SourceFolder](topic6833.md)| Get/sets the folder that will be scanned.   
![Public Property](dotnetimages/publicProperty.gif)| [SuccessFolder](topic6834.md)| Gets/sets where files that are have been scanned and successfully used will be moved into.   
![Public Property](dotnetimages/publicProperty.gif)| [TimerInterval](topic6835.md)| Gets/sets the time in seconds for the period of time to wait between scans of the source folder.   
Top

# Protected Properties

| Name| Description  
---|---|---  
![Protected Property](dotnetimages/protectedProperty.gif)| [Data](topic3093.md)| Gets/sets Value used by connector containing configuration information. (Inherited from [DriveWorks.GroupConnectorInformation](topic3084.md))  
Top

# Public Methods

| Name| Description  
---|---|---  
Public Method| CreateObjRef|  (Inherited from System.MarshalByRefObject)  
Public Method| [GetClone](topic3091.md)| Creates a cloned version of this object. (Inherited from [DriveWorks.GroupConnectorInformation](topic3084.md))  
Public Method| GetLifetimeService|  (Inherited from System.MarshalByRefObject)  
Top

# Protected Methods

| Name| Description  
---|---|---  
Protected Method| [EnsureDataStored](topic6830.md)| Overridden.   
Protected Method| MemberwiseClone| Overloaded. (Inherited from System.MarshalByRefObject)  
Protected Method| [OnInitialized](topic6831.md)| Overridden.   
Top

# See Also

#### Reference

[FolderWatcherConfiguration Class](topic6823.md)   
[DriveWorks.Connectors.Folder Namespace](topic6821.md)


