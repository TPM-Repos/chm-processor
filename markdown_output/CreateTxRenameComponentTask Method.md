![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxRenameComponentTask Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic13124.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxRenameComponentTask Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_task_
    The task to rename.

_newName_
    The new name to give the task.

_component_
    The component the task is associated with.

Glossary Item Box

Creates a new transaction that when executed will change the name of the given task. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxRenameComponentTask( _
       ByVal _task_ As [ComponentTask](topic6407.md), _
       ByVal _newName_ As String, _
       ByVal _component_ As [ProjectComponent](topic6183.md) _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim task As [ComponentTask](topic6407.md)
    Dim newName As String
    Dim component As [ProjectComponent](topic6183.md)
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxRenameComponentTask(task, newName, component)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxRenameComponentTask( 
       [ComponentTask](topic6407.md) _task_ ,
       string _newName_ ,
       [ProjectComponent](topic6183.md) _component_
    )  
  
#### Parameters

 _task_
    The task to rename.
_newName_
    The new name to give the task.
_component_
    The component the task is associated with.

#### Return Value

A transaction that when executed will change the name of the given task.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)

©2024 DriveWorks Ltd. All Rights Reserved.
