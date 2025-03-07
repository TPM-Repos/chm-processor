Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetQueue(Type) Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [IAutopilotQueueManager Interface](topic1643.md) > [GetQueue Method](topic1649.md) : GetQueue(Type) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_queueType_
    The type of service to search for.

Glossary Item Box

Gets any queues which implement the specified service. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Overloads Function GetQueue( _
       ByVal _queueType_ As Type _
    ) As IEnumerable  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IAutopilotQueueManager](topic1643.md)
    Dim queueType As Type
    Dim value As IEnumerable
     
    value = instance.GetQueue(queueType)  
  
C#|   
---|---  
      
    
    IEnumerable GetQueue( 
       Type _queueType_
    )  
  
#### Parameters

 _queueType_
    The type of service to search for.

#### Return Value

A collection of queues matching the search criteria.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IAutopilotQueueManager Interface](topic1643.md)   
[IAutopilotQueueManager Members](topic1644.md)   
[Overload List](topic1649.md)


