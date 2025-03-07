Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
EditNode Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.EventFlow Namespace](topic6871.md) > [INodeEditor Interface](topic6888.md) : EditNode Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_node_
    The node to edit.

Glossary Item Box

Shows the editor for the given node. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function EditNode( _
       ByVal _node_ As [ExecutableNodeBase](topic6938.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [INodeEditor](topic6888.md)
    Dim node As [ExecutableNodeBase](topic6938.md)
    Dim value As Boolean
     
    value = instance.EditNode(node)  
  
C#|   
---|---  
      
    
    bool EditNode( 
       [ExecutableNodeBase](topic6938.md) _node_
    )  
  
#### Parameters

 _node_
    The node to edit.

#### Return Value

True if the node was modified.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[INodeEditor Interface](topic6888.md)   
[INodeEditor Members](topic6889.md)


