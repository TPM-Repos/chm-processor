ViewActivating Event   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IViewEnvironment Interface](topic549.md) : ViewActivating Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

The event raised when the view is activating. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event ViewActivating As CancelEventHandler  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IViewEnvironment](topic549.md)
    Dim handler As CancelEventHandler
     
    AddHandler instance.ViewActivating, handler  
  
C#|   
---|---  
      
    
    event CancelEventHandler ViewActivating  
  
# Event Data

The event handler receives an argument of type CancelEventArgs containing data related to this event. The following **CancelEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
Cancel|   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IViewEnvironment Interface](topic549.md)   
[IViewEnvironment Members](topic550.md)


