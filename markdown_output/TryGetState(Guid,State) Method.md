       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TryGetState(Guid,State) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [States Class](topic11612.md) > [TryGetState Method](topic11622.md) : TryGetState(Guid,State) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_stateId_
    The unique identifier of the state to get.

_state_
    A reference to a variable which will receive the state.

Glossary Item Box

Tries to get the state with the specified identifier. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function TryGetState( _
       ByVal _stateId_ As Guid, _
       ByRef _state_ As [State](topic11559.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [States](topic11612.md)
    Dim stateId As Guid
    Dim state As [State](topic11559.md)
    Dim value As Boolean
     
    value = instance.TryGetState(stateId, state)  
  
C#|   
---|---  
      
    
    public bool TryGetState( 
       Guid _stateId_ ,
       ref [State](topic11559.md) _state_
    )  
  
#### Parameters

 _stateId_
    The unique identifier of the state to get.
_state_
    A reference to a variable which will receive the state.

#### Return Value

True if the state was found and returned, otherwise false.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[States Class](topic11612.md)   
[States Members](topic11613.md)   
[Overload List](topic11622.md)


