       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
VirtualItemSelectedEventHandler Delegate   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic1275.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) : VirtualItemSelectedEventHandler Delegate  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_sender_
    The sender of the event.

_e_
    The event data.

Glossary Item Box

Represents a method which will handle the [IVirtualSplitCommandButton.VirtualItemSelected](topic606.md) event. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Delegate Sub VirtualItemSelectedEventHandler( _
       ByVal _sender_ As Object, _
       ByVal _e_ As [VirtualItemSelectedEventArgs](topic1184.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As New [VirtualItemSelectedEventHandler](topic1275.md)(AddressOf HandlerMethod)  
  
C#|   
---|---  
      
    
    public delegate void VirtualItemSelectedEventHandler( 
       object _sender_ ,
       [VirtualItemSelectedEventArgs](topic1184.md) _e_
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

[VirtualItemSelectedEventHandler Members](topic1275.md)   
[DriveWorks.Applications Namespace](topic16.md)

©2024 DriveWorks Ltd. All Rights Reserved.
