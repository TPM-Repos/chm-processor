Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
PreviousInvoking Event   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IWizard Interface](topic613.md) : PreviousInvoking Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised by the wizard when the previous action is being invoked. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event PreviousInvoking As CancelEventHandler  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IWizard](topic613.md)
    Dim handler As CancelEventHandler
     
    AddHandler instance.PreviousInvoking, handler  
  
C#|   
---|---  
      
    
    event CancelEventHandler PreviousInvoking  
  
# Event Data

The event handler receives an argument of type CancelEventArgs containing data related to this event. The following **CancelEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
Cancel|   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IWizard Interface](topic613.md)   
[IWizard Members](topic614.md)


