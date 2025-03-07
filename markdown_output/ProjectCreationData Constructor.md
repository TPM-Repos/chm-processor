Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ProjectCreationData Constructor   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Extensibility Namespace](topic1995.md) > [ProjectCreationData Class](topic2132.md) : ProjectCreationData Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_application_
    The application hosting the wizard.

_projectName_
    The name of the project to created if required by the template.

_projectFolder_
    The folder in which to create the project if required by the template.

_groupService_
    The group service.

_projectService_
    The project service.

Glossary Item Box

Initializes a new instance of the [ProjectCreationData](topic2132.md) type. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _application_ As [IApplication](topic24.md), _
       ByVal _projectName_ As String, _
       ByVal _projectFolder_ As String, _
       ByVal _groupService_ As [IGroupService](topic251.md), _
       ByVal _projectService_ As [IProjectService](topic382.md) _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim application As [IApplication](topic24.md)
    Dim projectName As String
    Dim projectFolder As String
    Dim groupService As [IGroupService](topic251.md)
    Dim projectService As [IProjectService](topic382.md)
     
    Dim instance As New [ProjectCreationData](topic2132.md)(application, projectName, projectFolder, groupService, projectService)  
  
C#|   
---|---  
      
    
    public ProjectCreationData( 
       [IApplication](topic24.md) _application_ ,
       string _projectName_ ,
       string _projectFolder_ ,
       [IGroupService](topic251.md) _groupService_ ,
       [IProjectService](topic382.md) _projectService_
    )  
  
#### Parameters

 _application_
    The application hosting the wizard.
_projectName_
    The name of the project to created if required by the template.
_projectFolder_
    The folder in which to create the project if required by the template.
_groupService_
    The group service.
_projectService_
    The project service.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectCreationData Class](topic2132.md)   
[ProjectCreationData Members](topic2133.md)


