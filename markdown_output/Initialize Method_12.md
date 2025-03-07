Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Initialize Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [IAutopilotQueue Interface](topic1635.md) : Initialize Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_queueManager_
    The queue manager.

Glossary Item Box

Initializes the queue. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub Initialize( _
       ByVal _queueManager_ As [IAutopilotQueueManager](topic1643.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IAutopilotQueue](topic1635.md)
    Dim queueManager As [IAutopilotQueueManager](topic1643.md)
     
    instance.Initialize(queueManager)  
  
C#|   
---|---  
      
    
    void Initialize( 
       [IAutopilotQueueManager](topic1643.md) _queueManager_
    )  
  
#### Parameters

 _queueManager_
    The queue manager.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IAutopilotQueue Interface](topic1635.md)   
[IAutopilotQueue Members](topic1636.md)


