Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ForceRemoveComponentTasksOfType Method   
  
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

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Sub ForceRemoveComponentTasksOfType( _
       ByVal _projectPath_ As String, _
       ByVal _taskTypeName_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
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

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectMaintenance Class](topic4579.md)   
[ProjectMaintenance Members](topic4580.md)


