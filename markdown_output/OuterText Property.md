![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
OuterText Property   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic10552.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Rules Namespace](topic10510.md) > [IRuleNode Interface](topic10542.md) : OuterText Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

The outer text value for this node. Same as [RuleText](topic10553.md), but formatted with ideal white spaces. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    ReadOnly Property OuterText As String  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IRuleNode](topic10542.md)
    Dim value As String
     
    value = instance.OuterText  
  
C#|   
---|---  
      
    
    string OuterText {get;}  
  
# ![](dotnetimages/collapse.gif)Remarks

The outer text is the text of the node including its arguments, for example the outer text for an operator would be the left hand side, operator, and right hand side, and for an IF statement it would be the entire IF statement.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IRuleNode Interface](topic10542.md)   
[IRuleNode Members](topic10543.md)

©2024 DriveWorks Ltd. All Rights Reserved.
