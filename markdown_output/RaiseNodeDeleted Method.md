Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RaiseNodeDeleted Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.EventFlow Namespace](topic6871.md) > [FlowNodeCollection Class](topic7011.md) : RaiseNodeDeleted Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_node_
    The node that was deleted.

Glossary Item Box

Raise the [NodeDeleted](topic7025.md) event. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Sub RaiseNodeDeleted( _
       ByVal _node_ As [ExecutableNodeBase](topic6938.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [FlowNodeCollection](topic7011.md)
    Dim node As [ExecutableNodeBase](topic6938.md)
     
    instance.RaiseNodeDeleted(node)  
  
C#|   
---|---  
      
    
    protected void RaiseNodeDeleted( 
       [ExecutableNodeBase](topic6938.md) _node_
    )  
  
#### Parameters

 _node_
    The node that was deleted.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[FlowNodeCollection Class](topic7011.md)   
[FlowNodeCollection Members](topic7012.md)


