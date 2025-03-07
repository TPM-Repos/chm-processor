Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RegisterState Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Extensibility Namespace](topic1995.md) > [IApplicationStateManager Interface](topic2035.md) : RegisterState Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_stateId_
    The unique identifier of the state to register.

Glossary Item Box

Registers the given state and returns an object which can be used to control it. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function RegisterState( _
       ByVal _stateId_ As Guid _
    ) As [IApplicationStateController](topic2028.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IApplicationStateManager](topic2035.md)
    Dim stateId As Guid
    Dim value As [IApplicationStateController](topic2028.md)
     
    value = instance.RegisterState(stateId)  
  
C#|   
---|---  
      
    
    [IApplicationStateController](topic2028.md) RegisterState( 
       Guid _stateId_
    )  
  
#### Parameters

 _stateId_
    The unique identifier of the state to register.

#### Return Value

A state controller.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IApplicationStateManager Interface](topic2035.md)   
[IApplicationStateManager Members](topic2036.md)


