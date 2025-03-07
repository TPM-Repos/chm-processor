Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IndexOf Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.EventFlow Namespace](topic6871.md) > [FlowNodeCollection Class](topic7011.md) : IndexOf Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_node_
    The node whose index to retrieve.

Glossary Item Box

Gets the index of the given node. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public MustOverride Function IndexOf( _
       ByVal _node_ As [ExecutableNodeBase](topic6938.md) _
    ) As Integer  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [FlowNodeCollection](topic7011.md)
    Dim node As [ExecutableNodeBase](topic6938.md)
    Dim value As Integer
     
    value = instance.IndexOf(node)  
  
C#|   
---|---  
      
    
    public abstract int IndexOf( 
       [ExecutableNodeBase](topic6938.md) _node_
    )  
  
#### Parameters

 _node_
    The node whose index to retrieve.

#### Return Value

The index of the node, or -1 if the node is not in this collection.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[FlowNodeCollection Class](topic7011.md)   
[FlowNodeCollection Members](topic7012.md)


