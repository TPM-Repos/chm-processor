       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TryUpdateProject Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3236.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupProjects Class](topic3190.md) : TryUpdateProject Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_projectDetails_
    The updated registration details for the project.

Glossary Item Box

Updates a project's registration details. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function TryUpdateProject( _
       ByVal _projectDetails_ As [ProjectDetails](topic4330.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupProjects](topic3190.md)
    Dim projectDetails As [ProjectDetails](topic4330.md)
    Dim value As Boolean
     
    value = instance.TryUpdateProject(projectDetails)  
  
C#|   
---|---  
      
    
    public bool TryUpdateProject( 
       [ProjectDetails](topic4330.md) _projectDetails_
    )  
  
#### Parameters

 _projectDetails_
    The updated registration details for the project.

#### Return Value

True if the project was successfully found and updated, otherwise false.

# Remarks

This method requires that the current user have edit permissions for the project.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupProjects Class](topic3190.md)   
[GroupProjects Members](topic3191.md)

©2024 DriveWorks Ltd. All Rights Reserved.
