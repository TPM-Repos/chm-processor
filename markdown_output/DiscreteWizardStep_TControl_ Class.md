![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

_TControl_
    

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DiscreteWizardStep<TControl> Class   
[Members](topic771.md) See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic770.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) : DiscreteWizardStep<TControl> Class  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Represents a step in a discrete wizard. 

# ![](dotnetimages/collapse.gif)Object Model

![](dotnetdiagramimages/image11.png)

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Class DiscreteWizardStep(Of TControl As Control) 
       Inherits [DiscreteWizardStep](topic750.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [DiscreteWizardStep(Of TControl)](topic770.md)  
  
C#|   
---|---  
      
    
    public class DiscreteWizardStep<TControl> : [DiscreteWizardStep](topic750.md) 
    where TControl: Control  
  
# ![](dotnetimages/collapse.gif)Type Parameters

_TControl_
    

# ![](dotnetimages/collapse.gif)Remarks

This class uses demand creation of the control to reduce the time taken to show the wizard.

To get access to the wizard step from the control, create a property which has the same type as the wizard step and it will be initialized after the constructor is called.

# ![](dotnetimages/collapse.gif)Inheritance Hierarchy

System.Object  
[DriveWorks.Applications.DiscreteWizardStep](topic750.md)  
**DriveWorks.Applications.DiscreteWizardStep <TControl>**  


# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[DiscreteWizardStep<TControl> Members](topic771.md)   
[DriveWorks.Applications Namespace](topic16.md)

©2024 DriveWorks Ltd. All Rights Reserved.
