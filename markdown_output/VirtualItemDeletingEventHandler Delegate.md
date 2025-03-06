       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
VirtualItemDeletingEventHandler Delegate   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic1274.md)  
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

©2024 DriveWorks Ltd. All Rights Reserved.
