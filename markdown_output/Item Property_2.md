Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Item Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [Operations Class](topic11095.md) : Item Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_index_
    The index of the operation to retrieve.

Glossary Item Box

Gets the operation at the specified index. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Default Property Item( _
       ByVal _index_ As Integer _
    ) As [Operation](topic11068.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Operations](topic11095.md)
    Dim index As Integer
    Dim value As [Operation](topic11068.md)
     
    value = instance.Item(index)  
  
C#|   
---|---  
      
    
    public [Operation](topic11068.md) this[ 
       int _index_
    ]; {get;}  
  
#### Parameters

 _index_
    The index of the operation to retrieve.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Operations Class](topic11095.md)   
[Operations Members](topic11096.md)


