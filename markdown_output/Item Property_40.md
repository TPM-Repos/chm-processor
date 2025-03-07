Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Item Property   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [ProjectViewDimensionCollection Class](topic14737.md) : Item Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_index_
    The index of the dimension to get.

Glossary Item Box

Gets the dimension at the given index. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Default Property Item( _
       ByVal _index_ As Integer _
    ) As [ProjectViewDimension](topic14728.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectViewDimensionCollection](topic14737.md)
    Dim index As Integer
    Dim value As [ProjectViewDimension](topic14728.md)
     
    value = instance.Item(index)  
  
C#|   
---|---  
      
    
    public [ProjectViewDimension](topic14728.md) this[ 
       int _index_
    ]; {get;}  
  
#### Parameters

 _index_
    The index of the dimension to get.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectViewDimensionCollection Class](topic14737.md)   
[ProjectViewDimensionCollection Members](topic14738.md)


