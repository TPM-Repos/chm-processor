Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
NextInvoked Event   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IWizard Interface](topic613.md) : NextInvoked Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised by the wizard when the next action has been invoked. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event NextInvoked As EventHandler  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IWizard](topic613.md)
    Dim handler As EventHandler
     
    AddHandler instance.NextInvoked, handler  
  
C#|   
---|---  
      
    
    event EventHandler NextInvoked  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IWizard Interface](topic613.md)   
[IWizard Members](topic614.md)


