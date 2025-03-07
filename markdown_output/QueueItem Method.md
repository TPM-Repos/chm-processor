Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
QueueItem Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [QueueingAutopilotQueueBase<T> Class](topic1925.md) : QueueItem Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_item_
    The work item to process.

Glossary Item Box

Queues the specified work item. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Sub QueueItem( _
       ByVal _item_ As T _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [QueueingAutopilotQueueBase(Of T)](topic1925.md)
    Dim item As T
     
    instance.QueueItem(item)  
  
C#|   
---|---  
      
    
    protected void QueueItem( 
       T _item_
    )  
  
#### Parameters

 _item_
    The work item to process.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[QueueingAutopilotQueueBase<T> Class](topic1925.md)   
[QueueingAutopilotQueueBase<T> Members](topic1926.md)


