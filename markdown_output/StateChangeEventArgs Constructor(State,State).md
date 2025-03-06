       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
StateChangeEventArgs Constructor(State,State)   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic11585.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [StateChangeEventArgs Class](topic11578.md) > [StateChangeEventArgs Constructor](topic11584.md) : StateChangeEventArgs Constructor(State,State)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_sourceState_
    The state which is the source of the event.

_targetState_
    The state which is the target of the event.

Glossary Item Box

Initializes a new instance of the [StateChangeEventArgs](topic11578.md) type. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _sourceState_ As [State](topic11559.md), _
       ByVal _targetState_ As [State](topic11559.md) _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim sourceState As [State](topic11559.md)
    Dim targetState As [State](topic11559.md)
     
    Dim instance As New [StateChangeEventArgs](topic11578.md)(sourceState, targetState)  
  
C#|   
---|---  
      
    
    public StateChangeEventArgs( 
       [State](topic11559.md) _sourceState_ ,
       [State](topic11559.md) _targetState_
    )  
  
#### Parameters

 _sourceState_
    The state which is the source of the event.
_targetState_
    The state which is the target of the event.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[StateChangeEventArgs Class](topic11578.md)   
[StateChangeEventArgs Members](topic11579.md)   
[Overload List](topic11584.md)

©2024 DriveWorks Ltd. All Rights Reserved.
