Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ForceRemoveSpecificationMacroTasksOfType Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectMaintenance Class](topic4579.md) : ForceRemoveSpecificationMacroTasksOfType Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_projectPath_
    The full path to the project file to delete the Specification Macro Tasks from.

_typeFullname_
    The full name of the type to remove.

Glossary Item Box

Forcefully removes all specification macro tasks of the specified type in the given project.

Note: If you are able to open the project, consider using [DriveWorks.Specification.Task.Delete](topic11636.md)() instead.

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Sub ForceRemoveSpecificationMacroTasksOfType( _
       ByVal _projectPath_ As String, _
       ByVal _typeFullname_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim projectPath As String
    Dim typeFullname As String
     
    [ProjectMaintenance](topic4579.md).ForceRemoveSpecificationMacroTasksOfType(projectPath, typeFullname)  
  
C#|   
---|---  
      
    
    public static void ForceRemoveSpecificationMacroTasksOfType( 
       string _projectPath_ ,
       string _typeFullname_
    )  
  
#### Parameters

 _projectPath_
    The full path to the project file to delete the Specification Macro Tasks from.
_typeFullname_
    The full name of the type to remove.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectMaintenance Class](topic4579.md)   
[ProjectMaintenance Members](topic4580.md)


