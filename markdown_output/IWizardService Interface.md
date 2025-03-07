Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IWizardService Interface   
[Members](topic643.md)   
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) : IWizardService Interface  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Provides a contract for a service capable of running a wizard. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Interface IWizardService   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IWizardService](topic642.md)  
  
C#|   
---|---  
      
    
    public interface IWizardService   
  
# Remarks

Wizards are used throughout DriveWorks to perform common tasks, and are a key component of several major APIs such as the document designer framework exposed by DriveWorks Administrator.

Wizards can be implemented by implementing the [IWizard](topic613.md) interface directly, or by inheriting from either the higher-level [WizardBase](topic1200.md) or the [DiscreteWizardBase](topic737.md) base classes.

A wizard can support be resized by implementing the [IDialogPreferences](topic195.md) interface.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IWizardService Members](topic643.md)   
[DriveWorks.Applications Namespace](topic16.md)


