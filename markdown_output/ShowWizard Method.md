![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ShowWizard Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic647.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IWizardService Interface](topic642.md) : ShowWizard Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_wizard_
    The wizard to run.

Glossary Item Box

Runs a wizard. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function ShowWizard( _
       ByVal _wizard_ As [IWizard](topic613.md) _
    ) As DialogResult  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IWizardService](topic642.md)
    Dim wizard As [IWizard](topic613.md)
    Dim value As DialogResult
     
    value = instance.ShowWizard(wizard)  
  
C#|   
---|---  
      
    
    DialogResult ShowWizard( 
       [IWizard](topic613.md) _wizard_
    )  
  
#### Parameters

 _wizard_
    The wizard to run.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IWizardService Interface](topic642.md)   
[IWizardService Members](topic643.md)

©2024 DriveWorks Ltd. All Rights Reserved.
