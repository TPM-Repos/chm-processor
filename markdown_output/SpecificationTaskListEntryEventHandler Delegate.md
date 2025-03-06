SpecificationTaskListEntryEventHandler Delegate   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) : SpecificationTaskListEntryEventHandler Delegate  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_sender_
    The sender of the event.

_e_
    The event data.

Glossary Item Box

Represents a method that will handle events related to specification task list entries. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Delegate Sub SpecificationTaskListEntryEventHandler( _
       ByVal _sender_ As Object, _
       ByVal _e_ As [SpecificationTaskListEntryEventArgs](topic11548.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As New [SpecificationTaskListEntryEventHandler](topic11823.md)(AddressOf HandlerMethod)  
  
C#|   
---|---  
      
    
    public delegate void SpecificationTaskListEntryEventHandler( 
       object _sender_ ,
       [SpecificationTaskListEntryEventArgs](topic11548.md) _e_
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

[SpecificationTaskListEntryEventHandler Members](topic11823.md)   
[DriveWorks.Specification Namespace](topic10764.md)


