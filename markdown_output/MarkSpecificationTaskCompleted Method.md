![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
MarkSpecificationTaskCompleted Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3390.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSpecifications Class](topic3355.md) : MarkSpecificationTaskCompleted Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_taskId_
    The unique identifier of the task to mark.

_completed_
    True if the task is completed, otherwise false.

Glossary Item Box

Attempts to mark the specified specification task as being complete/incomplete. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function MarkSpecificationTaskCompleted( _
       ByVal _taskId_ As Guid, _
       ByVal _completed_ As Boolean _
    ) As Boolean  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [GroupSpecifications](topic3355.md)
    Dim taskId As Guid
    Dim completed As Boolean
    Dim value As Boolean
     
    value = instance.MarkSpecificationTaskCompleted(taskId, completed)  
  
C#|   
---|---  
      
    
    public bool MarkSpecificationTaskCompleted( 
       Guid _taskId_ ,
       bool _completed_
    )  
  
#### Parameters

 _taskId_
    The unique identifier of the task to mark.
_completed_
    True if the task is completed, otherwise false.

# ![](dotnetimages/collapse.gif)Remarks

This will reset the fail count of the task.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[GroupSpecifications Class](topic3355.md)   
[GroupSpecifications Members](topic3356.md)

©2024 DriveWorks Ltd. All Rights Reserved.
