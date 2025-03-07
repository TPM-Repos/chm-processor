Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ControlsEventHandler Delegate   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) : ControlsEventHandler Delegate  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_sender_
    The sender of the event.

_e_
    The event data.

Glossary Item Box

Represents a method which will handle an event for an operation which affects one or more controls. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Delegate Sub ControlsEventHandler( _
       ByVal _sender_ As Object, _
       ByVal _e_ As [ControlsEventArgs](topic7816.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As New [ControlsEventHandler](topic9367.md)(AddressOf HandlerMethod)  
  
C#|   
---|---  
      
    
    public delegate void ControlsEventHandler( 
       object _sender_ ,
       [ControlsEventArgs](topic7816.md) _e_
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

[ControlsEventHandler Members](topic9367.md)   
[DriveWorks.Forms Namespace](topic7266.md)


