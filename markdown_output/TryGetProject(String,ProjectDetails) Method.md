TryGetProject(String,ProjectDetails) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupProjects Class](topic3190.md) > [TryGetProject Method](topic3230.md) : TryGetProject(String,ProjectDetails) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_projectName_
    The name of the project to retrieve.

_projectDetails_
    A reference to a variable which will receive the project details.

Glossary Item Box

Gets the specified project's details. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function TryGetProject( _
       ByVal _projectName_ As String, _
       ByRef _projectDetails_ As [ProjectDetails](topic4330.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupProjects](topic3190.md)
    Dim projectName As String
    Dim projectDetails As [ProjectDetails](topic4330.md)
    Dim value As Boolean
     
    value = instance.TryGetProject(projectName, projectDetails)  
  
C#|   
---|---  
      
    
    public bool TryGetProject( 
       string _projectName_ ,
       ref [ProjectDetails](topic4330.md) _projectDetails_
    )  
  
#### Parameters

 _projectName_
    The name of the project to retrieve.
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


