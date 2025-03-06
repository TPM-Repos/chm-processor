![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
UsageFound Event   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic13226.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Utility Namespace](topic13190.md) > [RuleSearchProcess Class](topic13212.md) : UsageFound Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Occurs when a match has been found. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event UsageFound As EventHandler(Of RuleSearchResultEventArgs)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [RuleSearchProcess](topic13212.md)
    Dim handler As EventHandler(Of RuleSearchResultEventArgs)
     
    AddHandler instance.UsageFound, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<RuleSearchResultEventArgs> UsageFound  
  
# ![](dotnetimages/collapse.gif)Event Data

The event handler receives an argument of type [RuleSearchResultEventArgs](topic13242.md) containing data related to this event. The following **RuleSearchResultEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Item](topic13248.md)| The found item from the search.   
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[RuleSearchProcess Class](topic13212.md)   
[RuleSearchProcess Members](topic13213.md)

©2024 DriveWorks Ltd. All Rights Reserved.
