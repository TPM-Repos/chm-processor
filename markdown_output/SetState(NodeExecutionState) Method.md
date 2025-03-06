SetState(NodeExecutionState) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.EventFlow Namespace](topic6871.md) > [ExecutableNodeBase Class](topic6938.md) > [SetState Method](topic6950.md) : SetState(NodeExecutionState) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_state_
    The resultant state of executing this node.

Glossary Item Box

Sets the result of executing this node. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overloads Sub SetState( _
       ByVal _state_ As [NodeExecutionState](topic6900.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ExecutableNodeBase](topic6938.md)
    Dim state As [NodeExecutionState](topic6900.md)
     
    instance.SetState(state)  
  
C#|   
---|---  
      
    
    protected void SetState( 
       [NodeExecutionState](topic6900.md) _state_
    )  
  
#### Parameters

 _state_
    The resultant state of executing this node.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ExecutableNodeBase Class](topic6938.md)   
[ExecutableNodeBase Members](topic6939.md)   
[Overload List](topic6950.md)


