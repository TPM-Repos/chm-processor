![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
OnParentDefaultFontChanged Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [ButtonBase Class](topic7338.md) : OnParentDefaultFontChanged Method  
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
      
    
    Dim instance As [ButtonBase](topic7338.md)
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

[ButtonBase Class](topic7338.md)   
[ButtonBase Members](topic7339.md)


