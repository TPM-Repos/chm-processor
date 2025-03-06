ShowWizard Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IWizardService Interface](topic642.md) : ShowWizard Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_wizard_
    The wizard to run.

Glossary Item Box

Runs a wizard. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function ShowWizard( _
       ByVal _wizard_ As [IWizard](topic613.md) _
    ) As DialogResult  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IWizardService](topic642.md)
    Dim wizard As [IWizard](topic613.md)
    Dim value As DialogResult
     
    value = instance.ShowWizard(wizard)  
  
C#|   
---|---  
      
    
    DialogResult ShowWizard( 
       [IWizard](topic613.md) _wizard_
    )  
  
#### Parameters

 _wizard_
    The wizard to run.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IWizardService Interface](topic642.md)   
[IWizardService Members](topic643.md)


