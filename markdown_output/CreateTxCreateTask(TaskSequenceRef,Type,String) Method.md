![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxCreateTask(TaskSequenceRef,Type,String) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic13070.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) > [CreateTxCreateTask Method](topic13069.md) : CreateTxCreateTask(TaskSequenceRef,Type,String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_taskSequenceRef_
    The reference to the task sequence to modify.

_taskType_
    The type of task to create.

_taskTitle_
    The title to give the new task.

Glossary Item Box

Creates a transaction which, when committed, will create a new task. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function CreateTxCreateTask( _
       ByVal _taskSequenceRef_ As [TaskSequenceRef](topic13159.md), _
       ByVal _taskType_ As Type, _
       ByVal _taskTitle_ As String _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim taskSequenceRef As [TaskSequenceRef](topic13159.md)
    Dim taskType As Type
    Dim taskTitle As String
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxCreateTask(taskSequenceRef, taskType, taskTitle)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxCreateTask( 
       [TaskSequenceRef](topic13159.md) _taskSequenceRef_ ,
       Type _taskType_ ,
       string _taskTitle_
    )  
  
#### Parameters

 _taskSequenceRef_
    The reference to the task sequence to modify.
_taskType_
    The type of task to create.
_taskTitle_
    The title to give the new task.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)   
[Overload List](topic13069.md)

©2024 DriveWorks Ltd. All Rights Reserved.
