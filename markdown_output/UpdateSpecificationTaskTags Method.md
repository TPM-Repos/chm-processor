![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
UpdateSpecificationTaskTags Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3413.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSpecifications Class](topic3355.md) : UpdateSpecificationTaskTags Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_taskId_
    The unique identifier of the task to update.

_newTags_
    The new tags to associate with the task.

Glossary Item Box

Updates the tags for the specified specification task. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function UpdateSpecificationTaskTags( _
       ByVal _taskId_ As Guid, _
       ByVal _newTags_() As String _
    ) As Boolean  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [GroupSpecifications](topic3355.md)
    Dim taskId As Guid
    Dim newTags() As String
    Dim value As Boolean
     
    value = instance.UpdateSpecificationTaskTags(taskId, newTags)  
  
C#|   
---|---  
      
    
    public bool UpdateSpecificationTaskTags( 
       Guid _taskId_ ,
       string[] _newTags_
    )  
  
#### Parameters

 _taskId_
    The unique identifier of the task to update.
_newTags_
    The new tags to associate with the task.

#### Return Value

True if the tags were successfully updated, otherwise False.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[GroupSpecifications Class](topic3355.md)   
[GroupSpecifications Members](topic3356.md)

©2024 DriveWorks Ltd. All Rights Reserved.
