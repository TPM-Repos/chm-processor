Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ProjectOpeningEventArgs Constructor   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ProjectOpeningEventArgs Class](topic898.md) : ProjectOpeningEventArgs Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_projectDetails_
    The [ProjectDetails](topic906.md) of the project that is opening.

Glossary Item Box

Creates a new instance of [ProjectOpeningEventArgs](topic898.md). 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _projectDetails_ As [ProjectDetails](topic4330.md) _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim projectDetails As [ProjectDetails](topic4330.md)
     
    Dim instance As New [ProjectOpeningEventArgs](topic898.md)(projectDetails)  
  
C#|   
---|---  
      
    
    public ProjectOpeningEventArgs( 
       [ProjectDetails](topic4330.md) _projectDetails_
    )  
  
#### Parameters

 _projectDetails_
    The [ProjectDetails](topic906.md) of the project that is opening.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectOpeningEventArgs Class](topic898.md)   
[ProjectOpeningEventArgs Members](topic899.md)


