       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
StateChangeEventHandler Delegate   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) : StateChangeEventHandler Delegate  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_sender_
    The sender of the event.

_e_
    The event data.

Glossary Item Box

Represents a method which will handle a state change event. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Delegate Sub StateChangeEventHandler( _
       ByVal _sender_ As Object, _
       ByVal _e_ As [StateChangeEventArgs](topic11578.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As New [StateChangeEventHandler](topic11824.md)(AddressOf HandlerMethod)  
  
C#|   
---|---  
      
    
    public delegate void StateChangeEventHandler( 
       object _sender_ ,
       [StateChangeEventArgs](topic11578.md) _e_
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

[StateChangeEventHandler Members](topic11824.md)   
[DriveWorks.Specification Namespace](topic10764.md)


