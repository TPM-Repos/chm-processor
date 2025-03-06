![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TaskExecutionException Constructor   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic11690.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [TaskExecutionException Class](topic11683.md) : TaskExecutionException Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_taskName_
    

_inner_
    

Glossary Item Box

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _taskName_ As String, _
       ByVal _inner_ As Exception _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim taskName As String
    Dim inner As Exception
     
    Dim instance As New [TaskExecutionException](topic11683.md)(taskName, inner)  
  
C#|   
---|---  
      
    
    public TaskExecutionException( 
       string _taskName_ ,
       Exception _inner_
    )  
  
#### Parameters

 _taskName_
    
_inner_
    

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[TaskExecutionException Class](topic11683.md)   
[TaskExecutionException Members](topic11684.md)

©2024 DriveWorks Ltd. All Rights Reserved.
