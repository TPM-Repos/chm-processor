Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Item Property   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [CapturedViewCollection Class](topic14362.md) : Item Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_index_
    The index of the view to retrieve.

Glossary Item Box

Gets the view at the given index. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property Item( _
       ByVal _index_ As Integer _
    ) As [CapturedView](topic14351.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [CapturedViewCollection](topic14362.md)
    Dim index As Integer
    Dim value As [CapturedView](topic14351.md)
     
    value = instance.Item(index)  
  
C#|   
---|---  
      
    
    public [CapturedView](topic14351.md) Item( 
       int _index_
    ) {get;}  
  
#### Parameters

 _index_
    The index of the view to retrieve.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[CapturedViewCollection Class](topic14362.md)   
[CapturedViewCollection Members](topic14363.md)


