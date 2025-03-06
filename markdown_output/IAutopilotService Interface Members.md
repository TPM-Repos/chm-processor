![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
IAutopilotService Interface Members   
See Also Properties Methods Events [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic1654.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) : IAutopilotService Interface  
---  
  
Include Inherited Members    


Glossary Item Box

The following tables list the members exposed by [IAutopilotService](topic1654.md).

# ![](dotnetimages/collapse.gif)Public Properties

| Name| Description  
---|---|---  
![ Property](dotnetimages/Property.gif)| [IsRunning](topic1673.md)| Determines whether the service is running.   
![ Property](dotnetimages/Property.gif)| [IsStarting](topic1674.md)| Determines whether the service is in the process of being started.   
![ Property](dotnetimages/Property.gif)| [IsStopping](topic1675.md)| Determines whether the service is in the process of being stopped.   
![ Property](dotnetimages/Property.gif)| [VerboseLoggingEnabled](topic1676.md)| Whether verbose logging is enabled.   
Top

# ![](dotnetimages/collapse.gif)Public Methods

| Name| Description  
---|---|---  
![ Method](dotnetimages/Method.gif)| [BeginStart](topic1659.md)| Begins starting the autopilot capability.   
![ Method](dotnetimages/Method.gif)| [BeginStop](topic1660.md)| Begins stopping the autopilot capability.   
![ Method](dotnetimages/Method.gif)| [OnBlockedTagsAdded](topic1661.md)| Raises the [BlockedTagsAdded](topic1677.md) event with the provided collection of added tags.   
![ Method](dotnetimages/Method.gif)| [OnBlockedTagsRemoved](topic1662.md)| Raises the [BlockedTagsRemoved](topic1678.md) event with the provided collection of removed tags.   
![ Method](dotnetimages/Method.gif)| [OnCheckedFileExists](topic1663.md)| Raises the [CheckedFileExists](topic1679.md) event with the provided file path.   
![ Method](dotnetimages/Method.gif)| [OnCheckingDirectory](topic1664.md)| Raises the [CheckingDirectory](topic1680.md) event.   
![ Method](dotnetimages/Method.gif)| [OnCheckingFileExists](topic1665.md)| Raises the [CheckingFileExists](topic1681.md) event with the provided file path.   
![ Method](dotnetimages/Method.gif)| [OnMovingFile](topic1666.md)| Raises the [MovingFile](topic1683.md) event.   
![ Method](dotnetimages/Method.gif)| [OnPriorityOnlyProcessingChanged](topic1667.md)| Raises the [PriorityOnlyProcessingChanged](topic1684.md) event with the provided value.   
![ Method](dotnetimages/Method.gif)| [OnPriorityTagsAdded](topic1668.md)| Raises the [PriorityTagsAdded](topic1685.md) event with the provided collection of added tags.   
![ Method](dotnetimages/Method.gif)| [OnPriorityTagsRemoved](topic1669.md)| Raises the [PriorityTagsRemoved](topic1686.md) event with the provided collection of removed tags.   
![ Method](dotnetimages/Method.gif)| [TestConnection](topic1670.md)| Overloaded. Tests the connection to the group currently in use by the [IAutopilotService](topic1654.md).   
Top

# ![](dotnetimages/collapse.gif)Public Events

| Name| Description  
---|---|---  
![ Event](dotnetimages/Event.gif)| [BlockedTagsAdded](topic1677.md)| Raised when new blocked tags have been added to the blocked tags collection.   
![ Event](dotnetimages/Event.gif)| [BlockedTagsRemoved](topic1678.md)| Raised when blocked tags have been removed from the blocked tags collection.   
![ Event](dotnetimages/Event.gif)| [CheckedFileExists](topic1679.md)| Raised when an Autopilot component such as a queue or connector has finished checking the existence of a file.   
![ Event](dotnetimages/Event.gif)| [CheckingDirectory](topic1680.md)| Raised when an Autopilot component such as a queue or connector is about to check the contents of a directory.   
![ Event](dotnetimages/Event.gif)| [CheckingFileExists](topic1681.md)| Raised when an Autopilot component such as a queue or connector is about to check the existence of a file.   
![ Event](dotnetimages/Event.gif)| [ConnectionSuccessful](topic1682.md)| Raised when a connection to the group currently in use by the [IAutopilotService](topic1654.md) was successful.   
![ Event](dotnetimages/Event.gif)| [MovingFile](topic1683.md)| Raised when an Autopilot component such as a queue or connector is about to move a file.   
![ Event](dotnetimages/Event.gif)| [PriorityOnlyProcessingChanged](topic1684.md)| Raised when the 'Process Priority Tags Only' setting has changed.   
![ Event](dotnetimages/Event.gif)| [PriorityTagsAdded](topic1685.md)| Raised when new priority tags have been added to the priority tags collection.   
![ Event](dotnetimages/Event.gif)| [PriorityTagsRemoved](topic1686.md)| Raised when priority tags have been removed from the priority tags collection.   
![ Event](dotnetimages/Event.gif)| [Started](topic1687.md)| Raised when the service is started.   
![ Event](dotnetimages/Event.gif)| [Starting](topic1688.md)| Raised when the service is starting.   
![ Event](dotnetimages/Event.gif)| [Stopped](topic1689.md)| Raised when the service is stopped.   
![ Event](dotnetimages/Event.gif)| [Stopping](topic1690.md)| Raised when the service is stopping.   
Top

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IAutopilotService Interface](topic1654.md)   
[DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md)


