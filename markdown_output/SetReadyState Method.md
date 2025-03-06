SetReadyState Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IStatusBarService Interface](topic495.md) : SetReadyState Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_newReadyState_
    The ready state to apply, or a null reference to reset the ready state to ready.

Glossary Item Box

Sets the caption displayed in the ready state panel of the status bar. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub SetReadyState( _
       ByVal _newReadyState_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IStatusBarService](topic495.md)
    Dim newReadyState As String
     
    instance.SetReadyState(newReadyState)  
  
C#|   
---|---  
      
    
    void SetReadyState( 
       string _newReadyState_
    )  
  
#### Parameters

 _newReadyState_
    The ready state to apply, or a null reference to reset the ready state to ready.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IStatusBarService Interface](topic495.md)   
[IStatusBarService Members](topic496.md)


