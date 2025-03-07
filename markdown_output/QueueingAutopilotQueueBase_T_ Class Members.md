Collapse All Expand All Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
QueueingAutopilotQueueBase<T> Class Members   
See Also Properties Methods [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic1925.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) : QueueingAutopilotQueueBase<T> Class  
---  
  
Include Inherited Members    
Include Protected Members  


Glossary Item Box

The following tables list the members exposed by [QueueingAutopilotQueueBase<T>](topic1925.md).

# Public Properties

| Name| Description  
---|---|---  
![Public Property](dotnetimages/publicProperty.gif)| [IsStopping](topic1939.md)| Determines whether the queue is in the process of starting.   
![Public Property](dotnetimages/publicProperty.gif)| [SyncRoot](topic1941.md)| Gets an object which can be use to synchronize access to the queue.   
Top

# Protected Properties

| Name| Description  
---|---|---  
![Protected Property](dotnetimages/protectedProperty.gif)| [QueueCount](topic1940.md)| Gets the number of work items in the queue.   
Top

# Public Methods

| Name| Description  
---|---|---  
Public Method| [BeginStart](topic1931.md)| Begins the process of starting the queue on a new thread.   
Public Method| [BeginStop](topic1932.md)| Begins the process of stopping the queue.   
Top

# Protected Methods

| Name| Description  
---|---|---  
Protected Method| [Execute](topic1933.md)| Must be overridden to perform the main work of the queue on the specified item.   
Protected Method| [Initialize](topic1934.md)| Can be overridden to perform custom initialization when the queue is created.   
Protected Method| [InitializeThread](topic1935.md)| Can be overridden to customize the thread that is used for execution.   
Protected Method| [OnStart](topic1936.md)| Can be overridden to perform one-time initialization when the queue is started.   
Protected Method| [OnStop](topic1937.md)| Can be overridden to perform shutdown when the queue is stopped.   
Protected Method| [QueueItem](topic1938.md)| Queues the specified work item.   
Top

# See Also

#### Reference

[QueueingAutopilotQueueBase<T> Class](topic1925.md)   
[DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md)


