Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Initialize Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [PollingAutopilotQueueBase Class](topic1898.md) : Initialize Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_queueManager_
    The queue manager.

Glossary Item Box

Can be overridden to perform custom initialization when the queue is created. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overridable Sub Initialize( _
       ByVal _queueManager_ As [IAutopilotQueueManager](topic1643.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [PollingAutopilotQueueBase](topic1898.md)
    Dim queueManager As [IAutopilotQueueManager](topic1643.md)
     
    instance.Initialize(queueManager)  
  
C#|   
---|---  
      
    
    protected virtual void Initialize( 
       [IAutopilotQueueManager](topic1643.md) _queueManager_
    )  
  
#### Parameters

 _queueManager_
    The queue manager.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[PollingAutopilotQueueBase Class](topic1898.md)   
[PollingAutopilotQueueBase Members](topic1899.md)


