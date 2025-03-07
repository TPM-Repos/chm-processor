Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Invoking Event   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ICommandOverride Interface](topic180.md) : Invoking Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the command is being invoked. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event Invoking As [CommandInvokeEventHandler](topic1267.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ICommandOverride](topic180.md)
    Dim handler As [CommandInvokeEventHandler](topic1267.md)
     
    AddHandler instance.Invoking, handler  
  
C#|   
---|---  
      
    
    event [CommandInvokeEventHandler](topic1267.md) Invoking  
  
# Event Data

The event handler receives an argument of type [CommandInvokeEventArgs](topic691.md) containing data related to this event. The following **CommandInvokeEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[CommandContext](topic698.md)| Gets the context passed to the command's [ICommand.Invoke](topic84.md) method.   
  
# Remarks

The [Invoking](topic95.md) event on the [ICommand](topic77.md) is raised in addition to this event.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ICommandOverride Interface](topic180.md)   
[ICommandOverride Members](topic181.md)


