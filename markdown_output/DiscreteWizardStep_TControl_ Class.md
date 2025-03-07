_TControl_
    

Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DiscreteWizardStep<TControl> Class   
[Members](topic771.md)   
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) : DiscreteWizardStep<TControl> Class  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Represents a step in a discrete wizard. 

# Object Model

![](dotnetdiagramimages/image11.png)

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Class DiscreteWizardStep(Of TControl As Control) 
       Inherits [DiscreteWizardStep](topic750.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [DiscreteWizardStep(Of TControl)](topic770.md)  
  
C#|   
---|---  
      
    
    public class DiscreteWizardStep<TControl> : [DiscreteWizardStep](topic750.md) 
    where TControl: Control  
  
# Type Parameters

_TControl_
    

# Remarks

This class uses demand creation of the control to reduce the time taken to show the wizard.

To get access to the wizard step from the control, create a property which has the same type as the wizard step and it will be initialized after the constructor is called.

# Inheritance Hierarchy

System.Object  
[DriveWorks.Applications.DiscreteWizardStep](topic750.md)  
**DriveWorks.Applications.DiscreteWizardStep <TControl>**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DiscreteWizardStep<TControl> Members](topic771.md)   
[DriveWorks.Applications Namespace](topic16.md)


