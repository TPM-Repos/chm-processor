WizardBase Class   
[Members](topic1201.md)   
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) : WizardBase Class  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Provides a base implementation of the [IWizard](topic613.md) interface which makes it easier to create wizards for use with DriveWorks applications. 

# Object Model

![](dotnetdiagramimages/image48.png)

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public MustInherit Class WizardBase 
       Implements [IDialogPreferences](topic195.md), [IWizard](topic613.md)   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [WizardBase](topic1200.md)  
  
C#|   
---|---  
      
    
    public abstract class WizardBase : [IDialogPreferences](topic195.md), [IWizard](topic613.md)    
  
# Remarks

For general information about wizards, see the [IWizardService](topic642.md) service.

To make the wizard resizable, implement the [IDialogPreferences](topic195.md) interface.

# Inheritance Hierarchy

System.Object  
**DriveWorks.Applications.WizardBase**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[WizardBase Members](topic1201.md)   
[DriveWorks.Applications Namespace](topic16.md)


