Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Item(String) Property   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [ProjectFileFormatCollection Class](topic14579.md) > [Item Property](topic14587.md) : Item(String) Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_extension_
    The extension name to find the rules for.

Glossary Item Box

Gets the item with the specified file extension. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads ReadOnly Property Item( _
       ByVal _extension_ As String _
    ) As [ProjectFileFormatRuleCollection](topic14603.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectFileFormatCollection](topic14579.md)
    Dim extension As String
    Dim value As [ProjectFileFormatRuleCollection](topic14603.md)
     
    value = instance.Item(extension)  
  
C#|   
---|---  
      
    
    public [ProjectFileFormatRuleCollection](topic14603.md) Item( 
       string _extension_
    ) {get;}  
  
#### Parameters

 _extension_
    The extension name to find the rules for.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectFileFormatCollection Class](topic14579.md)   
[ProjectFileFormatCollection Members](topic14580.md)   
[Overload List](topic14587.md)


