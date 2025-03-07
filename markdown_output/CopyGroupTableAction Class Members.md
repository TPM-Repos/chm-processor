Collapse All Expand All Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
CopyGroupTableAction Class Members   
See Also Properties Methods Events [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic9797.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.GroupMaintenance Namespace](topic9628.md) : CopyGroupTableAction Class  
---  
  
Include Inherited Members    
Include Protected Members  


Glossary Item Box

The following tables list the members exposed by [CopyGroupTableAction](topic9797.md).

# Public Properties

| Name| Description  
---|---|---  
![Public Property](dotnetimages/publicProperty.gif)| [DependentActions](topic9944.md)| All actions that are required to have executed for this action to run. (Inherited from [DriveWorks.GroupMaintenance.ProcessActionBase](topic9935.md))  
![Public Property](dotnetimages/publicProperty.gif)| [HasExecuted](topic9945.md)| Whether or not this action has executed. (Inherited from [DriveWorks.GroupMaintenance.ProcessActionBase](topic9935.md))  
![Public Property](dotnetimages/publicProperty.gif)| [Status](topic9804.md)| The current status of the action.   
![Public Property](dotnetimages/publicProperty.gif)| [StatusMessage](topic9805.md)| Overridden. The current human readable status of this action.   
![Public Property](dotnetimages/publicProperty.gif)| [WillExecute](topic9947.md)| Returns whether or not this action wants to execute. (Inherited from [DriveWorks.GroupMaintenance.ProcessActionBase](topic9935.md))  
Top

# Public Methods

| Name| Description  
---|---|---  
Public Method| [Execute](topic9803.md)| Overridden. Executes this action.   
Public Method| [GetCanExecute](topic9942.md)| Checks to see if the action can be executed or not. (Inherited from [DriveWorks.GroupMaintenance.ProcessActionBase](topic9935.md))  
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

[CopyGroupTableAction Class](topic9797.md)   
[DriveWorks.GroupMaintenance Namespace](topic9628.md)


