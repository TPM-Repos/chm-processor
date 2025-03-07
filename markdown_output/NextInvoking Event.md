Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
NextInvoking Event   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [WizardBase Class](topic1200.md) : NextInvoking Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when forward navigation is requested in the wizard. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Event NextInvoking As CancelEventHandler  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [WizardBase](topic1200.md)
    Dim handler As CancelEventHandler
     
    AddHandler instance.NextInvoking, handler  
  
C#|   
---|---  
      
    
    protected event CancelEventHandler NextInvoking  
  
# Event Data

The event handler receives an argument of type CancelEventArgs containing data related to this event. The following **CancelEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
Cancel|   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[WizardBase Class](topic1200.md)   
[WizardBase Members](topic1201.md)


