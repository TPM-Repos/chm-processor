VirtualItemDeletedEventHandler Delegate   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) : VirtualItemDeletedEventHandler Delegate  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_sender_
    The sender of the event.

_e_
    The event data.

Glossary Item Box

Represents a method which will handle the [IVirtualSplitCommandButton.VirtualItemDeleted](topic604.md) event. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Delegate Sub VirtualItemDeletedEventHandler( _
       ByVal _sender_ As Object, _
       ByVal _e_ As [VirtualItemDeletedEventArgs](topic1167.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As New [VirtualItemDeletedEventHandler](topic1273.md)(AddressOf HandlerMethod)  
  
C#|   
---|---  
      
    
    public delegate void VirtualItemDeletedEventHandler( 
       object _sender_ ,
       [VirtualItemDeletedEventArgs](topic1167.md) _e_
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

[VirtualItemDeletedEventHandler Members](topic1273.md)   
[DriveWorks.Applications Namespace](topic16.md)


