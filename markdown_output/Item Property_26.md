Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Item Property   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [CapturedViewDimensionCollection Class](topic14384.md) : Item Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_index_
    The index of the dimension to retrieve.

Glossary Item Box

Gets the dimension at the given index. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property Item( _
       ByVal _index_ As Integer _
    ) As [CapturedViewDimension](topic14374.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [CapturedViewDimensionCollection](topic14384.md)
    Dim index As Integer
    Dim value As [CapturedViewDimension](topic14374.md)
     
    value = instance.Item(index)  
  
C#|   
---|---  
      
    
    public [CapturedViewDimension](topic14374.md) Item( 
       int _index_
    ) {get;}  
  
#### Parameters

 _index_
    The index of the dimension to retrieve.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[CapturedViewDimensionCollection Class](topic14384.md)   
[CapturedViewDimensionCollection Members](topic14385.md)


