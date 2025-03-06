![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxChangeScopedComponentTaskReleaseCondition Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic12999.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxChangeScopedComponentTaskReleaseCondition Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_scope_
    The scope of the task that owns the condition to change.

_taskName_
    The name of the task that owns the condition.

_conditionName_
    The name of the condition to change.

_title_
    The new title of the condition (or the old title if no change is desired).

_ruleChanges_
    The changes to the condition's rules to apply.

Glossary Item Box

Creates a new transaction that when executed will change the title of the given release condition. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxChangeScopedComponentTaskReleaseCondition( _
       ByVal _scope_ As String, _
       ByVal _taskName_ As String, _
       ByVal _conditionName_ As String, _
       ByVal _title_ As String, _
       ByVal ParamArray _ruleChanges_() As [FlowPropertyData](topic12873.md) _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim scope As String
    Dim taskName As String
    Dim conditionName As String
    Dim title As String
    Dim ruleChanges() As [FlowPropertyData](topic12873.md)
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxChangeScopedComponentTaskReleaseCondition(scope, taskName, conditionName, title, ruleChanges)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxChangeScopedComponentTaskReleaseCondition( 
       string _scope_ ,
       string _taskName_ ,
       string _conditionName_ ,
       string _title_ ,
       params [FlowPropertyData](topic12873.md)[] _ruleChanges_
    )  
  
#### Parameters

 _scope_
    The scope of the task that owns the condition to change.
_taskName_
    The name of the task that owns the condition.
_conditionName_
    The name of the condition to change.
_title_
    The new title of the condition (or the old title if no change is desired).
_ruleChanges_
    The changes to the condition's rules to apply.

#### Return Value

A transaction that when executed will change the title of the given task.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)

©2024 DriveWorks Ltd. All Rights Reserved.
