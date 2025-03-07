Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Item Property   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [CapturedSheetCollection Class](topic14331.md) : Item Property  
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
    ) As [CapturedSheet](topic14323.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [CapturedSheetCollection](topic14331.md)
    Dim index As Integer
    Dim value As [CapturedSheet](topic14323.md)
     
    value = instance.Item(index)  
  
C#|   
---|---  
      
    
    public [CapturedSheet](topic14323.md) Item( 
       int _index_
    ) {get;}  
  
#### Parameters

 _index_
    The index of the sheet to retrieve.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[CapturedSheetCollection Class](topic14331.md)   
[CapturedSheetCollection Members](topic14332.md)


