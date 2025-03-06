![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SetContext Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic1505.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Administrator.Extensibility.Diagnostics Namespace](topic1498.md) > [IRuleAnalyzerService Interface](topic1500.md) : SetContext Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_context_
    Object that contains rule to analyze

_specificationProject_
    The owning project for the context.

Glossary Item Box

Sets the object will that be shown in the rule analyzer. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub SetContext( _
       ByVal _context_ As [IHasRule](topic5947.md), _
       ByVal _specificationProject_ As [Project](topic3859.md) _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IRuleAnalyzerService](topic1500.md)
    Dim context As [IHasRule](topic5947.md)
    Dim specificationProject As [Project](topic3859.md)
     
    instance.SetContext(context, specificationProject)  
  
C#|   
---|---  
      
    
    void SetContext( 
       [IHasRule](topic5947.md) _context_ ,
       [Project](topic3859.md) _specificationProject_
    )  
  
#### Parameters

 _context_
    Object that contains rule to analyze
 _specificationProject_
    The owning project for the context.

# ![](dotnetimages/collapse.gif)Remarks

This will update the analyze button's enabled state depending on a valid context.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IRuleAnalyzerService Interface](topic1500.md)   
[IRuleAnalyzerService Members](topic1501.md)

©2024 DriveWorks Ltd. All Rights Reserved.
