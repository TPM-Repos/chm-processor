![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxCreateTaskFromExisting Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxCreateTaskFromExisting Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_taskSequenceRef_
    The reference to the task sequence to modify.

_taskType_
    The type of task to create.

_taskData_
    The XElement containing the data for the task.

_index_
    The index at which the task will be placed.

Glossary Item Box

Creates a transaction which, when committed, will create a new task from existing task data. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxCreateTaskFromExisting( _
       ByVal _taskSequenceRef_ As [TaskSequenceRef](topic13159.md), _
       ByVal _taskType_ As Type, _
       ByVal _taskData_ As XElement, _
       ByVal _index_ As Integer _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim taskSequenceRef As [TaskSequenceRef](topic13159.md)
    Dim taskType As Type
    Dim taskData As XElement
    Dim index As Integer
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxCreateTaskFromExisting(taskSequenceRef, taskType, taskData, index)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxCreateTaskFromExisting( 
       [TaskSequenceRef](topic13159.md) _taskSequenceRef_ ,
       Type _taskType_ ,
       XElement _taskData_ ,
       int _index_
    )  
  
#### Parameters

 _taskSequenceRef_
    The reference to the task sequence to modify.
_taskType_
    The type of task to create.
_taskData_
    The XElement containing the data for the task.
_index_
    The index at which the task will be placed.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


