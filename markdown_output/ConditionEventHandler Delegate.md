Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ConditionEventHandler Delegate   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) : ConditionEventHandler Delegate  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_sender_
    The sender of the event.

_e_
    The event data.

Glossary Item Box

Represents a method which will handle a condition event. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Delegate Sub ConditionEventHandler( _
       ByVal _sender_ As Object, _
       ByVal _e_ As [ConditionEventArgs](topic10843.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As New [ConditionEventHandler](topic11818.md)(AddressOf HandlerMethod)  
  
C#|   
---|---  
      
    
    public delegate void ConditionEventHandler( 
       object _sender_ ,
       [ConditionEventArgs](topic10843.md) _e_
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

[ConditionEventHandler Members](topic11818.md)   
[DriveWorks.Specification Namespace](topic10764.md)


