Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
PreviousInvoked Event   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IWizard Interface](topic613.md) : PreviousInvoked Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised by the wizard when the previous action has been invoked. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event PreviousInvoked As EventHandler  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IWizard](topic613.md)
    Dim handler As EventHandler
     
    AddHandler instance.PreviousInvoked, handler  
  
C#|   
---|---  
      
    
    event EventHandler PreviousInvoked  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IWizard Interface](topic613.md)   
[IWizard Members](topic614.md)


