       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TryGetProject(Guid,ProjectDetails) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3232.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupProjects Class](topic3190.md) > [TryGetProject Method](topic3230.md) : TryGetProject(Guid,ProjectDetails) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_projectId_
    The unique identifier of the project to retrieve.

_projectDetails_
    A reference to a variable which will receive the project details.

Glossary Item Box

Gets the specified project's details. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function TryGetProject( _
       ByVal _projectId_ As Guid, _
       ByRef _projectDetails_ As [ProjectDetails](topic4330.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupProjects](topic3190.md)
    Dim projectId As Guid
    Dim projectDetails As [ProjectDetails](topic4330.md)
    Dim value As Boolean
     
    value = instance.TryGetProject(projectId, projectDetails)  
  
C#|   
---|---  
      
    
    public bool TryGetProject( 
       Guid _projectId_ ,
       ref [ProjectDetails](topic4330.md) _projectDetails_
    )  
  
#### Parameters

 _projectId_
    The unique identifier of the project to retrieve.
_projectDetails_
    A reference to a variable which will receive the project details.

#### Return Value

True if the project was found and returned, otherwise false.

# Remarks

This method will return a project even if the current user doesn't have access to the project.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupProjects Class](topic3190.md)   
[GroupProjects Members](topic3191.md)   
[Overload List](topic3230.md)

©2024 DriveWorks Ltd. All Rights Reserved.
