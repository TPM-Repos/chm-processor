Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
BeforeInvoke Event   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ICommandMonitor Interface](topic158.md) : BeforeInvoke Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the command is about to be invoked. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event BeforeInvoke As [CommandInvokeEventHandler](topic1267.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ICommandMonitor](topic158.md)
    Dim handler As [CommandInvokeEventHandler](topic1267.md)
     
    AddHandler instance.BeforeInvoke, handler  
  
C#|   
---|---  
      
    
    event [CommandInvokeEventHandler](topic1267.md) BeforeInvoke  
  
# Event Data

The event handler receives an argument of type [CommandInvokeEventArgs](topic691.md) containing data related to this event. The following **CommandInvokeEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[CommandContext](topic698.md)| Gets the context passed to the command's [ICommand.Invoke](topic84.md) method.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ICommandMonitor Interface](topic158.md)   
[ICommandMonitor Members](topic159.md)


