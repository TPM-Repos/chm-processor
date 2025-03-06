TransitionEventHandler Delegate   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) : TransitionEventHandler Delegate  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_sender_
    The sender of the event.

_e_
    The event data.

Glossary Item Box

Represents a method which will handle a transition event. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Delegate Sub TransitionEventHandler( _
       ByVal _sender_ As Object, _
       ByVal _e_ As [TransitionEventArgs](topic11776.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As New [TransitionEventHandler](topic11827.md)(AddressOf HandlerMethod)  
  
C#|   
---|---  
      
    
    public delegate void TransitionEventHandler( 
       object _sender_ ,
       [TransitionEventArgs](topic11776.md) _e_
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

[TransitionEventHandler Members](topic11827.md)   
[DriveWorks.Specification Namespace](topic10764.md)


