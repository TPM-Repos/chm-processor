Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Item Property   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [ReleasedViewDimensionCollection Class](topic15078.md) : Item Property  
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
    ) As [ReleasedViewDimension](topic15069.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleasedViewDimensionCollection](topic15078.md)
    Dim index As Integer
    Dim value As [ReleasedViewDimension](topic15069.md)
     
    value = instance.Item(index)  
  
C#|   
---|---  
      
    
    public [ReleasedViewDimension](topic15069.md) Item( 
       int _index_
    ) {get;}  
  
#### Parameters

 _index_
    The index of the dimension to retrieve.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleasedViewDimensionCollection Class](topic15078.md)   
[ReleasedViewDimensionCollection Members](topic15079.md)


