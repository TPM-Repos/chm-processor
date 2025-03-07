Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
INotifyExceptionThrown.ExceptionThrownEventHandler Delegate   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) : INotifyExceptionThrown.ExceptionThrownEventHandler Delegate  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_sender_
    The sender of the event.

_e_
    The event information containing the exception.

Glossary Item Box

Represents a method that will handle the [INotifyExceptionThrown.ExceptionThrown](topic354.md) event. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Delegate Sub INotifyExceptionThrown.ExceptionThrownEventHandler( _
       ByVal _sender_ As Object, _
       ByVal _e_ As [ExceptionEventArgs](topic806.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As New [INotifyExceptionThrown.ExceptionThrownEventHandler](topic1269.md)(AddressOf HandlerMethod)  
  
C#|   
---|---  
      
    
    public delegate void INotifyExceptionThrown.ExceptionThrownEventHandler( 
       object _sender_ ,
       [ExceptionEventArgs](topic806.md) _e_
    )  
  
#### Parameters

 _sender_
    The sender of the event.
_e_
    The event information containing the exception.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[INotifyExceptionThrown.ExceptionThrownEventHandler Members](topic1269.md)   
[DriveWorks.Applications Namespace](topic16.md)


