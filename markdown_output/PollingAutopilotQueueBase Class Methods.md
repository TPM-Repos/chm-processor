![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
PollingAutopilotQueueBase Class Methods   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) : PollingAutopilotQueueBase Class  
---  
  
Include Inherited Members    
Include Protected Members    


Glossary Item Box

For a list of all members of this type, see [PollingAutopilotQueueBase members](topic1899.md).

# ![](dotnetimages/collapse.gif)Public Methods

| Name| Description  
---|---|---  
![Public Method](dotnetimages/publicMethod.gif)| [BeginStart](topic1904.md)| Begins the process of starting the queue on a new thread.   
![Public Method](dotnetimages/publicMethod.gif)| [BeginStop](topic1905.md)| Begins the process of stopping the queue.   
Top

# ![](dotnetimages/collapse.gif)Protected Methods

| Name| Description  
---|---|---  
![Protected Method](dotnetimages/protectedMethod.gif)| [Execute](topic1906.md)| Must be overridden to perform the main work of the queue.   
![Protected Method](dotnetimages/protectedMethod.gif)| [Initialize](topic1907.md)| Can be overridden to perform custom initialization when the queue is created.   
![Protected Method](dotnetimages/protectedMethod.gif)| [InitializeThread](topic1908.md)| Can be overridden to customize the thread that is used for execution.   
![Protected Method](dotnetimages/protectedMethod.gif)| [OnStart](topic1909.md)| Can be overridden to perform one-time initialization when the queue is started.   
![Protected Method](dotnetimages/protectedMethod.gif)| [OnStop](topic1910.md)| Can be overridden to perform shutdown when the queue is stopped.   
![Protected Method](dotnetimages/protectedMethod.gif)| [WaitForIntervalOrStopRequest](topic1911.md)| Waits until either the polling interval elapses, or a request to stop is made.   
Top

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[PollingAutopilotQueueBase Class](topic1898.md)   
[DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md)


