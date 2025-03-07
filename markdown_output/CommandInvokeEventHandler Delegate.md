Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CommandInvokeEventHandler Delegate   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) : CommandInvokeEventHandler Delegate  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_sender_
    The command sending the event.

_e_
    The event data which provides contextual information about the event.

Glossary Item Box

The event handler delegate for the various invocation events on the [ICommand](topic77.md) type. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Delegate Sub CommandInvokeEventHandler( _
       ByVal _sender_ As Object, _
       ByVal _e_ As [CommandInvokeEventArgs](topic691.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As New [CommandInvokeEventHandler](topic1267.md)(AddressOf HandlerMethod)  
  
C#|   
---|---  
      
    
    public delegate void CommandInvokeEventHandler( 
       object _sender_ ,
       [CommandInvokeEventArgs](topic691.md) _e_
    )  
  
#### Parameters

 _sender_
    The command sending the event.
_e_
    The event data which provides contextual information about the event.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[CommandInvokeEventHandler Members](topic1267.md)   
[DriveWorks.Applications Namespace](topic16.md)


