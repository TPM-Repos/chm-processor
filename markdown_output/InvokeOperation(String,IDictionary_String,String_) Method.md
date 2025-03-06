![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
InvokeOperation(String,IDictionary<String,String>) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic11172.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationContext Class](topic11149.md) > [InvokeOperation Method](topic11170.md) : InvokeOperation(String,IDictionary<String,String>) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_operationName_
    The name of the operation to invoke.

_inputs_
    Inputs to be driven in to spec

Glossary Item Box

Invokes the specified operation. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function InvokeOperation( _
       ByVal _operationName_ As String, _
       ByVal _inputs_ As IDictionary(Of String,String) _
    ) As Boolean  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [SpecificationContext](topic11149.md)
    Dim operationName As String
    Dim inputs As IDictionary(Of String,String)
    Dim value As Boolean
     
    value = instance.InvokeOperation(operationName, inputs)  
  
C#|   
---|---  
      
    
    public bool InvokeOperation( 
       string _operationName_ ,
       IDictionary<string,string> _inputs_
    )  
  
#### Parameters

 _operationName_
    The name of the operation to invoke.
_inputs_
    Inputs to be driven in to spec

#### Return Value

True if the operation was successfully invoked, false if one or more conditions caused the operation to be aborted.

# ![](dotnetimages/collapse.gif)Exceptions

Exception| Description  
---|---  
[DriveWorks.ItemNotFoundException](topic3571.md)| The specified operation does not exist for the current state.  
System.UnauthorizedAccessException| Thrown if the current user does not have permission to invoke the operation.  
[TaskExecutionException](topic11683.md)| The transition can't be invoked because a task threw an unhandled exception.  
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[SpecificationContext Class](topic11149.md)   
[SpecificationContext Members](topic11150.md)   
[Overload List](topic11170.md)

©2024 DriveWorks Ltd. All Rights Reserved.
