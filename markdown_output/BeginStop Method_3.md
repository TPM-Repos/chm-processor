Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
BeginStop Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [QueueingAutopilotQueueBase<T> Class](topic1925.md) : BeginStop Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Begins the process of stopping the queue. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function BeginStop() As WaitHandle  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [QueueingAutopilotQueueBase(Of T)](topic1925.md)
    Dim value As WaitHandle
     
    value = instance.BeginStop()  
  
C#|   
---|---  
      
    
    public WaitHandle BeginStop()  
  
#### Return Value

A wait handle which can be used to determine when the queue has stopped.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[QueueingAutopilotQueueBase<T> Class](topic1925.md)   
[QueueingAutopilotQueueBase<T> Members](topic1926.md)


