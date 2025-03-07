Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Item Property   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [ReleasedViewCollection Class](topic15057.md) : Item Property  
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
    ) As [ReleasedView](topic15041.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleasedViewCollection](topic15057.md)
    Dim index As Integer
    Dim value As [ReleasedView](topic15041.md)
     
    value = instance.Item(index)  
  
C#|   
---|---  
      
    
    public [ReleasedView](topic15041.md) Item( 
       int _index_
    ) {get;}  
  
#### Parameters

 _index_
    The index of the view to retrieve.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleasedViewCollection Class](topic15057.md)   
[ReleasedViewCollection Members](topic15058.md)


