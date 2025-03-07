Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Item Property   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [ReleasedDimensionCollection Class](topic14838.md) : Item Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_index_
    The index of the item to retrieve.

Glossary Item Box

Gets the item at the specified index. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Default Property Item( _
       ByVal _index_ As Integer _
    ) As [ReleasedDimension](topic14826.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleasedDimensionCollection](topic14838.md)
    Dim index As Integer
    Dim value As [ReleasedDimension](topic14826.md)
     
    value = instance.Item(index)  
  
C#|   
---|---  
      
    
    public [ReleasedDimension](topic14826.md) this[ 
       int _index_
    ]; {get;}  
  
#### Parameters

 _index_
    The index of the item to retrieve.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleasedDimensionCollection Class](topic14838.md)   
[ReleasedDimensionCollection Members](topic14839.md)


