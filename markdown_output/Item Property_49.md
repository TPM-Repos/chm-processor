Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Item Property   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [ReleasedLayerCollection Class](topic14976.md) : Item Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_index_
    The index of the layer to retrieve.

Glossary Item Box

Gets the layer at the given index. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property Item( _
       ByVal _index_ As Integer _
    ) As [ReleasedLayer](topic14968.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleasedLayerCollection](topic14976.md)
    Dim index As Integer
    Dim value As [ReleasedLayer](topic14968.md)
     
    value = instance.Item(index)  
  
C#|   
---|---  
      
    
    public [ReleasedLayer](topic14968.md) Item( 
       int _index_
    ) {get;}  
  
#### Parameters

 _index_
    The index of the layer to retrieve.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleasedLayerCollection Class](topic14976.md)   
[ReleasedLayerCollection Members](topic14977.md)


