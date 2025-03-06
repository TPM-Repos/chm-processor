![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RealRule Property   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic13238.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Utility Namespace](topic13190.md) > [RuleSearchResult Class](topic13227.md) : RealRule Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the underlying [DriveWorks.Abstractions.IHasRule](topic5947.md) or a generic wrapper. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overridable ReadOnly Property RealRule As [IHasRule](topic5947.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [RuleSearchResult](topic13227.md)
    Dim value As [IHasRule](topic5947.md)
     
    value = instance.RealRule  
  
C#|   
---|---  
      
    
    public virtual [IHasRule](topic5947.md) RealRule {get;}  
  
#### Property Value

The [DriveWorks.Abstractions.IHasRule](topic5947.md) for this item.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[RuleSearchResult Class](topic13227.md)   
[RuleSearchResult Members](topic13228.md)

©2024 DriveWorks Ltd. All Rights Reserved.
