Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ControlEventHandler Delegate   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) : ControlEventHandler Delegate  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_sender_
    The sender of the event.

_e_
    The event data.

Glossary Item Box

Represents a method which will handle an event for an operation which affects a control. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Delegate Sub ControlEventHandler( _
       ByVal _sender_ As Object, _
       ByVal _e_ As [ControlEventArgs](topic7806.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As New [ControlEventHandler](topic9366.md)(AddressOf HandlerMethod)  
  
C#|   
---|---  
      
    
    public delegate void ControlEventHandler( 
       object _sender_ ,
       [ControlEventArgs](topic7806.md) _e_
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

[ControlEventHandler Members](topic9366.md)   
[DriveWorks.Forms Namespace](topic7266.md)


