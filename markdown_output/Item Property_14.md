Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Item Property   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [CapturedAnnotationCollection Class](topic14063.md) : Item Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_index_
    The index of the annotation to retrieve.

Glossary Item Box

Gets the annotation at the given index. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property Item( _
       ByVal _index_ As Integer _
    ) As [CapturedAnnotation](topic14054.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [CapturedAnnotationCollection](topic14063.md)
    Dim index As Integer
    Dim value As [CapturedAnnotation](topic14054.md)
     
    value = instance.Item(index)  
  
C#|   
---|---  
      
    
    public [CapturedAnnotation](topic14054.md) Item( 
       int _index_
    ) {get;}  
  
#### Parameters

 _index_
    The index of the annotation to retrieve.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[CapturedAnnotationCollection Class](topic14063.md)   
[CapturedAnnotationCollection Members](topic14064.md)


