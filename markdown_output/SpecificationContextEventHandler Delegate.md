       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SpecificationContextEventHandler Delegate   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic11821.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) : SpecificationContextEventHandler Delegate  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_sender_
    The sender of the event.

_e_
    The event data.

Glossary Item Box

Represents a method that will handle events involving specification context. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Delegate Sub SpecificationContextEventHandler( _
       ByVal _sender_ As Object, _
       ByVal _e_ As [SpecificationContextEventArgs](topic11284.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As New [SpecificationContextEventHandler](topic11821.md)(AddressOf HandlerMethod)  
  
C#|   
---|---  
      
    
    public delegate void SpecificationContextEventHandler( 
       object _sender_ ,
       [SpecificationContextEventArgs](topic11284.md) _e_
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

[SpecificationContextEventHandler Members](topic11821.md)   
[DriveWorks.Specification Namespace](topic10764.md)

©2024 DriveWorks Ltd. All Rights Reserved.
