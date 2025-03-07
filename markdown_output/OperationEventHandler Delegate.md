Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
OperationEventHandler Delegate   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) : OperationEventHandler Delegate  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_sender_
    The sender of the event.

_e_
    The event data.

Glossary Item Box

Represents a method which will handle an operation event. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Delegate Sub OperationEventHandler( _
       ByVal _sender_ As Object, _
       ByVal _e_ As [OperationEventArgs](topic11084.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As New [OperationEventHandler](topic11820.md)(AddressOf HandlerMethod)  
  
C#|   
---|---  
      
    
    public delegate void OperationEventHandler( 
       object _sender_ ,
       [OperationEventArgs](topic11084.md) _e_
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

[OperationEventHandler Members](topic11820.md)   
[DriveWorks.Specification Namespace](topic10764.md)


