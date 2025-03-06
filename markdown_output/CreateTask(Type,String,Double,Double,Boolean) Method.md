![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTask(Type,String,Double,Double,Boolean) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic11728.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [TaskSequence Class](topic11713.md) > [CreateTask Method](topic11720.md) : CreateTask(Type,String,Double,Double,Boolean) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_taskType_
    The type of the task to add.

_title_
    The title of the task

_left_
    The left position of the task.

_top_
    The top position of the task.

_createConnection_
    True to create a connection between the created task and the last added task.

Glossary Item Box

Creates and adds a new task to the task sequence. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function CreateTask( _
       ByVal _taskType_ As Type, _
       ByVal _title_ As String, _
       ByVal _left_ As Double, _
       ByVal _top_ As Double, _
       ByVal _createConnection_ As Boolean _
    ) As [Task](topic11629.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [TaskSequence](topic11713.md)
    Dim taskType As Type
    Dim title As String
    Dim left As Double
    Dim top As Double
    Dim createConnection As Boolean
    Dim value As [Task](topic11629.md)
     
    value = instance.CreateTask(taskType, title, left, top, createConnection)  
  
C#|   
---|---  
      
    
    public [Task](topic11629.md) CreateTask( 
       Type _taskType_ ,
       string _title_ ,
       double _left_ ,
       double _top_ ,
       bool _createConnection_
    )  
  
#### Parameters

 _taskType_
    The type of the task to add.
_title_
    The title of the task
 _left_
    The left position of the task.
_top_
    The top position of the task.
_createConnection_
    True to create a connection between the created task and the last added task.

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

©2024 DriveWorks Ltd. All Rights Reserved.
