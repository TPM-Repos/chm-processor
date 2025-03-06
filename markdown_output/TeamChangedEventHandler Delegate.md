       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TeamChangedEventHandler Delegate   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) : TeamChangedEventHandler Delegate  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_sender_
    The source of the event.

_e_
    The event data.

Glossary Item Box

Represents the method that will handle an event raised due to a team changing. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Delegate Sub TeamChangedEventHandler( _
       ByVal _sender_ As Object, _
       ByVal _e_ As TeamChangedEventArgs _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As New [TeamChangedEventHandler](topic5935.md)(AddressOf HandlerMethod)  
  
C#|   
---|---  
      
    
    public delegate void TeamChangedEventHandler( 
       object _sender_ ,
       TeamChangedEventArgs _e_
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

[TeamChangedEventHandler Members](topic5935.md)   
[DriveWorks Namespace](topic2159.md)


