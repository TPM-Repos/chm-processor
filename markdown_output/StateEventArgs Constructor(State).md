       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
StateEventArgs Constructor(State)   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic11597.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [StateEventArgs Class](topic11590.md) > [StateEventArgs Constructor](topic11596.md) : StateEventArgs Constructor(State)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_state_
    The state which is the target of the event.

Glossary Item Box

Initializes a new instance of the [StateEventArgs](topic11590.md) type. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _state_ As [State](topic11559.md) _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim state As [State](topic11559.md)
     
    Dim instance As New [StateEventArgs](topic11590.md)(state)  
  
C#|   
---|---  
      
    
    public StateEventArgs( 
       [State](topic11559.md) _state_
    )  
  
#### Parameters

 _state_
    The state which is the target of the event.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[StateEventArgs Class](topic11590.md)   
[StateEventArgs Members](topic11591.md)   
[Overload List](topic11596.md)

©2024 DriveWorks Ltd. All Rights Reserved.
