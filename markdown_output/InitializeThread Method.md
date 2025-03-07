Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
InitializeThread Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [PollingAutopilotQueueBase Class](topic1898.md) : InitializeThread Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_thread_
    The thread to be customized.

Glossary Item Box

Can be overridden to customize the thread that is used for execution. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overridable Sub InitializeThread( _
       ByVal _thread_ As Thread _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [PollingAutopilotQueueBase](topic1898.md)
    Dim thread As Thread
     
    instance.InitializeThread(thread)  
  
C#|   
---|---  
      
    
    protected virtual void InitializeThread( 
       Thread _thread_
    )  
  
#### Parameters

 _thread_
    The thread to be customized.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[PollingAutopilotQueueBase Class](topic1898.md)   
[PollingAutopilotQueueBase Members](topic1899.md)


