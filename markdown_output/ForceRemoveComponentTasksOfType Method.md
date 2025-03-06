![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ForceRemoveComponentTasksOfType Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic4586.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectMaintenance Class](topic4579.md) : ForceRemoveComponentTasksOfType Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_projectPath_
    The full path to the project file to delete the Component Tasks from.

_taskTypeName_
    The full name of the type to remove.

Glossary Item Box

Forcefully removes all component tasks of the specified type in the given project.

Note: If you are able to open the project, consider using [DriveWorks.Components.Tasks.ComponentTaskCollection.Remove](topic6485.md)(ComponentTask) instead.

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Sub ForceRemoveComponentTasksOfType( _
       ByVal _projectPath_ As String, _
       ByVal _taskTypeName_ As String _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim projectPath As String
    Dim taskTypeName As String
     
    [ProjectMaintenance](topic4579.md).ForceRemoveComponentTasksOfType(projectPath, taskTypeName)  
  
C#|   
---|---  
      
    
    public static void ForceRemoveComponentTasksOfType( 
       string _projectPath_ ,
       string _taskTypeName_
    )  
  
#### Parameters

 _projectPath_
    The full path to the project file to delete the Component Tasks from.
_taskTypeName_
    The full name of the type to remove.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectMaintenance Class](topic4579.md)   
[ProjectMaintenance Members](topic4580.md)

©2024 DriveWorks Ltd. All Rights Reserved.
