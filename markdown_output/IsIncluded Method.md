Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IsIncluded Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [StateFilter Class](topic1077.md) : IsIncluded Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_state_
    The array of states that comprise the application state.

Glossary Item Box

Checks whether the state filter means that the filtered entity is included in the specified state. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function IsIncluded( _
       ByVal _state_() As Guid _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [StateFilter](topic1077.md)
    Dim state() As Guid
    Dim value As Boolean
     
    value = instance.IsIncluded(state)  
  
C#|   
---|---  
      
    
    public bool IsIncluded( 
       Guid[] _state_
    )  
  
#### Parameters

 _state_
    The array of states that comprise the application state.

#### Return Value

True if the filtered entity is included, false if the filtered entity is excluded.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[StateFilter Class](topic1077.md)   
[StateFilter Members](topic1078.md)


