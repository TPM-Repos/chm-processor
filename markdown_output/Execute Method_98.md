Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Execute Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [QueueingAutopilotQueueBase<T> Class](topic1925.md) : Execute Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_item_
    

Glossary Item Box

Must be overridden to perform the main work of the queue on the specified item. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected MustOverride Sub Execute( _
       ByVal _item_ As T _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [QueueingAutopilotQueueBase(Of T)](topic1925.md)
    Dim item As T
     
    instance.Execute(item)  
  
C#|   
---|---  
      
    
    protected abstract void Execute( 
       T _item_
    )  
  
#### Parameters

 _item_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[QueueingAutopilotQueueBase<T> Class](topic1925.md)   
[QueueingAutopilotQueueBase<T> Members](topic1926.md)


