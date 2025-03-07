Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Item Property   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [ProjectLayerCollection Class](topic14650.md) : Item Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_index_
    The index of the layer to get.

Glossary Item Box

Gets the layer at the given index. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Default Property Item( _
       ByVal _index_ As Integer _
    ) As [ProjectLayer](topic14638.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectLayerCollection](topic14650.md)
    Dim index As Integer
    Dim value As [ProjectLayer](topic14638.md)
     
    value = instance.Item(index)  
  
C#|   
---|---  
      
    
    public [ProjectLayer](topic14638.md) this[ 
       int _index_
    ]; {get;}  
  
#### Parameters

 _index_
    The index of the layer to get.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectLayerCollection Class](topic14650.md)   
[ProjectLayerCollection Members](topic14651.md)


