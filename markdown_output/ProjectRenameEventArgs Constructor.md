Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ProjectRenameEventArgs Constructor   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ProjectRenameEventArgs Class](topic907.md) : ProjectRenameEventArgs Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_projectDetails_
    The [ProjectDetails](topic914.md) of the project that is being renamed.

Glossary Item Box

Creates a new instance of [ProjectRenameEventArgs](topic907.md). 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _projectDetails_ As [ProjectDetails](topic4330.md) _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim projectDetails As [ProjectDetails](topic4330.md)
     
    Dim instance As New [ProjectRenameEventArgs](topic907.md)(projectDetails)  
  
C#|   
---|---  
      
    
    public ProjectRenameEventArgs( 
       [ProjectDetails](topic4330.md) _projectDetails_
    )  
  
#### Parameters

 _projectDetails_
    The [ProjectDetails](topic914.md) of the project that is being renamed.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectRenameEventArgs Class](topic907.md)   
[ProjectRenameEventArgs Members](topic908.md)


