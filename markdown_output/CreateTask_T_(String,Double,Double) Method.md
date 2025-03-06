![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

_T_
    The type of the task to add.

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTask<T>(String,Double,Double) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic11723.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [TaskSequence Class](topic11713.md) > [CreateTask Method](topic11720.md) : CreateTask<T>(String,Double,Double) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_title_
    The title of the task

_left_
    The left position of the task.

_top_
    The top position of the task.

Glossary Item Box

Creates and adds a new task to the task sequence. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function CreateTask(Of T As [Task](topic11629.md))( _
       ByVal _title_ As String, _
       ByVal _left_ As Double, _
       ByVal _top_ As Double _
    ) As T  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [TaskSequence](topic11713.md)
    Dim title As String
    Dim left As Double
    Dim top As Double
    Dim value As T
     
    value = instance.CreateTask(Of T)(title, left, top)  
  
C#|   
---|---  
      
    
    public T CreateTask<T>( 
       string _title_ ,
       double _left_ ,
       double _top_
    )
    where T: [Task](topic11629.md)  
  
#### Parameters

 _title_
    The title of the task
 _left_
    The left position of the task.
_top_
    The top position of the task.

#### Type Parameters

_T_
    The type of the task to add.

#### Return Value

The newly created task.

# ![](dotnetimages/collapse.gif)Exceptions

Exception| Description  
---|---  
System.ArgumentOutOfRangeException| The type specified in for the type parameter T isn't defined in a extension library.  
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[TaskSequence Class](topic11713.md)   
[TaskSequence Members](topic11714.md)   
[Overload List](topic11720.md)

©2024 DriveWorks Ltd. All Rights Reserved.
