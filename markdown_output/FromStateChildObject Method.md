Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
FromStateChildObject Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [TaskSequenceRef Class](topic13159.md) : FromStateChildObject Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_state_
    The state to which the transition, operation, or event belongs.

_obj_
    The transition, operation, or event for which to get a reference.

Glossary Item Box

Gets a task sequence ref from a transition, operation, or event on the given state. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function FromStateChildObject( _
       ByVal _state_ As [State](topic11559.md), _
       ByVal _obj_ As Object _
    ) As [TaskSequenceRef](topic13159.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim state As [State](topic11559.md)
    Dim obj As Object
    Dim value As [TaskSequenceRef](topic13159.md)
     
    value = [TaskSequenceRef](topic13159.md).FromStateChildObject(state, obj)  
  
C#|   
---|---  
      
    
    public static [TaskSequenceRef](topic13159.md) FromStateChildObject( 
       [State](topic11559.md) _state_ ,
       object _obj_
    )  
  
#### Parameters

 _state_
    The state to which the transition, operation, or event belongs.
_obj_
    The transition, operation, or event for which to get a reference.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[TaskSequenceRef Class](topic13159.md)   
[TaskSequenceRef Members](topic13160.md)


