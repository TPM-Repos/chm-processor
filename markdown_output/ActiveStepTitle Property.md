Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ActiveStepTitle Property   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [WizardBase Class](topic1200.md) : ActiveStepTitle Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

If the value from the [ActiveStep](topic1232.md) property implements the [IWizardStep](topic648.md) interface then the title is returned from the active step, otherwise the [FallbackStepTitle](topic1239.md) is returned. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overridable ReadOnly Property ActiveStepTitle As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [WizardBase](topic1200.md)
    Dim value As String
     
    value = instance.ActiveStepTitle  
  
C#|   
---|---  
      
    
    protected virtual string ActiveStepTitle {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[WizardBase Class](topic1200.md)   
[WizardBase Members](topic1201.md)


