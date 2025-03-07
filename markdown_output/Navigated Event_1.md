Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Navigated Event   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IWizard Interface](topic613.md) : Navigated Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised by the wizard when some action on the active step has changed the navigation, e.g. if validation has determined the user can no longer select Next, or if the wizard wants to manually switch to another step. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event Navigated As EventHandler  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IWizard](topic613.md)
    Dim handler As EventHandler
     
    AddHandler instance.Navigated, handler  
  
C#|   
---|---  
      
    
    event EventHandler Navigated  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IWizard Interface](topic613.md)   
[IWizard Members](topic614.md)


