![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
OnParentDefaultFontChanged Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic8618.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [OptionGroup Class](topic8608.md) : OnParentDefaultFontChanged Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_newFont_
    

Glossary Item Box

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overrides Sub OnParentDefaultFontChanged( _
       ByVal _newFont_ As [SimpleFont](topic8882.md) _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [OptionGroup](topic8608.md)
    Dim newFont As [SimpleFont](topic8882.md)
     
    instance.OnParentDefaultFontChanged(newFont)  
  
C#|   
---|---  
      
    
    protected override void OnParentDefaultFontChanged( 
       [SimpleFont](topic8882.md) _newFont_
    )  
  
#### Parameters

 _newFont_
    

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[OptionGroup Class](topic8608.md)   
[OptionGroup Members](topic8609.md)

©2024 DriveWorks Ltd. All Rights Reserved.
