Collapse All Expand All Members Options: Show All  Members Options: Filtered   
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

# Public Methods

| Name| Description  
---|---|---  
Public Method| [BeginStart](topic1904.md)| Begins the process of starting the queue on a new thread.   
Public Method| [BeginStop](topic1905.md)| Begins the process of stopping the queue.   
Top

# Protected Methods

| Name| Description  
---|---|---  
Protected Method| [Execute](topic1906.md)| Must be overridden to perform the main work of the queue.   
Protected Method| [Initialize](topic1907.md)| Can be overridden to perform custom initialization when the queue is created.   
Protected Method| [InitializeThread](topic1908.md)| Can be overridden to customize the thread that is used for execution.   
Protected Method| [OnStart](topic1909.md)| Can be overridden to perform one-time initialization when the queue is started.   
Protected Method| [OnStop](topic1910.md)| Can be overridden to perform shutdown when the queue is stopped.   
Protected Method| [WaitForIntervalOrStopRequest](topic1911.md)| Waits until either the polling interval elapses, or a request to stop is made.   
Top

# See Also

#### Reference

[PollingAutopilotQueueBase Class](topic1898.md)   
[DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md)


