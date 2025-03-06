TaskEventHandler Delegate   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) : TaskEventHandler Delegate  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_sender_
    The sender of the event.

_e_
    The event data.

Glossary Item Box

Represents a method which will handle a task event. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Delegate Sub TaskEventHandler( _
       ByVal _sender_ As Object, _
       ByVal _e_ As [TaskEventArgs](topic11672.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As New [TaskEventHandler](topic11826.md)(AddressOf HandlerMethod)  
  
C#|   
---|---  
      
    
    public delegate void TaskEventHandler( 
       object _sender_ ,
       [TaskEventArgs](topic11672.md) _e_
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

[TaskEventHandler Members](topic11826.md)   
[DriveWorks.Specification Namespace](topic10764.md)


