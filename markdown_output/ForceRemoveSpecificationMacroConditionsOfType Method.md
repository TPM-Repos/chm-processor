Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ForceRemoveSpecificationMacroConditionsOfType Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectMaintenance Class](topic4579.md) : ForceRemoveSpecificationMacroConditionsOfType Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_projectPath_
    The full path to the project file to delete the conditions from.

_typeFullname_
    The full name of the type to remove.

Glossary Item Box

Forcefully removes all Specification Macro Conditions of the specified type in the given project.

Note: If you are able to open the project, consider using [DriveWorks.Specification.Condition.Delete](topic10811.md)() instead.

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Sub ForceRemoveSpecificationMacroConditionsOfType( _
       ByVal _projectPath_ As String, _
       ByVal _typeFullname_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim projectPath As String
    Dim typeFullname As String
     
    [ProjectMaintenance](topic4579.md).ForceRemoveSpecificationMacroConditionsOfType(projectPath, typeFullname)  
  
C#|   
---|---  
      
    
    public static void ForceRemoveSpecificationMacroConditionsOfType( 
       string _projectPath_ ,
       string _typeFullname_
    )  
  
#### Parameters

 _projectPath_
    The full path to the project file to delete the conditions from.
_typeFullname_
    The full name of the type to remove.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectMaintenance Class](topic4579.md)   
[ProjectMaintenance Members](topic4580.md)


