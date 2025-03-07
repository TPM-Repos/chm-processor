Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DiscreteWizardBase Class   
[Members](topic738.md)   
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) : DiscreteWizardBase Class  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Provides a base implementation of the [IWizard](topic613.md) interface which makes it easier to create wizards which are based on discrete steps for use with DriveWorks applications. 

# Object Model

![](dotnetdiagramimages/image9.png)

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public MustInherit Class DiscreteWizardBase 
       Implements [IWizard](topic613.md)   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [DiscreteWizardBase](topic737.md)  
  
C#|   
---|---  
      
    
    public abstract class DiscreteWizardBase : [IWizard](topic613.md)    
  
# Remarks

For general information about wizards, see the [IWizardService](topic642.md) service.

To make the wizard resizable, implement the [IDialogPreferences](topic195.md) interface.

# Inheritance Hierarchy

System.Object  
**DriveWorks.Applications.DiscreteWizardBase**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DiscreteWizardBase Members](topic738.md)   
[DriveWorks.Applications Namespace](topic16.md)


