Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetProject(Guid) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupProjects Class](topic3190.md) > [GetProject Method](topic3208.md) : GetProject(Guid) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_projectId_
    The unique identifier of the project to retrieve.

Glossary Item Box

Gets the specified project's details. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function GetProject( _
       ByVal _projectId_ As Guid _
    ) As [ProjectDetails](topic4330.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupProjects](topic3190.md)
    Dim projectId As Guid
    Dim value As [ProjectDetails](topic4330.md)
     
    value = instance.GetProject(projectId)  
  
C#|   
---|---  
      
    
    public [ProjectDetails](topic4330.md) GetProject( 
       Guid _projectId_
    )  
  
#### Parameters

 _projectId_
    The unique identifier of the project to retrieve.

#### Return Value

The project details.

# Exceptions

Exception| Description  
---|---  
[ItemNotFoundException](topic3571.md)| Thrown if the specified project could not be found.  
  
# Remarks

This method will return a project even if the current user doesn't have access to the project.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupProjects Class](topic3190.md)   
[GroupProjects Members](topic3191.md)   
[Overload List](topic3208.md)


