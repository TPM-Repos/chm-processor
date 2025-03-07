Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
NextStepChanged Event   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [DiscreteWizardStep Class](topic750.md) : NextStepChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised if the next step has changed, e.g. a different option was chosen, or the state has become valid/invalid. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event NextStepChanged As EventHandler  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [DiscreteWizardStep](topic750.md)
    Dim handler As EventHandler
     
    AddHandler instance.NextStepChanged, handler  
  
C#|   
---|---  
      
    
    public event EventHandler NextStepChanged  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DiscreteWizardStep Class](topic750.md)   
[DiscreteWizardStep Members](topic751.md)


