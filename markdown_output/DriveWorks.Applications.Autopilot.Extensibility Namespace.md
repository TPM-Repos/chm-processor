![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All  
---  
DriveWorks SDK Documentation  |   
---|---  
DriveWorks.Applications.Autopilot.Extensibility Namespace   
See Also [Inheritance Hierarchy](topic1634.md) [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic1633.md)  
[DriveWorks.Applications Assembly](topic13.md) : DriveWorks.Applications.Autopilot.Extensibility Namespace  
---  
  
Glossary Item Box

# ![](dotnetimages/collapse.gif)Classes

| Class| Description  
---|---|---  
![Class](dotnetimages/Class.gif)| [AutopilotViewNames](topic1810.md) | Provides access to the names of common views in DriveWorks Autopilot.  
![Class](dotnetimages/Class.gif)| [CheckingDirectoryEventArgs](topic1826.md) | Provides event arguments for checking directory events.  
![Class](dotnetimages/Class.gif)| [ConnectorBase](topic1834.md) | Provides a base class to make implementing connectors easier.  
![Class](dotnetimages/Class.gif)| [FileExistenceCheckEventArgs](topic1849.md) | Provides event arguments for file existence check events.  
![Class](dotnetimages/Class.gif)| [GroupConnectorBase<T>](topic1857.md) | Provides a base class to make implementing group connectors easier.  
![Class](dotnetimages/Class.gif)| [GroupPollingConnectorBase<T>](topic1878.md) | Provides a base class for group connectors which use a polling strategy.  
![Class](dotnetimages/Class.gif)| [MovingFileEventArgs](topic1888.md) | Provides event arguments for moving file events.  
![Class](dotnetimages/Class.gif)| [PollingAutopilotQueueBase](topic1898.md) | Provides a base class to make implementing polling autopilot queues easier.  
![Class](dotnetimages/Class.gif)| [PollingConnectorBase](topic1914.md) | Provides a base class for connectors which use a polling strategy.  
![Class](dotnetimages/Class.gif)| [QueueingAutopilotQueueBase<T>](topic1925.md) | Provides a base class to make implementing queueing autopilot queues easier.  
![Class](dotnetimages/Class.gif)| [RunDriveAppTask](topic1942.md) | Used by the AutoPilot schedule connector to run a driveapp and set a constant defined in the arguments property.  
![Class](dotnetimages/Class.gif)| [RunProjectTask](topic1951.md) | Used by the AutoPilot schedule connector to run a project and invoke a transition defined in the arguments property.  
![Class](dotnetimages/Class.gif)| [SpecificationRequestInputsDrivenEventArgs](topic1960.md) | Provides information about the results of driving a specification request's inputs.  
![Class](dotnetimages/Class.gif)| [TransitionFailedEventArgs](topic1968.md) | Provides event data for the [ISpecificationRequest.TransitionFailed](topic1790.md) event.  
  
# ![](dotnetimages/collapse.gif)Interfaces

| Interface| Description  
---|---|---  
![Interface](dotnetimages/Interface.gif)| [IAutopilotQueue](topic1635.md) | Provides support for custom autopilot queues.  
![Interface](dotnetimages/Interface.gif)| [IAutopilotQueueManager](topic1643.md) | Represents the queue manager hosting one or more queues.  
![Interface](dotnetimages/Interface.gif)| [IAutopilotService](topic1654.md) | Provides support for controlling DriveWorks Autopilot.  
![Interface](dotnetimages/Interface.gif)| [IChildSpecificationRequest](topic1691.md) | Encapsulates all the data required to automate the specification of a sub-project.  
![Interface](dotnetimages/Interface.gif)| [IConnector](topic1697.md) | Provides a contract for plug-ins which can connect to external systems and receive specifications from them.  
![Interface](dotnetimages/Interface.gif)| [IGroupConnector](topic1706.md) | Provides a contract for a group connector.  
![Interface](dotnetimages/Interface.gif)| [IGroupConnectorEditor](topic1716.md) | Provides a contract between the DriveWorks Administrator Connector management view, and a connector designer's view UI.  
![Interface](dotnetimages/Interface.gif)| [IGroupConnectorRegistration](topic1724.md) | Provides a contract for objects which provides information about group connectors.  
![Interface](dotnetimages/Interface.gif)| [IScheduleConnectorTask](topic1734.md) | Provides a contract for a schedule connector task.  
![Interface](dotnetimages/Interface.gif)| [ISolidWorksHealthMonitor](topic1741.md) | Provides access to the SolidWorks "Nurse", the component of DriveWorks which is responsible for monitoring the health of SolidWorks processes used for model and preview generation.  
![Interface](dotnetimages/Interface.gif)| [ISolidWorksOperation](topic1748.md) | Represents a single model generation operation being coordinated by the [ISolidWorksHealthMonitor](topic1741.md).  
![Interface](dotnetimages/Interface.gif)| [ISolidWorksOperationBatch](topic1755.md) | Represents a model generation batch being coordinated by the [ISolidWorksHealthMonitor](topic1741.md).  
![Interface](dotnetimages/Interface.gif)| [ISpecificationAutomation](topic1761.md) | Provides a means by which to automate one or more Specifications within DriveWorks Server.  
![Interface](dotnetimages/Interface.gif)| [ISpecificationRequest](topic1778.md) | Encapsulates all the data required to automate the specification of a project.  
![Interface](dotnetimages/Interface.gif)| [ITranslationRequest](topic1791.md) | Represents a translation request.  
![Interface](dotnetimages/Interface.gif)| [ITranslator](topic1801.md) | Provides a contract for plug-ins which can take raw data and translate it into an series of [ISpecificationRequest](topic1778.md) instances.  
  
# ![](dotnetimages/collapse.gif)Delegates

| Delegate| Description  
---|---|---  
![Delegate](dotnetimages/Delegate.gif)| [IAutopilotService.BlockedTagsAddedEventHandler](topic1977.md) | Represents a method that will handle the [IAutopilotService.BlockedTagsAdded](topic1677.md) event.  
![Delegate](dotnetimages/Delegate.gif)| [IAutopilotService.BlockedTagsRemovedEventHandler](topic1978.md) | Represents a method that will handle the [IAutopilotService.BlockedTagsRemoved](topic1678.md) event.  
![Delegate](dotnetimages/Delegate.gif)| [IAutopilotService.PriorityOnlyProcessingChangedEventHandler](topic1979.md) | Represents a method that will handle the [IAutopilotService.PriorityOnlyProcessingChanged](topic1684.md) event.  
![Delegate](dotnetimages/Delegate.gif)| [IAutopilotService.PriorityTagsAddedEventHandler](topic1980.md) | Represents a method that will handle the [IAutopilotService.PriorityTagsAdded](topic1685.md) event.  
![Delegate](dotnetimages/Delegate.gif)| [IAutopilotService.PriorityTagsRemovedEventHandler](topic1981.md) | Represents a method that will handle the [IAutopilotService.PriorityTagsRemoved](topic1686.md) event.  
  
# ![](dotnetimages/collapse.gif)Enumerations

| Enumeration| Description  
---|---|---  
![Enumeration](dotnetimages/Enumeration.gif)| [SolidWorksBatchHint](topic1807.md) | Provides hints to the health monitor about a batch.  
![Enumeration](dotnetimages/Enumeration.gif)| [SolidWorksOperationPriority](topic1808.md) | Represents the relative priority of an operation being coordinated by the [ISolidWorksHealthMonitor](topic1741.md).  
![Enumeration](dotnetimages/Enumeration.gif)| [SolidWorksOperationType](topic1809.md) | Indicates the type of an operation being coordinated by the [ISolidWorksHealthMonitor](topic1741.md).  
  
# ![](dotnetimages/collapse.gif)See Also

#### Reference

[DriveWorks.Applications Assembly](topic13.md)

©2024 DriveWorks Ltd. All Rights Reserved.
