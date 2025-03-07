Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
BeginStart Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [PollingAutopilotQueueBase Class](topic1898.md) : BeginStart Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Begins the process of starting the queue on a new thread. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function BeginStart() As WaitHandle  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [PollingAutopilotQueueBase](topic1898.md)
    Dim value As WaitHandle
     
    value = instance.BeginStart()  
  
C#|   
---|---  
      
    
    public WaitHandle BeginStart()  
  
#### Return Value

A wait handle which can be used to determine when the queue has started.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[PollingAutopilotQueueBase Class](topic1898.md)   
[PollingAutopilotQueueBase Members](topic1899.md)


