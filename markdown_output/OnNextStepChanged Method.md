Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
OnNextStepChanged Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [DiscreteWizardStep Class](topic750.md) : OnNextStepChanged Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_e_
    The event data.

Glossary Item Box

Raises the [NextStepChanged](topic769.md) event. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overridable Sub OnNextStepChanged( _
       ByVal _e_ As EventArgs _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [DiscreteWizardStep](topic750.md)
    Dim e As EventArgs
     
    instance.OnNextStepChanged(e)  
  
C#|   
---|---  
      
    
    protected virtual void OnNextStepChanged( 
       EventArgs _e_
    )  
  
#### Parameters

 _e_
    The event data.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DiscreteWizardStep Class](topic750.md)   
[DiscreteWizardStep Members](topic751.md)


