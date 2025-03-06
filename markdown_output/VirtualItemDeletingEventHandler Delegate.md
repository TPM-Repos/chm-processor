VirtualItemDeletingEventHandler Delegate   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) : VirtualItemDeletingEventHandler Delegate  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_sender_
    The sender of the event.

_e_
    The evetn data.

Glossary Item Box

Represents a method which will handle the [IVirtualSplitCommandButton.VirtualItemDeleting](topic605.md) event. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Delegate Sub VirtualItemDeletingEventHandler( _
       ByVal _sender_ As Object, _
       ByVal _e_ As [VirtualItemDeletingEventArgs](topic1175.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As New [VirtualItemDeletingEventHandler](topic1274.md)(AddressOf HandlerMethod)  
  
C#|   
---|---  
      
    
    public delegate void VirtualItemDeletingEventHandler( 
       object _sender_ ,
       [VirtualItemDeletingEventArgs](topic1175.md) _e_
    )  
  
#### Parameters

 _sender_
    The sender of the event.
_e_
    The evetn data.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[VirtualItemDeletingEventHandler Members](topic1274.md)   
[DriveWorks.Applications Namespace](topic16.md)


