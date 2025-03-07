Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
FallbackStepTitle Property   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [WizardBase Class](topic1200.md) : FallbackStepTitle Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Provides the title used for the active step if the value from the [ActiveStep](topic1232.md) property does not implement the [IWizardStep](topic648.md) interface. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overridable ReadOnly Property FallbackStepTitle As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [WizardBase](topic1200.md)
    Dim value As String
     
    value = instance.FallbackStepTitle  
  
C#|   
---|---  
      
    
    protected virtual string FallbackStepTitle {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[WizardBase Class](topic1200.md)   
[WizardBase Members](topic1201.md)


