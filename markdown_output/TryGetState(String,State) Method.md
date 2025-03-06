       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TryGetState(String,State) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [States Class](topic11612.md) > [TryGetState Method](topic11622.md) : TryGetState(String,State) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_title_
    The title of the state to try find.

_state_
    The matching state or null.

Glossary Item Box

Tries to get the state with the specified title. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function TryGetState( _
       ByVal _title_ As String, _
       ByRef _state_ As [State](topic11559.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [States](topic11612.md)
    Dim title As String
    Dim state As [State](topic11559.md)
    Dim value As Boolean
     
    value = instance.TryGetState(title, state)  
  
C#|   
---|---  
      
    
    public bool TryGetState( 
       string _title_ ,
       ref [State](topic11559.md) _state_
    )  
  
#### Parameters

 _title_
    The title of the state to try find.
_state_
    The matching state or null.

#### Return Value

True if the state is found.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[States Class](topic11612.md)   
[States Members](topic11613.md)   
[Overload List](topic11622.md)


