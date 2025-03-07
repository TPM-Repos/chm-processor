Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Item Property   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [ProjectAnnotationCollection Class](topic14419.md) : Item Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_index_
    The index of the annotation to get.

Glossary Item Box

Gets the annotation at the given index. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Default Property Item( _
       ByVal _index_ As Integer _
    ) As [ProjectAnnotation](topic14405.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectAnnotationCollection](topic14419.md)
    Dim index As Integer
    Dim value As [ProjectAnnotation](topic14405.md)
     
    value = instance.Item(index)  
  
C#|   
---|---  
      
    
    public [ProjectAnnotation](topic14405.md) this[ 
       int _index_
    ]; {get;}  
  
#### Parameters

 _index_
    The index of the annotation to get.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectAnnotationCollection Class](topic14419.md)   
[ProjectAnnotationCollection Members](topic14420.md)


