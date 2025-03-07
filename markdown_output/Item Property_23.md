Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Item Property   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [CapturedLayerCollection Class](topic14295.md) : Item Property  
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
    ) As [CapturedLayer](topic14288.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [CapturedLayerCollection](topic14295.md)
    Dim index As Integer
    Dim value As [CapturedLayer](topic14288.md)
     
    value = instance.Item(index)  
  
C#|   
---|---  
      
    
    public [CapturedLayer](topic14288.md) Item( 
       int _index_
    ) {get;}  
  
#### Parameters

 _index_
    The index of the layer to retrieve.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[CapturedLayerCollection Class](topic14295.md)   
[CapturedLayerCollection Members](topic14296.md)


