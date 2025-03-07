Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Item Property   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [ProjectSheetCollection Class](topic14683.md) : Item Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_index_
    The index of the sheet to get.

Glossary Item Box

Gets the sheet at the given index. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Default Property Item( _
       ByVal _index_ As Integer _
    ) As [ProjectSheet](topic14673.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectSheetCollection](topic14683.md)
    Dim index As Integer
    Dim value As [ProjectSheet](topic14673.md)
     
    value = instance.Item(index)  
  
C#|   
---|---  
      
    
    public [ProjectSheet](topic14673.md) this[ 
       int _index_
    ]; {get;}  
  
#### Parameters

 _index_
    The index of the sheet to get.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectSheetCollection Class](topic14683.md)   
[ProjectSheetCollection Members](topic14684.md)


