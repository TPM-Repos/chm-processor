       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RuleChangedEventHandler Delegate   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms.DataModel Namespace](topic9371.md) : RuleChangedEventHandler Delegate  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_sender_
    The sender of the event.

_e_
    The event data.

Glossary Item Box

Represents the method that will handle a rule changed event. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Delegate Sub RuleChangedEventHandler( _
       ByVal _sender_ As Object, _
       ByVal _e_ As [RuleChangedEventArgs](topic9499.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As New [RuleChangedEventHandler](topic9589.md)(AddressOf HandlerMethod)  
  
C#|   
---|---  
      
    
    public delegate void RuleChangedEventHandler( 
       object _sender_ ,
       [RuleChangedEventArgs](topic9499.md) _e_
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

[RuleChangedEventHandler Members](topic9589.md)   
[DriveWorks.Forms.DataModel Namespace](topic9371.md)


