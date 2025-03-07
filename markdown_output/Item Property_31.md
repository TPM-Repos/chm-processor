Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Item Property   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [ProjectDimensionCollection Class](topic14506.md) : Item Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_index_
    The index of the item to get.

Glossary Item Box

Gets the item at the specified index. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Default Property Item( _
       ByVal _index_ As Integer _
    ) As [ProjectDimension](topic14493.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectDimensionCollection](topic14506.md)
    Dim index As Integer
    Dim value As [ProjectDimension](topic14493.md)
     
    value = instance.Item(index)  
  
C#|   
---|---  
      
    
    public [ProjectDimension](topic14493.md) this[ 
       int _index_
    ]; {get;}  
  
#### Parameters

 _index_
    The index of the item to get.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectDimensionCollection Class](topic14506.md)   
[ProjectDimensionCollection Members](topic14507.md)


