![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetLocalizedName Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic5276.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [RuleSectionUtility Class](topic5269.md) : GetLocalizedName Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_section_
    The value to get the localized string of.

Glossary Item Box

Gets the localized name of the specified enum. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function GetLocalizedName( _
       ByVal _section_ As [RuleSection](topic2362.md) _
    ) As String  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim section As [RuleSection](topic2362.md)
    Dim value As String
     
    value = [RuleSectionUtility](topic5269.md).GetLocalizedName(section)  
  
C#|   
---|---  
      
    
    public static string GetLocalizedName( 
       [RuleSection](topic2362.md) _section_
    )  
  
#### Parameters

 _section_
    The value to get the localized string of.

#### Return Value

The localized name of the value.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[RuleSectionUtility Class](topic5269.md)   
[RuleSectionUtility Members](topic5270.md)

©2024 DriveWorks Ltd. All Rights Reserved.
