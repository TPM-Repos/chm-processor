       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TransitionFailedEventArgs Constructor   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [TransitionFailedEventArgs Class](topic1968.md) : TransitionFailedEventArgs Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_exception_
    The exception that occurred during execution of the transition, e.g. if the transition could not be found, or the user doesn't have permissions to access the transition.

_result_
    The result of executing the transition, e.g. false if the conditions on the transition could not be satisfied.

Glossary Item Box

Initializes a new instance of the [TransitionFailedEventArgs](topic1968.md) class. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _exception_ As Exception, _
       ByVal _result_ As Boolean _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim exception As Exception
    Dim result As Boolean
     
    Dim instance As New [TransitionFailedEventArgs](topic1968.md)(exception, result)  
  
C#|   
---|---  
      
    
    public TransitionFailedEventArgs( 
       Exception _exception_ ,
       bool _result_
    )  
  
#### Parameters

 _exception_
    The exception that occurred during execution of the transition, e.g. if the transition could not be found, or the user doesn't have permissions to access the transition.
_result_
    The result of executing the transition, e.g. false if the conditions on the transition could not be satisfied.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[TransitionFailedEventArgs Class](topic1968.md)   
[TransitionFailedEventArgs Members](topic1969.md)


