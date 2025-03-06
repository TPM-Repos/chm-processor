![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
CopyFileAction Class Members   
See Also Properties Methods Events [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic9696.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.GroupMaintenance Namespace](topic9628.md) : CopyFileAction Class  
---  
  
Include Inherited Members    
Include Protected Members  


Glossary Item Box

The following tables list the members exposed by [CopyFileAction](topic9696.md).

# ![](dotnetimages/collapse.gif)Public Properties

| Name| Description  
---|---|---  
![Public Property](dotnetimages/publicProperty.gif)| [DependentActions](topic9944.md)| All actions that are required to have executed for this action to run. (Inherited from [DriveWorks.GroupMaintenance.ProcessActionBase](topic9935.md))  
![Public Property](dotnetimages/publicProperty.gif)| [ErrorMessage](topic9704.md)| An error message from attempting to read / copy the file.   
![Public Property](dotnetimages/publicProperty.gif)| [HasExecuted](topic9945.md)| Whether or not this action has executed. (Inherited from [DriveWorks.GroupMaintenance.ProcessActionBase](topic9935.md))  
![Public Property](dotnetimages/publicProperty.gif)| [SourceFile](topic9705.md)| The file to be copied.   
![Public Property](dotnetimages/publicProperty.gif)| [Status](topic9706.md)| The current status of the action.   
![Public Property](dotnetimages/publicProperty.gif)| [StatusMessage](topic9707.md)| Overridden. The current human readable status of this action.   
![Public Property](dotnetimages/publicProperty.gif)| [TargetFile](topic9708.md)| The path to place the file.   
![Public Property](dotnetimages/publicProperty.gif)| [WillExecute](topic9947.md)| Returns whether or not this action wants to execute. (Inherited from [DriveWorks.GroupMaintenance.ProcessActionBase](topic9935.md))  
Top

# ![](dotnetimages/collapse.gif)Public Methods

| Name| Description  
---|---|---  
Public Method| [Execute](topic9702.md)| Overridden. Executes this action.   
Public Method| [GetCanExecute](topic9703.md)| Overridden. Checks to see if the action can be executed or not.   
Top

# ![](dotnetimages/collapse.gif)Protected Methods

| Name| Description  
---|---|---  
Protected Method| [RaisePropertyChanged](topic9943.md)| Raises the [ProcessActionBase.PropertyChanged](topic9948.md) event. (Inherited from [DriveWorks.GroupMaintenance.ProcessActionBase](topic9935.md))  
Top

# ![](dotnetimages/collapse.gif)Public Events

| Name| Description  
---|---|---  
![Public Event](dotnetimages/publicEvent.gif)| [PropertyChanged](topic9948.md)| Raised when a property on this object changes. (Inherited from [DriveWorks.GroupMaintenance.ProcessActionBase](topic9935.md))  
Top

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[CopyFileAction Class](topic9696.md)   
[DriveWorks.GroupMaintenance Namespace](topic9628.md)


