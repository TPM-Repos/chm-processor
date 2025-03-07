Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Item(Int32) Property   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [ProjectFileFormatRuleCollection Class](topic14603.md) > [Item Property](topic14612.md) : Item(Int32) Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_index_
    The index of the item to retrieve.

Glossary Item Box

Gets the item at the specified index. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads ReadOnly Property Item( _
       ByVal _index_ As Integer _
    ) As [ProjectFileFormatRule](topic14590.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectFileFormatRuleCollection](topic14603.md)
    Dim index As Integer
    Dim value As [ProjectFileFormatRule](topic14590.md)
     
    value = instance.Item(index)  
  
C#|   
---|---  
      
    
    public [ProjectFileFormatRule](topic14590.md) Item( 
       int _index_
    ) {get;}  
  
#### Parameters

 _index_
    The index of the item to retrieve.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectFileFormatRuleCollection Class](topic14603.md)   
[ProjectFileFormatRuleCollection Members](topic14604.md)   
[Overload List](topic14612.md)


