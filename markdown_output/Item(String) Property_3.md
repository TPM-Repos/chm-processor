Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Item(String) Property   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [ProjectFileFormatRuleCollection Class](topic14603.md) > [Item Property](topic14612.md) : Item(String) Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The invariant name of the property to get the rule for.

Glossary Item Box

Get the item with the specified property name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads ReadOnly Property Item( _
       ByVal _name_ As String _
    ) As [ProjectFileFormatRule](topic14590.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectFileFormatRuleCollection](topic14603.md)
    Dim name As String
    Dim value As [ProjectFileFormatRule](topic14590.md)
     
    value = instance.Item(name)  
  
C#|   
---|---  
      
    
    public [ProjectFileFormatRule](topic14590.md) Item( 
       string _name_
    ) {get;}  
  
#### Parameters

 _name_
    The invariant name of the property to get the rule for.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectFileFormatRuleCollection Class](topic14603.md)   
[ProjectFileFormatRuleCollection Members](topic14604.md)   
[Overload List](topic14612.md)


