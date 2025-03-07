Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Item Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.EventFlow Namespace](topic6871.md) > [FlowNodeCollection Class](topic7011.md) : Item Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_index_
    The zero-based index of the node to retrieve.

Glossary Item Box

Gets the node at the specified index. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public MustOverride ReadOnly Default Property Item( _
       ByVal _index_ As Integer _
    ) As [ExecutableNodeBase](topic6938.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [FlowNodeCollection](topic7011.md)
    Dim index As Integer
    Dim value As [ExecutableNodeBase](topic6938.md)
     
    value = instance.Item(index)  
  
C#|   
---|---  
      
    
    public abstract [ExecutableNodeBase](topic6938.md) this[ 
       int _index_
    ]; {get;}  
  
#### Parameters

 _index_
    The zero-based index of the node to retrieve.

# Exceptions

Exception| Description  
---|---  
System.IndexOutOfRangeException| Thrown if the specified index is out of range.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[FlowNodeCollection Class](topic7011.md)   
[FlowNodeCollection Members](topic7012.md)


