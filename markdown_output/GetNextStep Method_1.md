Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetNextStep Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [DiscreteWizardStep<TControl> Class](topic770.md) : GetNextStep Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the next step if the state is valid, a null reference if the state is not valid, or [FinishStep](topic766.md) if the wizard's next action is to finish. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overrides Function GetNextStep() As [DiscreteWizardStep](topic750.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [DiscreteWizardStep(Of TControl)](topic770.md)
    Dim value As [DiscreteWizardStep](topic750.md)
     
    value = instance.GetNextStep()  
  
C#|   
---|---  
      
    
    public override [DiscreteWizardStep](topic750.md) GetNextStep()  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DiscreteWizardStep<TControl> Class](topic770.md)   
[DiscreteWizardStep<TControl> Members](topic771.md)


