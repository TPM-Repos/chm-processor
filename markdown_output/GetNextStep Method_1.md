![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetNextStep Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic778.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [DiscreteWizardStep<TControl> Class](topic770.md) : GetNextStep Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the next step if the state is valid, a null reference if the state is not valid, or [FinishStep](topic766.md) if the wizard's next action is to finish. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overrides Function GetNextStep() As [DiscreteWizardStep](topic750.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [DiscreteWizardStep(Of TControl)](topic770.md)
    Dim value As [DiscreteWizardStep](topic750.md)
     
    value = instance.GetNextStep()  
  
C#|   
---|---  
      
    
    public override [DiscreteWizardStep](topic750.md) GetNextStep()  
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[DiscreteWizardStep<TControl> Class](topic770.md)   
[DiscreteWizardStep<TControl> Members](topic771.md)

©2024 DriveWorks Ltd. All Rights Reserved.
