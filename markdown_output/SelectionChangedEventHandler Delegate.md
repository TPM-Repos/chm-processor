       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SelectionChangedEventHandler Delegate   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic1270.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) : SelectionChangedEventHandler Delegate  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_sender_
    The sender of the event.

_e_
    The event data.

Glossary Item Box

Represent the method that will handle selection change events. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Delegate Sub SelectionChangedEventHandler( _
       ByVal _sender_ As Object, _
       ByVal _e_ As [SelectionChangeEventArgs](topic926.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As New [SelectionChangedEventHandler](topic1270.md)(AddressOf HandlerMethod)  
  
C#|   
---|---  
      
    
    public delegate void SelectionChangedEventHandler( 
       object _sender_ ,
       [SelectionChangeEventArgs](topic926.md) _e_
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

[SelectionChangedEventHandler Members](topic1270.md)   
[DriveWorks.Applications Namespace](topic16.md)

©2024 DriveWorks Ltd. All Rights Reserved.
