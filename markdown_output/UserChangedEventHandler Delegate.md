       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
UserChangedEventHandler Delegate   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic5936.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) : UserChangedEventHandler Delegate  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_sender_
    The source of the event.

_e_
    The event data.

Glossary Item Box

Represents the method that will handle an event raised due to a user changing. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Delegate Sub UserChangedEventHandler( _
       ByVal _sender_ As Object, _
       ByVal _e_ As [UserChangedEventArgs](topic5800.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As New [UserChangedEventHandler](topic5936.md)(AddressOf HandlerMethod)  
  
C#|   
---|---  
      
    
    public delegate void UserChangedEventHandler( 
       object _sender_ ,
       [UserChangedEventArgs](topic5800.md) _e_
    )  
  
#### Parameters

 _sender_
    The source of the event.
_e_
    The event data.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[UserChangedEventHandler Members](topic5936.md)   
[DriveWorks Namespace](topic2159.md)

©2024 DriveWorks Ltd. All Rights Reserved.
