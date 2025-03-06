       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SpecificationDocumentEventHandler Delegate   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) : SpecificationDocumentEventHandler Delegate  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_sender_
    The sender of the event.

_e_
    The event data.

Glossary Item Box

Represents a method which will handle a specification document event. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Delegate Sub SpecificationDocumentEventHandler( _
       ByVal _sender_ As Object, _
       ByVal _e_ As [SpecificationDocumentEventArgs](topic11344.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As New [SpecificationDocumentEventHandler](topic11822.md)(AddressOf HandlerMethod)  
  
C#|   
---|---  
      
    
    public delegate void SpecificationDocumentEventHandler( 
       object _sender_ ,
       [SpecificationDocumentEventArgs](topic11344.md) _e_
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

[SpecificationDocumentEventHandler Members](topic11822.md)   
[DriveWorks.Specification Namespace](topic10764.md)


