![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Item(String) Property   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic14614.md)  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [ProjectFileFormatRuleCollection Class](topic14603.md) > [Item Property](topic14612.md) : Item(String) Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The invariant name of the property to get the rule for.

Glossary Item Box

Get the item with the specified property name. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads ReadOnly Property Item( _
       ByVal _name_ As String _
    ) As [ProjectFileFormatRule](topic14590.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
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

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectFileFormatRuleCollection Class](topic14603.md)   
[ProjectFileFormatRuleCollection Members](topic14604.md)   
[Overload List](topic14612.md)

©2024 DriveWorks Ltd. All Rights Reserved.
