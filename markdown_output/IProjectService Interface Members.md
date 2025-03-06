![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
IProjectService Interface Members   
See Also Properties Methods Events [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic382.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) : IProjectService Interface  
---  
  
Include Inherited Members    


Glossary Item Box

The following tables list the members exposed by [IProjectService](topic382.md).

# ![](dotnetimages/collapse.gif)Public Properties

| Name| Description  
---|---|---  
![ Property](dotnetimages/Property.gif)| [ActiveProject](topic392.md)| Gets the active project.   
![ Property](dotnetimages/Property.gif)| [HasChanges](topic393.md)| Gets/set if the current project has any changes that have not been saved.   
![ Property](dotnetimages/Property.gif)| [SupportsCloseProject](topic394.md)| Gets a boolean indicating whether the implementation supports projects being closed by 3rd party code.   
![ Property](dotnetimages/Property.gif)| [SupportsCreateProject](topic395.md)| Gets a boolean indicating whether the implementation supports projects being created by 3rd party code.   
![ Property](dotnetimages/Property.gif)| [SupportsOpenProject](topic396.md)| Gets a boolean indicating whether the implementation supports projects being opened by 3rd party code.   
Top

# ![](dotnetimages/collapse.gif)Public Methods

| Name| Description  
---|---|---  
![ Method](dotnetimages/Method.gif)| [CloseProject](topic387.md)| Closes the active project without saving it.   
![ Method](dotnetimages/Method.gif)| [CreateProject](topic388.md)| Creates a new project.   
![ Method](dotnetimages/Method.gif)| [OpenProject](topic389.md)| Opens the specified project.   
![ Method](dotnetimages/Method.gif)| [RaiseProjectRenameFinished](topic390.md)| Raises the [ProjectRenameFinished](topic401.md) event with the given parameters.   
![ Method](dotnetimages/Method.gif)| [RaiseProjectRenameStarted](topic391.md)| Raises the [ProjectRenameStarted](topic402.md) event with the given parameters.   
Top

# ![](dotnetimages/collapse.gif)Public Events

| Name| Description  
---|---|---  
![ Event](dotnetimages/Event.gif)| [ProjectClosed](topic397.md)| Raised when the active project is closed.   
![ Event](dotnetimages/Event.gif)| [ProjectClosing](topic398.md)| Raised when the active project is about to be closed.   
![ Event](dotnetimages/Event.gif)| [ProjectOpened](topic399.md)| Raised when a project has been opened.   
![ Event](dotnetimages/Event.gif)| [ProjectOpening](topic400.md)| Raised when a project is about to be opened.   
![ Event](dotnetimages/Event.gif)| [ProjectRenameFinished](topic401.md)| Raised when a project has finished the renaming process.   
![ Event](dotnetimages/Event.gif)| [ProjectRenameStarted](topic402.md)| Raised when a project has started the renaming process.   
Top

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IProjectService Interface](topic382.md)   
[DriveWorks.Applications Namespace](topic16.md)

©2024 DriveWorks Ltd. All Rights Reserved.
