       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
StateEventHandler Delegate   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) : StateEventHandler Delegate  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_sender_
    The sender of the event.

_e_
    The event data.

Glossary Item Box

Represents a method which will handle a state event. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Delegate Sub StateEventHandler( _
       ByVal _sender_ As Object, _
       ByVal _e_ As [StateEventArgs](topic11590.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As New [StateEventHandler](topic11825.md)(AddressOf HandlerMethod)  
  
C#|   
---|---  
      
    
    public delegate void StateEventHandler( 
       object _sender_ ,
       [StateEventArgs](topic11590.md) _e_
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

[StateEventHandler Members](topic11825.md)   
[DriveWorks.Specification Namespace](topic10764.md)


