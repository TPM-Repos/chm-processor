![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
QueueingAutopilotQueueBase<T> Class Methods   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic1925.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) : QueueingAutopilotQueueBase<T> Class  
---  
  
Include Inherited Members    
Include Protected Members    


Glossary Item Box

For a list of all members of this type, see [QueueingAutopilotQueueBase<T> members](topic1926.md).

# ![](dotnetimages/collapse.gif)Public Methods

| Name| Description  
---|---|---  
![Public Method](dotnetimages/publicMethod.gif)| [BeginStart](topic1931.md)| Begins the process of starting the queue on a new thread.   
![Public Method](dotnetimages/publicMethod.gif)| [BeginStop](topic1932.md)| Begins the process of stopping the queue.   
Top

# ![](dotnetimages/collapse.gif)Protected Methods

| Name| Description  
---|---|---  
![Protected Method](dotnetimages/protectedMethod.gif)| [Execute](topic1933.md)| Must be overridden to perform the main work of the queue on the specified item.   
![Protected Method](dotnetimages/protectedMethod.gif)| [Initialize](topic1934.md)| Can be overridden to perform custom initialization when the queue is created.   
![Protected Method](dotnetimages/protectedMethod.gif)| [InitializeThread](topic1935.md)| Can be overridden to customize the thread that is used for execution.   
![Protected Method](dotnetimages/protectedMethod.gif)| [OnStart](topic1936.md)| Can be overridden to perform one-time initialization when the queue is started.   
![Protected Method](dotnetimages/protectedMethod.gif)| [OnStop](topic1937.md)| Can be overridden to perform shutdown when the queue is stopped.   
![Protected Method](dotnetimages/protectedMethod.gif)| [QueueItem](topic1938.md)| Queues the specified work item.   
Top

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[QueueingAutopilotQueueBase<T> Class](topic1925.md)   
[DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md)

©2024 DriveWorks Ltd. All Rights Reserved.
