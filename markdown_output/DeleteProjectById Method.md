Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DeleteProjectById Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupProjects Class](topic3190.md) : DeleteProjectById Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_projectId_
    The identifier which uniquely identifies the project to delete.

Glossary Item Box

Deletes an existing project using it's Id. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function DeleteProjectById( _
       ByVal _projectId_ As Guid _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupProjects](topic3190.md)
    Dim projectId As Guid
    Dim value As Boolean
     
    value = instance.DeleteProjectById(projectId)  
  
C#|   
---|---  
      
    
    public bool DeleteProjectById( 
       Guid _projectId_
    )  
  
#### Parameters

 _projectId_
    The identifier which uniquely identifies the project to delete.

#### Return Value

True if the project was found and deleted, otherwise false.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupProjects Class](topic3190.md)   
[GroupProjects Members](topic3191.md)


