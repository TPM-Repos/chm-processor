Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RaiseNodeCreated Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.EventFlow Namespace](topic6871.md) > [FlowNodeCollection Class](topic7011.md) : RaiseNodeCreated Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_node_
    The node that was created.

Glossary Item Box

Raise the [NodeCreated](topic7024.md) event. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Sub RaiseNodeCreated( _
       ByVal _node_ As [ExecutableNodeBase](topic6938.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [FlowNodeCollection](topic7011.md)
    Dim node As [ExecutableNodeBase](topic6938.md)
     
    instance.RaiseNodeCreated(node)  
  
C#|   
---|---  
      
    
    protected void RaiseNodeCreated( 
       [ExecutableNodeBase](topic6938.md) _node_
    )  
  
#### Parameters

 _node_
    The node that was created.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[FlowNodeCollection Class](topic7011.md)   
[FlowNodeCollection Members](topic7012.md)


