Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ForceRemoveComponentTaskConditionsOfType Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectMaintenance Class](topic4579.md) : ForceRemoveComponentTaskConditionsOfType Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_projectPath_
    The full path to the project file to delete the Component Tasks Conditions from.

_conditionTypeName_
    The full name of the type to remove.

Glossary Item Box

Forcefully removes all component task conditions of the specified type in the given project.

Note: If you are able to open the project, consider using the [DriveWorks.Components.Tasks.ComponentTaskConditions](topic6561.md) API instead.

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Sub ForceRemoveComponentTaskConditionsOfType( _
       ByVal _projectPath_ As String, _
       ByVal _conditionTypeName_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim projectPath As String
    Dim conditionTypeName As String
     
    [ProjectMaintenance](topic4579.md).ForceRemoveComponentTaskConditionsOfType(projectPath, conditionTypeName)  
  
C#|   
---|---  
      
    
    public static void ForceRemoveComponentTaskConditionsOfType( 
       string _projectPath_ ,
       string _conditionTypeName_
    )  
  
#### Parameters

 _projectPath_
    The full path to the project file to delete the Component Tasks Conditions from.
_conditionTypeName_
    The full name of the type to remove.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectMaintenance Class](topic4579.md)   
[ProjectMaintenance Members](topic4580.md)


