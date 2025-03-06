![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTask(Type,String,Boolean) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [TaskSequence Class](topic11713.md) > [CreateTask Method](topic11720.md) : CreateTask(Type,String,Boolean) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_taskType_
    The type of the task to add.

_title_
    The title of the task

_createConnection_
    True to create a connection between this task and the previously added task. (Or Start if no other task has been added).

Glossary Item Box

Creates and adds a new task to the task sequence. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function CreateTask( _
       ByVal _taskType_ As Type, _
       ByVal _title_ As String, _
       ByVal _createConnection_ As Boolean _
    ) As [Task](topic11629.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [TaskSequence](topic11713.md)
    Dim taskType As Type
    Dim title As String
    Dim createConnection As Boolean
    Dim value As [Task](topic11629.md)
     
    value = instance.CreateTask(taskType, title, createConnection)  
  
C#|   
---|---  
      
    
    public [Task](topic11629.md) CreateTask( 
       Type _taskType_ ,
       string _title_ ,
       bool _createConnection_
    )  
  
#### Parameters

 _taskType_
    The type of the task to add.
_title_
    The title of the task
 _createConnection_
    True to create a connection between this task and the previously added task. (Or Start if no other task has been added).

#### Return Value

The newly created task.

# ![](dotnetimages/collapse.gif)Exceptions

Exception| Description  
---|---  
System.ArgumentOutOfRangeException| The type specified in taskType does not inherit from [Task](topic11629.md) or isn't defined in a extension library.  
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[TaskSequence Class](topic11713.md)   
[TaskSequence Members](topic11714.md)   
[Overload List](topic11720.md)


