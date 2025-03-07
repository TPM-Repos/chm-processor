Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Initialize Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [DiscreteWizardBase Class](topic737.md) : Initialize Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_initialStep_
    The initial step.

Glossary Item Box

Called by the inheritor before the wizard is used to ensure that the initial state is setup. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Sub Initialize( _
       ByVal _initialStep_ As [DiscreteWizardStep](topic750.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [DiscreteWizardBase](topic737.md)
    Dim initialStep As [DiscreteWizardStep](topic750.md)
     
    instance.Initialize(initialStep)  
  
C#|   
---|---  
      
    
    protected void Initialize( 
       [DiscreteWizardStep](topic750.md) _initialStep_
    )  
  
#### Parameters

 _initialStep_
    The initial step.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DiscreteWizardBase Class](topic737.md)   
[DiscreteWizardBase Members](topic738.md)


