![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SetState(NodeExecutionState,String,String,Nullable<ReportingLevel>) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic6954.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.EventFlow Namespace](topic6871.md) > [ExecutableNodeBase Class](topic6938.md) > [SetState Method](topic6950.md) : SetState(NodeExecutionState,String,String,Nullable<ReportingLevel>) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_state_
    The resultant state of executing this node.

_result_
    The result of this node.

_details_
    A detailed message clarifying the result.

_reportLevelOverride_
    The reporting level to use when writing the result of this task.

Glossary Item Box

Sets the result of executing this node. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overloads Sub SetState( _
       ByVal _state_ As [NodeExecutionState](topic6900.md), _
       ByVal _result_ As String, _
       ByVal _details_ As String, _
       ByVal _reportLevelOverride_ As Nullable(Of ReportingLevel) _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ExecutableNodeBase](topic6938.md)
    Dim state As [NodeExecutionState](topic6900.md)
    Dim result As String
    Dim details As String
    Dim reportLevelOverride As Nullable(Of ReportingLevel)
     
    instance.SetState(state, result, details, reportLevelOverride)  
  
C#|   
---|---  
      
    
    protected void SetState( 
       [NodeExecutionState](topic6900.md) _state_ ,
       string _result_ ,
       string _details_ ,
       Nullable<ReportingLevel> _reportLevelOverride_
    )  
  
#### Parameters

 _state_
    The resultant state of executing this node.
_result_
    The result of this node.
_details_
    A detailed message clarifying the result.
_reportLevelOverride_
    The reporting level to use when writing the result of this task.

# ![](dotnetimages/collapse.gif)Remarks

The message passed into result will be written to the specification report.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ExecutableNodeBase Class](topic6938.md)   
[ExecutableNodeBase Members](topic6939.md)   
[Overload List](topic6950.md)

©2024 DriveWorks Ltd. All Rights Reserved.
