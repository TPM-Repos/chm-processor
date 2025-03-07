Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CancelCore Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [DiscreteWizardBase Class](topic737.md) : CancelCore Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Performs any additional processing required before canceling. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overridable Function CancelCore() As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [DiscreteWizardBase](topic737.md)
    Dim value As Boolean
     
    value = instance.CancelCore()  
  
C#|   
---|---  
      
    
    protected virtual bool CancelCore()  
  
#### Return Value

True if the cancel operation is allowed to proceed.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DiscreteWizardBase Class](topic737.md)   
[DiscreteWizardBase Members](topic738.md)


