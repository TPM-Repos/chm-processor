![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
ICommandMonitor Interface Members   
See Also Properties Methods Events [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic158.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) : ICommandMonitor Interface  
---  
  
Include Inherited Members    


Glossary Item Box

The following tables list the members exposed by [ICommandMonitor](topic158.md).

# ![](dotnetimages/collapse.gif)Public Properties

| Name| Description  
---|---|---  
![ Property](dotnetimages/Property.gif)| [Application](topic167.md)| Gets the application to which the command belongs.   
![ Property](dotnetimages/Property.gif)| [IsAvailable](topic168.md)| Gets whether the command is available.   
![ Property](dotnetimages/Property.gif)| [IsEnabled](topic169.md)| Gets whether the command is enabled.   
![ Property](dotnetimages/Property.gif)| [IsValid](topic170.md)| Gets whether the command is valid in the current application state.   
![ Property](dotnetimages/Property.gif)| [Manager](topic171.md)| Gets the command manager which is managing the command.   
![ Property](dotnetimages/Property.gif)| [Name](topic172.md)| Gets the culture invariant name of the command.   
![ Property](dotnetimages/Property.gif)| [StateFilter](topic173.md)| Gets the filter which determines in which application states the command is visible.   
Top

# ![](dotnetimages/collapse.gif)Public Methods

| Name| Description  
---|---|---  
![ Method](dotnetimages/Method.gif)| [GetImage](topic163.md)| Gets the context-specific image which represents the command.   
![ Method](dotnetimages/Method.gif)| [GetTitle](topic164.md)| Gets the context-specific title of the command.   
![ Method](dotnetimages/Method.gif)| [Invoke](topic165.md)| Invokes the operation represented by the command.   
![ Method](dotnetimages/Method.gif)| [ValidateContext](topic166.md)| Validates the specified context is suitable for the command.   
Top

# ![](dotnetimages/collapse.gif)Public Events

| Name| Description  
---|---|---  
![ Event](dotnetimages/Event.gif)| [AfterInvoke](topic174.md)| Raised after the command has been invoked.   
![ Event](dotnetimages/Event.gif)| [BeforeInvoke](topic175.md)| Raised when the command is about to be invoked.   
![ Event](dotnetimages/Event.gif)| [Invoking](topic176.md)| Raised when the command is being invoked.   
![ Event](dotnetimages/Event.gif)| [IsAvailableChanged](topic177.md)| Raised when the [IsAvailable](topic168.md) property changes.   
![ Event](dotnetimages/Event.gif)| [IsEnabledChanged](topic178.md)| Raised when the [IsEnabled](topic169.md) property changes.   
![ Event](dotnetimages/Event.gif)| [IsValidChanged](topic179.md)| Raised when the [IsValid](topic170.md) property changes.   
Top

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ICommandMonitor Interface](topic158.md)   
[DriveWorks.Applications Namespace](topic16.md)

©2024 DriveWorks Ltd. All Rights Reserved.
