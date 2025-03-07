Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
HideFromNavigation Property   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [DiscreteWizardStep Class](topic750.md) : HideFromNavigation Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Determines whether the step is added to the list of previous steps when it is navigated past. This is useful when a step acts as a transition between one step and another. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property HideFromNavigation As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [DiscreteWizardStep](topic750.md)
    Dim value As Boolean
     
    instance.HideFromNavigation = value
     
    value = instance.HideFromNavigation  
  
C#|   
---|---  
      
    
    public bool HideFromNavigation {get; set;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DiscreteWizardStep Class](topic750.md)   
[DiscreteWizardStep Members](topic751.md)


