_T_
    

Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
QueueingAutopilotQueueBase<T> Class   
[Members](topic1926.md)   
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) : QueueingAutopilotQueueBase<T> Class  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Provides a base class to make implementing queueing autopilot queues easier. 

# Object Model

![](dotnetdiagramimages/image67.png)

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public MustInherit Class QueueingAutopilotQueueBase(Of T) 
       Implements [IAutopilotQueue](topic1635.md), [DriveWorks.Extensibility.IExtension](topic7152.md)   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [QueueingAutopilotQueueBase(Of T)](topic1925.md)  
  
C#|   
---|---  
      
    
    public abstract class QueueingAutopilotQueueBase<T> : [IAutopilotQueue](topic1635.md), [DriveWorks.Extensibility.IExtension](topic7152.md)    
  
# Type Parameters

_T_
    

# Inheritance Hierarchy

System.Object  
**DriveWorks.Applications.Autopilot.Extensibility.QueueingAutopilotQueueBase <T>**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[QueueingAutopilotQueueBase<T> Members](topic1926.md)   
[DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md)


