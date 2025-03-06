SetExecutionResult Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [GenerationTask Class](topic13678.md) : SetExecutionResult Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_result_
    The execution result of this task.

_details_
    Additional information about the execution result of this task.

Glossary Item Box

Sets the result of this task. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Sub SetExecutionResult( _
       ByVal _result_ As [TaskExecutionResult](topic13454.md), _
       Optional ByVal _details_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GenerationTask](topic13678.md)
    Dim result As [TaskExecutionResult](topic13454.md)
    Dim details As String
     
    instance.SetExecutionResult(result, details)  
  
C#|   
---|---  
      
    
    protected void SetExecutionResult( 
       [TaskExecutionResult](topic13454.md) _result_ ,
       string _details_
    )  
  
#### Parameters

 _result_
    The execution result of this task.
_details_
    Additional information about the execution result of this task.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GenerationTask Class](topic13678.md)   
[GenerationTask Members](topic13679.md)


