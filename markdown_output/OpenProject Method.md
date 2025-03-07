Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
OpenProject Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IProjectService Interface](topic382.md) : OpenProject Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_projectName_
    The name of the project to open.

Glossary Item Box

Opens the specified project. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub OpenProject( _
       ByVal _projectName_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IProjectService](topic382.md)
    Dim projectName As String
     
    instance.OpenProject(projectName)  
  
C#|   
---|---  
      
    
    void OpenProject( 
       string _projectName_
    )  
  
#### Parameters

 _projectName_
    The name of the project to open.

# Exceptions

Exception| Description  
---|---  
System.InvalidOperationException| The implementation does not support projects being opened by 3rd party code.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IProjectService Interface](topic382.md)   
[IProjectService Members](topic383.md)


