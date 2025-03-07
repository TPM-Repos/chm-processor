Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AreAllIncluded Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [StateFilter Class](topic1077.md) : AreAllIncluded Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_state_
    The array of states that comprise the application state.

Glossary Item Box

Checks whether the state filter means that the filtered entity is included in the specified state by verifying that all of the included states are included in the state. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function AreAllIncluded( _
       ByVal _state_() As Guid _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [StateFilter](topic1077.md)
    Dim state() As Guid
    Dim value As Boolean
     
    value = instance.AreAllIncluded(state)  
  
C#|   
---|---  
      
    
    public bool AreAllIncluded( 
       Guid[] _state_
    )  
  
#### Parameters

 _state_
    The array of states that comprise the application state.

#### Return Value

True if all included states in this state filter as present in the given array.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[StateFilter Class](topic1077.md)   
[StateFilter Members](topic1078.md)


