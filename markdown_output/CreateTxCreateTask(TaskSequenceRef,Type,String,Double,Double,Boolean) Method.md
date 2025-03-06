![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxCreateTask(TaskSequenceRef,Type,String,Double,Double,Boolean) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) > [CreateTxCreateTask Method](topic13069.md) : CreateTxCreateTask(TaskSequenceRef,Type,String,Double,Double,Boolean) Method  
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

_left_
    The left position of the task.

_top_
    The top position of the task.

_createConnection_
    True to create a connection to the previously added task (or Start if no other tasks have been added).

Glossary Item Box

Creates a transaction which, when committed, will create a new task. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function CreateTxCreateTask( _
       ByVal _taskSequenceRef_ As [TaskSequenceRef](topic13159.md), _
       ByVal _taskType_ As Type, _
       ByVal _taskTitle_ As String, _
       ByVal _left_ As Double, _
       ByVal _top_ As Double, _
       ByVal _createConnection_ As Boolean _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim taskSequenceRef As [TaskSequenceRef](topic13159.md)
    Dim taskType As Type
    Dim taskTitle As String
    Dim left As Double
    Dim top As Double
    Dim createConnection As Boolean
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxCreateTask(taskSequenceRef, taskType, taskTitle, left, top, createConnection)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxCreateTask( 
       [TaskSequenceRef](topic13159.md) _taskSequenceRef_ ,
       Type _taskType_ ,
       string _taskTitle_ ,
       double _left_ ,
       double _top_ ,
       bool _createConnection_
    )  
  
#### Parameters

 _taskSequenceRef_
    The reference to the task sequence to modify.
_taskType_
    The type of task to create.
_taskTitle_
    The title to give the new task.
_left_
    The left position of the task.
_top_
    The top position of the task.
_createConnection_
    True to create a connection to the previously added task (or Start if no other tasks have been added).

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)   
[Overload List](topic13069.md)


