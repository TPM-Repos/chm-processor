Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
InvokeOperation(String) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationContext Class](topic11149.md) > [InvokeOperation Method](topic11170.md) : InvokeOperation(String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_operationName_
    The name of the operation to invoke.

Glossary Item Box

Invokes the specified operation. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function InvokeOperation( _
       ByVal _operationName_ As String _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationContext](topic11149.md)
    Dim operationName As String
    Dim value As Boolean
     
    value = instance.InvokeOperation(operationName)  
  
C#|   
---|---  
      
    
    public bool InvokeOperation( 
       string _operationName_
    )  
  
#### Parameters

 _operationName_
    The name of the operation to invoke.

#### Return Value

True if the operation was successfully invoked, false if one or more conditions caused the operation to be aborted.

# Exceptions

Exception| Description  
---|---  
[DriveWorks.ItemNotFoundException](topic3571.md)| The specified operation does not exist for the current state.  
System.UnauthorizedAccessException| Thrown if the current user does not have permission to invoke the operation.  
[TaskExecutionException](topic11683.md)| The transition can't be invoked because a task threw an unhandled exception.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationContext Class](topic11149.md)   
[SpecificationContext Members](topic11150.md)   
[Overload List](topic11170.md)


