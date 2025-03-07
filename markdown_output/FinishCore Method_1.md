Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
FinishCore Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [DiscreteWizardBase Class](topic737.md) : FinishCore Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Performs any additional processing required before finishing. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overridable Function FinishCore() As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [DiscreteWizardBase](topic737.md)
    Dim value As Boolean
     
    value = instance.FinishCore()  
  
C#|   
---|---  
      
    
    protected virtual bool FinishCore()  
  
#### Return Value

True if the finish operation is allowed to proceed.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DiscreteWizardBase Class](topic737.md)   
[DiscreteWizardBase Members](topic738.md)


