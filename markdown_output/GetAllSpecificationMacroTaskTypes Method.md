Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetAllSpecificationMacroTaskTypes Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectMaintenance Class](topic4579.md) : GetAllSpecificationMacroTaskTypes Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_projectPath_
    The full path to the project to load the types from.

Glossary Item Box

Retrieves a list of all types of specification macro tasks in the given project. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function GetAllSpecificationMacroTaskTypes( _
       ByVal _projectPath_ As String _
    ) As IEnumerable(Of String)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim projectPath As String
    Dim value As IEnumerable(Of String)
     
    value = [ProjectMaintenance](topic4579.md).GetAllSpecificationMacroTaskTypes(projectPath)  
  
C#|   
---|---  
      
    
    public static IEnumerable<string> GetAllSpecificationMacroTaskTypes( 
       string _projectPath_
    )  
  
#### Parameters

 _projectPath_
    The full path to the project to load the types from.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectMaintenance Class](topic4579.md)   
[ProjectMaintenance Members](topic4580.md)


