![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Item(String) Property   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic14589.md)  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [ProjectFileFormatCollection Class](topic14579.md) > [Item Property](topic14587.md) : Item(String) Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_extension_
    The extension name to find the rules for.

Glossary Item Box

Gets the item with the specified file extension. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads ReadOnly Property Item( _
       ByVal _extension_ As String _
    ) As [ProjectFileFormatRuleCollection](topic14603.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
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

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectFileFormatCollection Class](topic14579.md)   
[ProjectFileFormatCollection Members](topic14580.md)   
[Overload List](topic14587.md)

©2024 DriveWorks Ltd. All Rights Reserved.
