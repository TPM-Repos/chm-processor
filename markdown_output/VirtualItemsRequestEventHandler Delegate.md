       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
VirtualItemsRequestEventHandler Delegate   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) : VirtualItemsRequestEventHandler Delegate  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_sender_
    The sender of the event.

_e_
    The event data for the event.

Glossary Item Box

The event handler delegate used for events such as [IVirtualSplitCommandButton.DropDownOpening](topic603.md) which request virtual items. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Delegate Sub VirtualItemsRequestEventHandler( _
       ByVal _sender_ As Object, _
       ByVal _e_ As [VirtualItemsRequestEventArgs](topic1192.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As New [VirtualItemsRequestEventHandler](topic1276.md)(AddressOf HandlerMethod)  
  
C#|   
---|---  
      
    
    public delegate void VirtualItemsRequestEventHandler( 
       object _sender_ ,
       [VirtualItemsRequestEventArgs](topic1192.md) _e_
    )  
  
#### Parameters

 _sender_
    The sender of the event.
_e_
    The event data for the event.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[VirtualItemsRequestEventHandler Members](topic1276.md)   
[DriveWorks.Applications Namespace](topic16.md)


