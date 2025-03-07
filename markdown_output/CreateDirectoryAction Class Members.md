Collapse All Expand All Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
CreateDirectoryAction Class Members   
See Also Properties Methods Events [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic9882.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.GroupMaintenance Namespace](topic9628.md) : CreateDirectoryAction Class  
---  
  
Include Inherited Members    
Include Protected Members  


Glossary Item Box

The following tables list the members exposed by [CreateDirectoryAction](topic9882.md).

# Public Properties

| Name| Description  
---|---|---  
![Public Property](dotnetimages/publicProperty.gif)| [DependentActions](topic9944.md)| All actions that are required to have executed for this action to run. (Inherited from [DriveWorks.GroupMaintenance.ProcessActionBase](topic9935.md))  
![Public Property](dotnetimages/publicProperty.gif)| [Directory](topic9890.md)| The directory path that will be made.   
![Public Property](dotnetimages/publicProperty.gif)| [ErrorMessage](topic9891.md)| The error message from attempting to view the target directory.   
![Public Property](dotnetimages/publicProperty.gif)| [HasExecuted](topic9945.md)| Whether or not this action has executed. (Inherited from [DriveWorks.GroupMaintenance.ProcessActionBase](topic9935.md))  
![Public Property](dotnetimages/publicProperty.gif)| [StatusMessage](topic9892.md)| Overridden. The current human readable status of this action.   
![Public Property](dotnetimages/publicProperty.gif)| [WillExecute](topic9947.md)| Returns whether or not this action wants to execute. (Inherited from [DriveWorks.GroupMaintenance.ProcessActionBase](topic9935.md))  
Top

# Public Methods

| Name| Description  
---|---|---  
Public Method| [Execute](topic9888.md)| Overridden. Executes this action.   
Public Method| [GetCanExecute](topic9889.md)| Overridden. Checks to see if the action can be executed or not.   
Top

# Protected Methods

| Name| Description  
---|---|---  
Protected Method| [RaisePropertyChanged](topic9943.md)| Raises the [ProcessActionBase.PropertyChanged](topic9948.md) event. (Inherited from [DriveWorks.GroupMaintenance.ProcessActionBase](topic9935.md))  
Top

# Public Events

| Name| Description  
---|---|---  
![Public Event](dotnetimages/publicEvent.gif)| [PropertyChanged](topic9948.md)| Raised when a property on this object changes. (Inherited from [DriveWorks.GroupMaintenance.ProcessActionBase](topic9935.md))  
Top

# See Also

#### Reference

[CreateDirectoryAction Class](topic9882.md)   
[DriveWorks.GroupMaintenance Namespace](topic9628.md)


