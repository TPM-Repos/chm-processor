![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTask(Type,String) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic11725.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [TaskSequence Class](topic11713.md) > [CreateTask Method](topic11720.md) : CreateTask(Type,String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_taskType_
    The type of the task to add.

_title_
    The title of the task

Glossary Item Box

Creates and adds a new task to the task sequence. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function CreateTask( _
       ByVal _taskType_ As Type, _
       ByVal _title_ As String _
    ) As [Task](topic11629.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [TaskSequence](topic11713.md)
    Dim taskType As Type
    Dim title As String
    Dim value As [Task](topic11629.md)
     
    value = instance.CreateTask(taskType, title)  
  
C#|   
---|---  
      
    
    public [Task](topic11629.md) CreateTask( 
       Type _taskType_ ,
       string _title_
    )  
  
#### Parameters

 _taskType_
    The type of the task to add.
_title_
    The title of the task

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
