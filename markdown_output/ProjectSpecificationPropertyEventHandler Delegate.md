Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ProjectSpecificationPropertyEventHandler Delegate   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) : ProjectSpecificationPropertyEventHandler Delegate  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_sender_
    The sender of the event.

_e_
    The event data.

Glossary Item Box

Represents a method which will handle an event which affects a specification property. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Delegate Sub ProjectSpecificationPropertyEventHandler( _
       ByVal _sender_ As Object, _
       ByVal _e_ As [ProjectSpecificationPropertyEventArgs](topic4874.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As New [ProjectSpecificationPropertyEventHandler](topic5934.md)(AddressOf HandlerMethod)  
  
C#|   
---|---  
      
    
    public delegate void ProjectSpecificationPropertyEventHandler( 
       object _sender_ ,
       [ProjectSpecificationPropertyEventArgs](topic4874.md) _e_
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

[ProjectSpecificationPropertyEventHandler Members](topic5934.md)   
[DriveWorks Namespace](topic2159.md)


