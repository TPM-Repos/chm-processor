Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ProcessEventHandler Delegate   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Reporting Namespace](topic10334.md) : ProcessEventHandler Delegate  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_sender_
    The sender of the event.

_e_
    The event data.

Glossary Item Box

Represents a method that will handle events related to report processes. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Delegate Sub ProcessEventHandler( _
       ByVal _sender_ As Object, _
       ByVal _e_ As [ProcessEventArgs](topic10424.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As New [ProcessEventHandler](topic10509.md)(AddressOf HandlerMethod)  
  
C#|   
---|---  
      
    
    public delegate void ProcessEventHandler( 
       object _sender_ ,
       [ProcessEventArgs](topic10424.md) _e_
    )  
  
#### Parameters

 _sender_
    The sender of the event.
_e_
    The event data.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProcessEventHandler Members](topic10509.md)   
[DriveWorks.Reporting Namespace](topic10334.md)


