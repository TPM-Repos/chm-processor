Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
MessageChangedEventHandler Delegate   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) : MessageChangedEventHandler Delegate  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_sender_
    The source of the event.

_e_
    The event data.

Glossary Item Box

Represents the method that will handle the event raised when a message is changed. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Delegate Sub MessageChangedEventHandler( _
       ByVal _sender_ As Object, _
       ByVal _e_ As [MessageEventArgs](topic3704.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As New [MessageChangedEventHandler](topic5932.md)(AddressOf HandlerMethod)  
  
C#|   
---|---  
      
    
    public delegate void MessageChangedEventHandler( 
       object _sender_ ,
       [MessageEventArgs](topic3704.md) _e_
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

[MessageChangedEventHandler Members](topic5932.md)   
[DriveWorks Namespace](topic2159.md)


