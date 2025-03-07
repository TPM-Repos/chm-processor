Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
EntryEventHandler Delegate   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Reporting Namespace](topic10334.md) : EntryEventHandler Delegate  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_sender_
    The sender of the event.

_e_
    The event data.

Glossary Item Box

Represents a method that will handle events related to report entries. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Delegate Sub EntryEventHandler( _
       ByVal _sender_ As Object, _
       ByVal _e_ As [EntryEventArgs](topic10379.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As New [EntryEventHandler](topic10508.md)(AddressOf HandlerMethod)  
  
C#|   
---|---  
      
    
    public delegate void EntryEventHandler( 
       object _sender_ ,
       [EntryEventArgs](topic10379.md) _e_
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

[EntryEventHandler Members](topic10508.md)   
[DriveWorks.Reporting Namespace](topic10334.md)


