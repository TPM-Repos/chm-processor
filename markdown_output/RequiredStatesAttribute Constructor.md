RequiredStatesAttribute Constructor   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [RequiredStatesAttribute Class](topic13901.md) : RequiredStatesAttribute Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_states_
    The list of application states the application is required to be in for this entity to be visible.

Glossary Item Box

Creates a new instance of the [RequiredStatesAttribute](topic13901.md). 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal ParamArray _states_() As String _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim states() As String
     
    Dim instance As New [RequiredStatesAttribute](topic13901.md)(states)  
  
C#|   
---|---  
      
    
    public RequiredStatesAttribute( 
       params string[] _states_
    )  
  
#### Parameters

 _states_
    The list of application states the application is required to be in for this entity to be visible.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[RequiredStatesAttribute Class](topic13901.md)   
[RequiredStatesAttribute Members](topic13902.md)


