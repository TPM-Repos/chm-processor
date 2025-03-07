Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Item Property   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [ReleasedSheetCollection Class](topic15017.md) : Item Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_index_
    The index of the sheet to retrieve.

Glossary Item Box

Gets the sheet at the given index. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property Item( _
       ByVal _index_ As Integer _
    ) As [ReleasedSheet](topic15007.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleasedSheetCollection](topic15017.md)
    Dim index As Integer
    Dim value As [ReleasedSheet](topic15007.md)
     
    value = instance.Item(index)  
  
C#|   
---|---  
      
    
    public [ReleasedSheet](topic15007.md) Item( 
       int _index_
    ) {get;}  
  
#### Parameters

 _index_
    The index of the sheet to retrieve.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleasedSheetCollection Class](topic15017.md)   
[ReleasedSheetCollection Members](topic15018.md)


